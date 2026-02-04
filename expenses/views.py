from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

def dashboard(request):
    expenses = Expense.objects.all().order_by('-date')

    total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    commute_total = Expense.objects.filter(
        category__in=['TO_UNI', 'FROM_UNI']
    ).aggregate(Sum('amount'))['amount__sum'] or 0
    lunch_total = Expense.objects.filter(
        category='LUNCH'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    other_total = total - commute_total - lunch_total

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/dashboard.html', {
        'form': form,
        'expenses': expenses,
        'total': total,
        'commute_total': commute_total,
        'lunch_total': lunch_total,
        'other_total': other_total,
    })

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from expenses.models import Expense

class Command(BaseCommand):
    help = "Import expenses from CSV"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Try different date formats
                date_str = row['date']
                date_obj = None
                
                # Try M/D/YYYY format first
                for fmt in ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y']:
                    try:
                        date_obj = datetime.strptime(date_str, fmt).date()
                        break
                    except ValueError:
                        continue
                
                if date_obj is None:
                    self.stdout.write(self.style.ERROR(f"Could not parse date: {date_str}"))
                    continue

                Expense.objects.create(
                    amount=int(row['amount']),
                    category=row['category'],
                    date=date_obj,
                    note=row.get('note', '')
                )

        self.stdout.write(self.style.SUCCESS("Expenses imported successfully"))
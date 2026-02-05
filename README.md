# Carpool Expense Tracker

A Django-based web application to track **university commute and food expenses** with analytics, charts, and cloud deployment.

---

## Features

- Add expenses with **categories**: Going to Uni, Coming from Uni, Lunch, Other
- **Dynamic total spending** and category-specific insights
- **Visual breakdown** via Chart.js
- Responsive **Bootstrap 5 UI**
- Persistent cloud database with **PostgreSQL**
- Admin panel for managing expenses

---

## Tech Stack

- Backend: Django 4+
- Database: PostgreSQL (Render free-tier)
- Frontend: Bootstrap 5 + Chart.js
- Deployment: Render.com
- Python: 3.10+

## Setup Instructions (Development)

1. **Clone the repository:**


git clone https://github.com/YOUR-USERNAME/CarpoolExpenseTracker.git

cd CarpoolExpenseTracker

2. **Create and activate a virtual environment:**

python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Install dependencies:**

pip install -r requirements.txt

Run migrations:

4. **Run migrations:**

python manage.py migrate

Start the development server:

5. **Start the development server:**

python manage.py runserver

Open your browser at http://127.0.0.1:8000/

---
## Usage
- Add your daily commute and lunch expenses
- View total spending and category breakdown
- Filter expenses by category
- Admin panel to manage all records
--
## Future Improvements
- Authentication (multi-user support)

- Monthly/weekly filters

- CSV export/import

- Mobile PWA version

Author
Syed Muhammad Shubair Hyder
GitHub: SyedMuhammadShubairHyder

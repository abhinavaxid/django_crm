# django_crm
Django CRM Project

This project is a Customer Relationship Management (CRM) system built using Django framework. It provides functionalities to manage customers, contacts, interactions, and opportunities.

Features:
- Customer Management: CRUD operations for managing customer information.
- Contact Management: CRUD operations for managing contacts associated with customers.
- Interaction Tracking: Log interactions (calls, meetings, emails) with customers.
- Opportunity : Track sales opportunities and their stages.
- Dashboard: Display key metrics.

Prerequisites:
- Python (>=3.6)
- Django (>=3.0)
- SQLite
- Git (optional, for version control)

Installation:
1. Clone the repository:git clone https://github.com/abhinavaxid/winaim_assessment.git
cd django-crm

2. Create a virtual environment:
python -m venv venv


3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install dependencies:
pip install -r requirements.txt

5. Apply database migrations:
python manage.py migrate


6. Create a superuser (admin):
python manage.py createsuperuser



7. Start the development server:
python manage.py runserver


8. Open your web browser and go to http://localhost:8000/admin/ to access the admin interface and http://localhost:8000/ to access the CRM system.

Usage:
- Navigate to http://localhost:8000/ to use the CRM system.
- Use the admin interface at http://localhost:8000/admin/ to manage database records (e.g., customers, contacts, interactions).
- Use the API endpoints for programmatic access to CRM functionalities.

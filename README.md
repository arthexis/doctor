# Doctor Django Starter

This repository contains a minimal Django project configured for local development. It provides a health-check endpoint to verify the server is running and ready for further development.

## Requirements
- Python 3.11+
- pip

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations and run the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
3. Visit the health check endpoint at [http://localhost:8000/health/](http://localhost:8000/health/).

## Testing
Run the Django test suite:
```bash
python manage.py test
```

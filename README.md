# AccuDesk
The application provides all basic functionality required for Personal accounting.
## Tools
1. Python
2. Django
3. Sqlite

## How to run application:
### pre-reqs:
    1. Python
    2. pip

### Steps:
1. install required packages using requirements.txt  
   `pip install -r requirements.txt`
2. migrate models to database using  
   `python manage.py migrate` or  
    `python3 manage.py migrate` (in case you have multiple versions of python installed)
3. add superuser using  
    `python manage.py createsuperuser` or  
    `python3 manage.py createsuperuser` (in case you have multiple versions of python installed)
4. run application using command  
    `python manage.py runserver` or  
   `python3 manage.py runserver` (in case you have multiple versions of python installed)

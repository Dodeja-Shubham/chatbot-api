# chatbot-api

## Build

###### Virtual Enviornment activation
- `sudo apt install python3-venv`
- `python3 -m venv name_of_virtual_environment`
- `source name_of_virtual_environment/bin/activate`
###### Setting up project (Install requirements)
- `Pip install -r requirements.txt`
###### Create super user for admin
- `python manage.py createsuperuser` 
###### Execute the project
- `python manage.py runserver `




## Change Database Character-set to utf-8 for globalization
- `ALTER TABLE table_name CONVERT TO CHARACTER SET utf8;`

## Resources

- [Django documentation](https://www.djangoproject.com/)
- [PostgreSQL Adapter](https://pypi.org/project/psycopg2/)
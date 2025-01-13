# Fixapp-Backend
Backend of web application in which professionals are loaded so that users find the necessary solution
# Create a virtual environment
python3 -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
# Install Dependencies
pip install -r requirements.txt
# Create/Update requirements.txt
pip freeze > requirements.txt
# Create migrations
python manage.py makemigrations
# Apply migrations
python manage.py migrate
# Run server
python manage.py runserver
# Create superuser
python manage.py createsuperuser
admin
admin@gmail.com
1234



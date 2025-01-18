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

#To install dlib i have to install 1. On Windows
Download and install CMake from the official website: https://cmake.org/download/.
During installation, make sure to select the option to Add CMake to PATH for all users.
2. Install Visual Studio Build Tools (Windows Only)
For Windows, dlib also requires a C++ compiler. You can install the Visual Studio Build Tools:

Download the build tools from Visual Studio Build Tools.
During installation, select the C++ build tools workload.

"""
    Django Quick Start
    ---
"""

"""
    - Install Django
    sudo pip3 install django
    - Update django to latest version
    sudo pip3 install django -U
    - Check Django version
    python3 -m django --version
    - Create new Django project
    django-admin startproject project_name
    - Create new Django app
    django-admin startapp app_name
"""

# Django Check list
print("Remember to add your app to INSTALLED_APPS in settings.py")
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    ...
]

print("Create/update models in models.py")  # Database tables/columns

print("Make migrations:")
"""
    python3 manage.py makemigrations
    python3 manage.py migrate
"""

# creating a minimal admin interface for checking database functionality
# is HIGHLY recommended
print("Create/update admin.py")
"""
    python3 manage.py runserver
    python3 manage.py runserver 0:8080
"""

# Setting Django to Run in Public IP Address
"""
    1. Open the required inbound and outbound ports for your
    virtual machine in Azure Portal. E.g. open port 8080
    2. Edit your django settings.py
    ALLOWED_HOSTS = ["your_servers_ip_address"]
    3. Run the development server like below
    python3 manage.py runserver 0:8080
"""

# Django Debug Toolbar
# a useful debugging tool for Django web applications

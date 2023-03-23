"""
    Virtual Environments with Python
    ---
    Additional information
    - Virtual Environments and Packages - Python Tutorial
    https://docs.python.org/3/tutorial/venv.html
    - Pipenv and Virtual Environments
    https://docs.python-guide.org/dev/virtualenvs/
    - Python Virtual Environments: Primer
    https://realpython.com/python-virtual-environments-a-primer/
"""

"""
    1.) Install virtualenv tool
    pip3 install virtualenv

    2.) Create a new virtual environment
    cd project_folder
    virtualenv venv

    3.) Activate virtual environment
    source venv/bin/activate  - Linux
    venv/venv/activate.bat    - Windows

    4.) Install packages like usual
    pip3 install package

    5.) Deactivate
    deactivate

    6.) Delete virtual environment
    rm -rf venv
"""

# Using Requirements
# Creating a requirements.txt file, which describes what Python libraries
# and their versions are needed for a project

"""
    pip3 freeze > requirements.txt - create the req files
    cat requirements.txt
    pip3 install -r requirements.txt - install the needed files
"""

# Using pipenv
# Pipenv is a higher lever user-interface for virtualenv
"""
    - pip3 install --user pipenv
    - cd project_folder
    - pipenv install package
    - pipenv run python3 main.py
    - pipenv shell
    - deactivate
"""

# You can also use the built-in venv module:
# python3 -m venv /path/to/virtual/environment
# Check the python3 docs for more info:

# Virtualenvwrapper
# this makes using virtual environments easier:
"""
    mkvirtualenv envname  - Create a new environment
    workon project_folder - Work on project
    lsvirtualenv          - List all virtual envs
    cdvirtualenv          - Navigate to current virtual env
    cdsitepackages        - cd into site-packages directory
    lssitepackages        - list site-packages directory
"""

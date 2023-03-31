"""
    How to migrate from the default sqlite to MySql
    in your Django project.
"""

print("Steps to migrating from sqlite to mysql:")
print("-----")
# install the services and packages
print("1) sudo apt -y install mysql-server")
print("2) sudo service mysql start")
print("3) sudo mysql_secure_installation utility")
print("4) sudo apt -y install libmysqlclient-dev")
# don't forget this part!
print("5) sudo pip3 install mysqlclient")
# log into mysql with the root user, creating a password in the process
print("6) sudo mysql -u root -p")
# create database
print("7) mysql> create database djangodb CHARACTER SET utf8;")
# create another user that isn't a root user
print("8) mysql> CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'user_password';")
print("9) mysql> FLUSH PRIVILEGES;")
# give the user all privileges on the current table.
# so that we don't have to use root for it, therefore making the database more secure
print("mysql> SELECT User, Host, authentication_string FROM mysql.user;")
print("mysql> GRANT ALL PRIVILEGES ON djangodb.* to user_name@localhost;")
print("mysql> FLUSH PRIVILEGES;")
# check that all permissions worked
print("mysql> SHOW GRANTS FOR 'user_name'@'localhost';")
# activate the current database
print("mysql> use djangodb")
print("mysql> CREATE TABLE student(id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INT NOT NULL);")
print("mysql> INSERT INTO student VALUES (1, 'Jack Student', 20), (2, 'Yrjö Pulkkinen', 31), (3, 'Arja Hämäläinen', 27);")
# check that the database works as expected
print("mysql> SELECT * FROM student ORDER BY name;")
# drop the test database
print("mysql> DROP TABLE student;")
# It is a good idea to back up your previous database data:
print("10) python3 manage.py dumpdata --indent 4 polls > polls.json")
print("11) python3 manage.py dumpdata --indent 4 > all.json")
# To make MySQL work with Django, you must first install a mysqlclient client with pip3
# Next change the settings.py of the Django project (comment out the old settings)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'user_name',
        'PASSWORD': 'user_password',
        'HOST': '127.0.0.1',  # localhost
        'PORT': '',
    }
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}
print("12) paste the following into your settings.py\n", DATABASES)
# after you have made the changes into your settings.py
print("13) python3 manage.py migrate")
# create an admin user again
print("14) python3 manage.py createsuperuser")
# load the data from the previous database
print("15) python3 manage.py loaddata polls.json")
# the following might fail due to mismatching user keys
print("16) python3 manage.py loaddata all.json")

# Test that everything works with MySQL

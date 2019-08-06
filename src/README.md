# Todo Task1 Restful API

This repository provides a sample django-rest-framework based upon the [Task1 Project].

The application allows users to create todo list entries. User location / IP address gets recorded against the created todo list. If geoip location API is present the user's location details like City and Country get added to the details of the todo item.  

Running the app in virtual enviroment will utilise SQLite. Cloud deployment to AWS ECS uses MYSQL database. 


## Quick Start

You can use the `todotask1 by running it in a virtual enviroment: `_::
    
    $ cd todotask1/src
    $ virtualenv .venv -p python3
    $ source .venv/bin/activate
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt 
    (env) $ python manage.py makemigrations
    (env) $ python manage.py migrate
    (env) $ python manage.py runserver 0.0.0.0:5557
    #To exist or deactivate the virtual enviroment 
    (env) $ deactivate

You can test by sending a simple curl request: _::

curl http://localhost:5558/todos?format=json


## Requirments 


PIP: _::
(env) $ cat requirments.txt 
backoff==1.8.0
certifi==2019.6.16
chardet==3.0.4
Django==2.0
django-cors-headers==2.1.0
djangorestframework==3.7.3
idna==2.8
ipify==1.0.0
mysql-connector-python==8.0.11
protobuf==3.9.0
pytz==2017.3
requests==2.22.0
retrying==1.3.3
six==1.12.0
urllib3==1.25.3
uWSGI==2.0.17

ipify - end user ip address 
retrying - adding retry behavior to the api calls  


## Disclaimer


Please note that this app is not production ready and must not be used in production envirment. 
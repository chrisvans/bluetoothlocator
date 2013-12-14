bluetoothlocator setup instructions
===================================

We are using postgres, you'll need to set up a local postgres database.

Set up a username_local.py file in the config folder, username is your name.

Add this line at the top of the file:


import * from common


In the same file, reference your local DB like so (insert your own values for those surrounded by {{}} ): 


    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': '{{ POSTGRES DATABASE NAME }}',

            'USER': '{{ DATABASE OWNER USERNAME }}',

            'PASSWORD': '{{ DATABASE OWNER PASSWORD }}',

            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.

            'PORT': '',                      # Set to empty string for default.

        }

    }


In your .bashrc file, include this:


export DJANGO_BLUETOOTH_SECRET='insert_random_string_of_letters_here'


Make sure to reload your terminal if it is open after editing your .bashrc file, or do this in the terminal:


source ~/.bashrc


To get setup on your local environment:


pip install -r requirements.txt
python manage.py syncdb


(( At this point, it will ask you to set a superuser.  Since this is local, set up a simple username / password that you will not forget. ))


python manage.py migrate


This will tell south to run the migrations currently in the migrations folder.

To run the server, use: 

python manage.py runserver --settings=config.username_local


To run the django app in a shell, use: 


python manage.py shell --settings=config.username_local


To create a test object under the current schema, do this in the shell:


import datetime

from nodes.models import Node

Node.objects.create(device_id = 'CCF0023', rssi_data = -78, distance = 5, timestamp = datetime.datetime.now(), node_id = 'South Corridor', confidence = 2, location_x = 21, location_y = -22, origin_x = 0, origin_y = 0)

Node.objects.all()


Note: To format a datetime object from the database (always stored as UTC) into a proper timezone-relevant Unix measurement of time in milliseconds, do this:


from nodes.models import Node

from django.utils.dateformat import format

from django.utils.timezone import get_current_timezone

node = Node.objects.all()[0]

timestamp = node.timestamp

timestamp = timestamp.replace(tzinfo=get_current_timezone())

timestamp = int(format(timestamp, "U"))*1000



Should all have gone well, you should receive no errors.

The django-admin is setup.  If you go to http://localhost:8000/admin/ you can manage database objects.

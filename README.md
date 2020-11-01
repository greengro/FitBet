Hey guys.

To make sure we are all using the same packages we are using pipenv. 
It is quite simple to use and is quite common.

You will need to install python and pipenv which I suggest looking up since it will vary by OS.
You will also need to install the tools for postgres which will also vary.
For ubuntu I did: ```sudo apt install python-dev libpq-dev postgresql postgresql-contrib```

To get it started, in the same directory as the Pipfile and Pipfile.lock
run ```pipenv install```. 
This command creates the environment and installs all the packages and the correct python version.
If you are using pycharm, it will take care of all of this for you.
Next, you can do ```pipenv shell``` to enter into this python environment.
To install packages you must use ```pipenv install packagename``` in order for pipenv to keep track of your changes.

I also created a docker container for the postgres db to standardize since it is more tricky.
Follow the instructions to install docker (you should probably install docker desktop if available).
You will also have to run ``` docker volume create pgdata``` for only a single time. 
This is used to make the changes to the database persistent. (https://stackoverflow.com/questions/41637505/how-to-persist-data-in-a-dockerized-postgres-database-using-volumes)

To use the container, run ```docker-compose up -d```. Now you can interact with the data using Django and at localhost:5555 and both the username and password is postgres.
I would also recommend installing pgadmin4 (provides gui).

Useful and Common Django Commands:

python manage.py runserver - runs the web server so you can view the site

python manage.py shell - allows you to view your database tables and the data within them

python manage.py startapp app_name - creates a new app in your project called app_name

To save edits to the database (creating or editing a database table), always run (in this order):
1. python manage.py makemigrations
2. python manage.py migrate





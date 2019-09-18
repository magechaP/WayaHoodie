# WayaHoodie
###### Description
Wayahoodie is an application for members living in the same neighborhood to 
interact with each other resulting into a friendly neighbourhood experience.
###### Author
WayaHoodie
###### Published
The application is published at the heroku site, https://wayanghoodie.herokuapp.com/
* 18/9/2019

### Application Functionality
* The app allows users to sihn up or sign in if they have an account already
* The user may select to choose a Neighbouhood or create their own neighborhood
* Once a is in a hood they can view posts and notifications by other members of the hood
* A user can also participate in posting  notifications
* A user can view info such as  the health departmnt of the hood or the police department
* Members of a hood can interact with their businesses
### Installations

1. Clone the repository with:
`git clone https://github.com/magechaP/wayahoodie`
2. You will then have to unzip the zipped format of the repo.

3. You will need to install all dependencies by running this command:
* First make sure your requirements.txt file is like this:

`config==0.3.9`
`dj-database-url==0.5.0`
`Django==1.11`
`django-bootstrap3==10.0.1`
`django-heroku==0.3.1`
`gunicorn==19.9.0`
`Pillow==5.2.0`
`psycopg2==2.7.5`
`python-decouple==3.1`
`pytz==2018.5`
`whitenoise==4.0`
`pip install -r requirements.txt`
`django-mathfilters==0.4.0`
`pytz==2019.1`
`djangorestframework==3.9.4`

* If not use this command:
`pip freeze > requirements.txt`
* i would advice you to use python version 3.6 +
* Do not try to use django version above 1.11, it will result to errors due to compatibility
* For this cause, i recommend python 3.6 but specify `python3.6.8` in your `runtime.txt` file when deploying to heroku

4. To use the application locally you wil have to create a postgress database
follow these steps to get the app up and running:
* in your psql:
`CREATE DATABASE wayahoodie;`
* in your terminal migrate with:
`python3.6 manage.py migrate`
* Make a `.env` file to store your environmental variables

* serve the application with:
`python manage.py runserver`
* open the app on localhost:8000

## Technologies used
1. Django 1.11
2. Python3.6
3. HTML and Css
4. Production deployment to heroku
## License
This project is licensed under the MIT Open Source license, (c) Peter Magecha
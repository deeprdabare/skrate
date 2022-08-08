# skrate

The application is hosted on **Heroku**.
DB is hosted on Mongo **Atlas**.

Python version : 3.10.0

**DEPLOYMENT READY :**
The app is deployment ready. Also it is deployed on Heroku server, the url is mentioned below.
To checkout and deploye :

Checkout the code in an environment on local :
- pip install requirements.py
- source ../{ENV_DIRECTORY}/bin/activate
- cd ticketingSystem
- python manage.py runserver 8081

**Following are the endpoints, to use:**

https://ticketingappskrate.herokuapp.com/users/new

Sample input JSON : (No Authorization)

{
    "username" : "Admin1",
    "role" : "admin"
}

OR

{
    "username" : "Emp1",
    "role" : "employee"
}

Response :

{"token"  :   "ahkdbfksbfks"}

**NOTE  : Save this token for further use !!**


https://ticketingappskrate.herokuapp.com/tickets/all (Anyone)

https://ticketingappskrate.herokuapp.com/tickets/new (Only Admin)

Sample input JSON : 
NOTE  : assignedTo is the "id" of user

{
    "title" : "First ticket",
    "description" : "Describe temp",
    "assignedTo" : 4
}

Response :

{
    "title": "First ticket",
    "description": "Describe temp",
    "assignedTo": 4,
    "status": "open",
    "priority": "low"
}

https://ticketingappskrate.herokuapp.com/tickets/?status=open (User and Admin)

https://ticketingappskrate.herokuapp.com/tickets/?priority=low (User and Admin)

https://ticketingappskrate.herokuapp.com/tickets/markAsClosed (Admin and ticket user)

Sample input JSON : 
{
    "ticketid":1
}

Response :

{
    "title": "First ticket",
    "description": "Describe temp",
    "assignedTo": 4,
    "status": "close",
    "priority": "low"
}

https://ticketingappskrate.herokuapp.com/tickets/delete   (Admin)

Sample input JSON : 
{
    "ticketid":1
}

Response :

{
    "message": "Ticket deleted"
}


**Additional end points for testing purpose:**

https://ticketingappskrate.herokuapp.com/ping
https://ticketingappskrate.herokuapp.com/users/all

**URLs**:

**Application URL** : https://ticketingappskrate.herokuapp.com/

**LOG File URL**    : https://dashboard.heroku.com/apps/ticketingappskrate/logs

**Demo video URL**  : https://drive.google.com/file/d/1Im42kXLWjIQkXFBI4gaFTP7WUFfAXSUq/view?usp=sharing

**POSTMAN collection**  : https://www.postman.com/research-technologist-99045294/workspace/skrate-calibre/collection/19639060-7435a8bc-6711-4496-bb07-89913ea0887a?action=share&creator=19639060

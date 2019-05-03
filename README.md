# Generic Data Model
This is a project that makes it possible for clients to create their own tables and fields and also store data in these tables. It is a generic data model developed in using Django framework 

## Approach
One model called **DataTable** holds all created tables, another model called **DataField** holds all fields and has a many-to-one relationship with the DataTable so a table can have multiple fields. Field types are either numbers, dates, text or enum (which is an option) and then the Field Options are comma separated options 

> Example if the field name is *sex* options would be *Male, Female*. 

**DataContent** model holds all the data as text in the content column and has a many-to-one relationship with the DataTable and DataField. In order to keep track of inserted rows so that created content can have a link and can be treated as one group of information I made the **DataRow** model that has a one-to-many relationship with the DataContent. 
The ERD diagram of the models is shown below
<img src="https://github.com/emmanuel-nike/django-generic-datamodel/blob/master/ERD.png" />

## Tech/Frameworks Used
**Backend**
* Django v2.2, APIs were developed using Django rest framework and Class Based Views

**Frontend**
* VueJs v2 
User Authentication was done using JWT Token Authentication

## How to Use?
The project uses an sqlite database and the compiled version of the VueJS application is included in this repository. To run this localy, make sure you have the requirements for Django v2.2 and have django rest framework installed. Just run the command below on your local machine

> python manage.py runserver

and visit your http://localhost:8000 to view project. You will be taken to a login screen the test username/password is **bctest**/**bctest123**. The compiled VueJs app is already included but if you feel the need to recompile the VueJs app, navigate to the vue-dashboard directory and run

> npm run build

this is configured to send the index.html to the template directory in britecore/template and also send javascript, css and image files to static directory
# Generic Data Model
This is a project that makes it possible for clients to create their own tables and fields and also store data in these tables. It is a generic data model developed in using Django framework 

## Aim
The aim of this project is to create a platform where users can create their own tables or risk types (for insurers) and attach as many fields as they like with different field types such as text, numbers, dates or even options. Then they can populate it with as much data as they can gather. These tables will be implemented in a generic manner and will not have to be manually inputed and migrated into the database.

## Approach
One model called **DataTable** holds all created tables, another model called **DataField** holds all fields and has a many-to-one relationship with the DataTable so a table can have multiple fields. Field types are either numbers, dates, text or enum (which is an option) and then the Field Options are comma separated options 

> Example if the field name is *sex* options would be *Male, Female*. 

**DataContent** model holds all the data as text in the content column and has a many-to-one relationship with the DataTable and DataField. In order to keep track of inserted rows so that created content can have a link and can be treated as one group of information I made the **DataRow** model that has a one-to-many relationship with the DataContent. 
The ERD diagram of the models is shown below
<img src="https://github.com/emmanuel-nike/django-generic-datamodel/blob/master/ERD.png" />

## Tech/Frameworks Used
**Backend**
* Django v2.2, APIs were developed using Django REST framework and Class Based Views

**Frontend**
* VueJs v2 
User Authentication was done using JWT Token Authentication

## Features
* Login and Authentication (Registration not implemented)
* Create tables
* Add as many fields to any created table
* Edit tables to add more fields or change fields information
* Select a table and add data to the table. A modal with a form pops up that shows input types depending on the field types of the table
* Delete a table entry
* Delete a table

## Deployment
This application is deployed on heroku for demo purposes. Note that you will be taken to a login screen and the test username/password is **bctest**/**bctest123**.

[Application demo](https://generic-datamodel.herokuapp.com)

> The test user *bctest* is a superuser therefore you can also visit [App Django Admin](https://generic-datamodel.herokuapp.com/admin/) and login to the django admin to view models and even create more users since the registration is not implemented yet.

For deployment to heroku the following files were added

* Procfile: For pointing to the django application i.e. britecore.wsgi
* requirements.txt: For indicating dependencies and requirements to be installed i.e. django, djangorestframework, etc
* runtime.txt: To state the python version this application will run on

## How to Use?
The project uses an sqlite database and the compiled version of the VueJS application is included in this repository. To run this locally, make sure you have the requirements for Django v2.2 and have django rest framework installed. Just run the command below on your local machine

> python manage.py runserver

and visit your http://localhost:8000 to view project. You will be taken to a login screen the test username/password is **bctest**/**bctest123**. The compiled VueJs app is already included but if you feel the need to recompile the VueJs app, navigate to the vue-dashboard directory and run

> npm run build

this is configured to send the index.html to the template directory in britecore/template and also send javascript, css and image files to static directory


## Credits
* Creative Tim [Argon Dashboard](https://www.creative-tim.com/product/argon-dashboard)

## License

MIT License

Copyright (c) 2019 [emmanuel-nike](https://www.github.com/emmanuel-nike)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
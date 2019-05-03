# Generic Data Model
This is a project that makes it possible for clients to create their own tables and fields and also store data in these tables. It is a generic data model developed in using Django framework 

## Approach
One model called DataTable holds all created tables, another model called DataField holds all fields and has a many-to-one relationship with the DataTable so a table can have multiple fields. Field types are either numbers, dates, text or enum (which is an option) and then the Field Options are comma separated options example if the field name is sex options woule be Male, Female. DataContent model holds all the data as text in the content column and has a many-to-one relationship with the DataTable and DataField. In order to keep track of inserted rows so that created content can have a link and can be treated as one group of information I made the DataRow model that has a one-to-many relationship with the DataContent. 
The ERD diagram of the models is shown below
<img src="https://github.com/emmanuel-nike/django-generic-datamodel/blob/master/ERD.png" />

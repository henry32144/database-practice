Database query practice app
===============================
This app is for user to practice database select operation. When I was taking the course about database, sometimes I dont really understand what is the result of the example in the book. 

So I built this website, and also practice SQlite3 and Python flask as the backend.

This app's database is the same as the example on [Fundamentals of Database Systems, Global Edition](http://catalogue.pearsoned.co.uk/educator/product/Fundamentals-of-Database-Systems-Global-Edition/9781292097619.page), table csv files is in the table folder. 

Query examples are according to the [Fundamentals of Database Systems, Global Edition](http://catalogue.pearsoned.co.uk/educator/product/Fundamentals-of-Database-Systems-Global-Edition/9781292097619.page), By test, there are some examples are not work, but doesnt affect the app.

Built With
===============================
FrontEnd:
*  [Bootstrap4](https://v4-alpha.getbootstrap.com/)
*  [Bootstrap-html-template](https://startbootstrap.com/template-overviews/bare/)
*  [Jquery](https://jquery.com/)
*  [Jquery-ui(autoCompelete)](https://jqueryui.com/)
*  [Jinja2](http://jinja.pocoo.org/docs/2.10/)

BackEnd:
*  [Python3.6](https://www.python.org/downloads/)
*  [Flask](http://flask.pocoo.org/)

Database:
*  [SQlite3](https://www.sqlite.org/)

How to Use
==============================
Open cmd, and install flask if you dont have.

and cd to the root folder of this app 

type 

python app.py

and you can run a local server 


Attention
==============================
For some reason, this app restrict user on database operator, which can only use SELECT, the others would be filtered(such as CREATE, DELETE...).

And the database's data is not refer to anyone in the world, all data and table in database are from the [Fundamentals of Database Systems, Global Edition](http://catalogue.pearsoned.co.uk/educator/product/Fundamentals-of-Database-Systems-Global-Edition/9781292097619.page), I dont own these data.
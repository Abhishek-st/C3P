# C3P

<h2>Inatallation SetUp</h2>
<ul>
    <li> First Intall MongoDb in your system</li>
    <li> Then Install MongoDb Compass in your system</li>
    <li> Now create virtual environment in python  " python3 -m venv env"</li>
    <li> Activate Env "source env/bin/activate"</li>
    <li> Now run "pip install -r requirements.txt"</li>
    <li> Now open MongoDb Compass and create database named "C3P"</li>
    <li> Type command "python manage.py makemigrations"</li>
    <li> Type command "python manage.py migrate"</li>
    <li> Type command "python manage.py runserver"</li>
    <li> Now you are ready for testing the API"</li>
</ul>
<br><br>

<h2>EndPoints</h2>
<ul>
    <li>GET  http://127.0.0.1:8000/api/getPizzas/   :  To get all pizzas</li>
    <li>POST http://127.0.0.1:8000/api/createPizzas/   :  To create a new pizza <br> 
    <center>    {
        "name": "Margerita",
        "types": "Regular",
        "size": "medium",
        "toppings": [
            "capsicum",
            "cheese"
        ]
    }</center></li>
    <li>PATCH Or DELETE  http://127.0.0.1:8000/api/updateOrDelete/str:pk/'   :  To delete or update the record if delete then only pass pizza name in place of "str:pk", for patch you are supposed to pass data as well</li>
    <li>POST  http://127.0.0.1:8000/api/filterPizza/  :  To filter and then get the pizzas,  you can either pass size or type or both in the data</li><br>
    <li>POST  http://127.0.0.1:8000/api/addSize/   :  To add size</li>
    <li>POST  http://127.0.0.1:8000/api/addTopping/   :  To add Toppings</li>
    <li>GET  http://127.0.0.1:8000/api/getSize/   :  To get size</li>
    <li>GET  http://127.0.0.1:8000/api/getTopping/   :  To get toppings</li>
</ul>
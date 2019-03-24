#!/usr/local/bin/python3

## simple demo script for showing how to connect to an sqlite DB
# from Python, and run a simple SQL query

# import the python library for SQLite
import sqlite3
import cgi

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'fav_restaurant'
# and assign it's value to a local variable called fav_restaurant_name
fav_restaurant_name = form.getvalue('neighborhood')

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database.
db_cursor = db_connection.cursor()

#run a query depending on which button in the html form was selected. 
if fav_restaurant_name == 'Kreuzberg':
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 1;")
elif fav_restaurant_name == "Wedding":
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 2;")
elif fav_restaurant_name == 'Neuköln':
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 3")
else:
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 4")

# store the result in a local variable.
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

print("""
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Here are the Re$taurants</h1>
    <p>Here are the Restaurants in '{}'</p>
    {} 
  </body>
</html>
""".format(fav_restaurant_name, list_restaurants))

# print("list_restaurants contents:")
# print(list_restaurants)

db_connection.close()

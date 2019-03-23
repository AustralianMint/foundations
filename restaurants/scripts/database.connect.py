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
fav_restaurant_name = form.getvalue('fav_restaurant')

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database.
db_cursor = db_connection.cursor()

# run a first query
db_cursor.execute("SELECT NAME FROM restaurants")

# store the result in a local variable.
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

# print("Content-Type: text/html")
print("""
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Here are the Re$taurants</h1>
    {}
    <p>I also like {}</p> 
  </body>
</html>
""".format(list_restaurants, fav_restaurant_name))

# print("list_restaurants contents:")
# print(list_restaurants)

db_connection.close()

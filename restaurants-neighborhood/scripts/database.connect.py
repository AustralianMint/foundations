#!/usr/local/bin/python3

## simple demo script for showing how to connect to an sqlite DB
# from Python, and run a simple SQL query

# import the python library for SQLite
import sqlite3
import cgi

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'fav_restaurant'
# and assign it's value to a local variable called selected_neighborhood
selected_neighborhood = form.getvalue('neighborhood')

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database.
db_cursor = db_connection.cursor()

#run a query depending on which button in the html form was selected. 
if selected_neighborhood == 'Kreuzberg':
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 1;")
elif selected_neighborhood == "Wedding":
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 2;")
elif selected_neighborhood == 'Neuköln':
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 3")
elif selected_neighborhood == 'Spandau':
  db_cursor.execute("SELECT NAME FROM restaurants WHERE NEIGHBORHOOD_ID = 4")
else:
  print("No field was selected")
  

# store the result in a local variable.
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

def showRestaurants():
  print("<table border='1'")
  print("<tr>")
  print("<th>Restaurant name</th>")
  print("</tr>")
  for each in list_restaurants:
    print("<tr>")
    print("<td>{}</td>".format(each))
    print("</tr>")

print("""
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1 style="color:orange;">Here are the Restaurants</h1>
    <p>Restaurants in '{}'</p> 
  </body>
</html>
""".format(selected_neighborhood))

showRestaurants()

db_connection.close()

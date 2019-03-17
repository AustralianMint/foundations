#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import csv

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
v_name = form.getvalue('fav-color')

with open('colors.csv', mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if row["realName"] != v_name:
            print(row["realName"])
            line_count += 1
        else:
            print("""
            <html>
            <style>
                p {
                color: red;
                }
            </style>
            <body>
            <p>
            Thanks! %s is indeed a color
            </p>
            </body>
            </html>
            """ % v_name)

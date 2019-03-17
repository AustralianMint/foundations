#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
v_name = form.getvalue('fav-color')

# send an html response.
print("""
<html>
<style>
    h1 {
    font-family: Trebuchet MS;
    color: white;
    background-color: black;
    }
    p {
    color: red;
    }
</style>
<body>
<h1>Hurraaahh!!</h1>
<p>Awesome, I like %s as well</p>
</body>
</html>
""" % v_name)

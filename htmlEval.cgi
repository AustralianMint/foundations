#!/usr/bin/python
import cgi

formData = cgi.fieldStorage()
fav_color = formData.getvalue(fav-color)
print("""
<html>
    <body>
        <p>This is some html i'd like to be printed</p>
    </body>
</html>
""")

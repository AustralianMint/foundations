import requests
import json

r_with_data = requests.get('https://dog.ceo/api/breeds/image/random')
converted_json_data = json.loads(r_with_data.text)

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
""")

print(converted_json_data['message'])
print("This is the retrieved json data:\n{} ".format(converted_json_data))
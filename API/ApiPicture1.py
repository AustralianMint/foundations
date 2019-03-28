##cURL the dog api to provide a random picture.
##turn json response into python dict.
#access linked img in dict

import requests
import json

r_with_data = requests.get('https://dog.ceo/api/breeds/image/random')
converted_json_data = json.loads(r_with_data.text)

#new variable with html 
#referencing json data -> .format it into <img src="{}"
html = ("""
<!DOCTYPE html>
<html>
<body>
<p>Here is a picture of a dog, fak...</p>
<img src="{}">
</body>
</html>
""".format(converted_json_data['message']))

with open('dogHtmlFile.html', 'w') as file:
    file.write(html)

# print(converted_json_data['message'])
# print("This is the retrieved json data:\n{} ".format(converted_json_data))
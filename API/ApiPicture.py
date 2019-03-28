#!usr/bin/python3

jsonInfo = {
    "alt": "The Python environmental protection agency wants to seal it in a cement chamber, with pictorial messages to future civilizations warning them about the danger of using sudo to install random Python packages.",
    "day": "30",
    "img": "https://imgs.xkcd.com/comics/python_environment.png",
    "link": "",
    "month": "4",
    "news": "",
    "num": 1987,
    "safe_title": "Python Environment",
    "title": "Python Environment",
    "transcript": "",
    "year": "2018"
}

html = ""

for values in jsonInfo.values():
    if 'http' in str(values):
        html_link = values

print(http_link)

print("""
<html>
<body>
<p>
Thanks,
</p>
<img src="{}">
</body>
</html>
""".format(html_link))



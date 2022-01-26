#!/usr/bin/python3
import cgi
import requests
import webbrowser

form = cgi.FieldStorage()
url = "https://contact-api-dev-3sujih4x4a-uc.a.run.app/email"
email = form.getvalue("email")
user_id = form.getvalue("userId")

#req = requests.get("https://contact-api-dev-3sujih4x4a-uc.a.run.app/email/?email=JaneJones1643166115.029112%40fake.com")
req = requests.get(url, params={"email": email})

print("Content-type: text/html\n")
print(req.text)
print(req.status_code)


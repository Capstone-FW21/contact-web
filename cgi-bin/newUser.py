#!/usr/bin/python3
import cgi
import requests
form = cgi.FieldStorage()
email = form.getvalue("email")
json_data = {"email": email}
req = requests.post("http://34.134.138.81/", json=json_data)
#req = requests.get("http://34.134.138.81/?email=JaneJones1643166115.029112%40fake.com")

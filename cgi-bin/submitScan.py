#!/usr/bin/python3
import cgi
import requests

form = cgi.FieldStorage()
email = form.getvalue("email")
room_id = form.getvalue("roomNumber")

json_data = {"scan": {"email": email, "room_id": room_id}}
req = requests.post("https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data", json=json_data)
print("Content-type: text/html\n")
print(req.status_code)
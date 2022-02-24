#!/usr/bin/python3
import cgi
import requests

form = cgi.FieldStorage()
room_id = form.getvalue("roomNumber")
email = form.getvalue("email")
x_value = form.getvalue("seat_xPos")
y_value = form.getvalue("seat_yPos")

json_data = {"scan": {"type": "PERSONAL", "email": email, "scanned_id": room_id, "xcoord": x_value, "ycoord": y_value}}
req = requests.post("https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data", json=json_data)
if req.status_code == requests.codes.ok+1:
    url = "http://34.134.138.81/scanSuccess.html"
    new_page = requests.post(url)
    print("Content-type: text/html\n")
    print(req.status_code)
    print(new_page.text)
else:
    url = "http://34.134.138.81/scanFail.html"
    new_page = requests.post(url)
    print("Content-type: text/html\n")
    print(req.status_code)
    print(req.text)
    print(new_page.text)

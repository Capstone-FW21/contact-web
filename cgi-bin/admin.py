#!/usr/bin/python3
import cgi
import requests
form = cgi.FieldStorage()
query = form.getfirst("stats", "").lower()
# room_id = form.getvalue("roomNumber")
# json_data = {"scan": {"type": "ROOM", "email": email, "scanned_id": room_id}}
req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/stats/?stat_type=", json=query)
# if req.status_code == requests.codes.ok+1:
#     url = "http://34.134.138.81/scanSuccess.html"
#     new_page = requests.post(url)
#     print("Content-type: text/html\n")
#     print(req.status_code)
#     print(new_page.text)
# else:
#     url = "http://34.134.138.81/scanFail.html"
#     new_page = requests.post(url)
#     print("Content-type: text/html\n")
#     print(req.status_code)
#     print(req.text)
#     print(new_page.text)

print(req.json())

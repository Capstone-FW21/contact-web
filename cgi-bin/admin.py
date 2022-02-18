#!/usr/bin/python3
import cgi
import requests
form = cgi.FieldStorage()
query = form.getvalue("stats")
page = """
<html class="bkAnchor">
<head>
  <title>Capstone 2021: Contact Tracing System (Prototype)</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" type="text/css" href="../../index.css" />
</head>
<body>
  <form class="forms" action="/" method="POST">
    <div id="logo">
      <img id="icon" src="https://www.logolynx.com/images/logolynx/82/82590470b83eb44be69e8598efa845a7.png" />
      <p id="title">PSU Contact Tracing</p>
    </div>
"""
if(query == "records"):
    limit = form.getvalue("limit")
    req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/records/?limit=" + limit)
    data = req.json()
    print("Content-type: text/html\n")
    #print("Data: ", data)
    page = page + """<p>Return to <a href="../admin/admin.html">Admin</a></p><fieldset>
    <legend>RECORDS</legend>"""
    for item in data:
        studentid = item[0]
        email = item[1]
        date = item[2]
        roomid = item[3]
        x = item[4]
        y = item[5]
        page = page + """<p class="results"> 
        Student ID: """ + str(studentid) + """<br>
        Email: """ + str(email) + """<br>
        Date/ Time: """ + str(date) + """<br>
        Room ID: """ + str(roomid) + """<br>
        X Coord: """ + str(x) + """<br>
        Y Coord: """ + str(y) + """
        </p><br>"""
else:
    req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/stats/?stat_type=" + query)
    print("Content-type: text/html\n")
    data = req.json()
    page = page + """<p>Return to <a href="../admin/admin.html">Admin</a></p><fieldset>
    <legend>""" + query.upper() + """</legend>"""
    for item in data:
        if(query == "students"):
            email = str(item[0])
            name = str(item[1])
            studentid = str(item[2])
            page = page + """<p class="results">
            Email: """ + email + """<br>
            Name: """ + name + """<br>
            Student ID: """ + studentid + """
            </p><br>"""
        elif(query == "buildings"):
            name = str(item[0])
            rooms = str(item[1])
            scans = str(item[2])
            students = str(item[3])
            page = page + """<p class="results">
            Building Name: """ + name + """<br>
            Number of Rooms: """ + rooms + """<br>
            Number of Scans: """ + scans + """<br>
            Number of Unique Students: """ + students + """
            </p><br>"""
        elif(query == "rooms"):
            roomid = str(item[0])
            cap = str(item[1])
            name = str(item[2])
            ratio = str(item[3])
            page = page + """<p class="results">
            Room ID: """ + roomid + """<br>
            Capacity: """ + cap + """<br>
            Building Name: """ + name + """<br>
            Room Ratio: """ + ratio + """<br>
            </p><br>"""
page = page + """</fieldset>
</form>
</body>"""
print(page)
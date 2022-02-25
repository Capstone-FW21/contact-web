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
elif(query == "students"):
    req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/stats/?stat_type=" + query)
    print("Content-type: text/html\n")
    data = req.json()
    page = page + """<fieldset>
    <legend>""" + query.upper() + """</legend>"""
    for item in data:
        email = str(item[0])
        name = str(item[1])
        studentid = str(item[2])
        page = page + """<p class="results">
        Email: """ + email + """<br>
        Name: """ + name + """<br>
        Student ID: """ + studentid + """ 
        </p><br>"""
elif(query == "buildings"):
    req = ''
    if(form.getvalue("building")):
        b_id = form.getvalue("building")
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/buildings?building_id=" + b_id)
    else:
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/buildings")
    print("Content-type: text/html\n")
    data = req.json()
    page = page + """<fieldset>
    <legend>""" + query.upper() + """</legend>"""
    if(req):
        for item in data:
            for att, val in item.items():
                #print("Item1: ", att)
                #print("Item2: ", val)
                page = page + """<p class="results">
                """ + str(att) + """: """ + str(val) + """\n"""
            page = page + """</p><br>"""
elif(query == "rooms"):
    req = ''
    if(form.getvalue("roomd")):
        r_id = form.getvalue("roomid")
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/rooms?room_id=" + r_id)
    else:
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/rooms")
    print("Content-type: text/html\n")
    page = page + """<fieldset>
    <legend>""" + query.upper() + """</legend>"""
    for item in data:
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
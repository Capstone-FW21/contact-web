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
elif(query == "breakouts"):
    email = form.getvalue("email")
    date = form.getvalue("date")
    req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/breakout?email=" + email + "&date=" + date)
    print("Content-type: text/html\n")
    data = req.json()
    page = page + """<fieldset>
    <legend>Breakouts</legend>"""
    #print(data)
    if(req.status_code == 400):
        page = page + """<h4 class="successText">
        """ + str(data["detail"]) + """</h4>"""
    else:
        page = page + """<h4 class="successText">
        Students that may have been in contact with:<br> """ + email + """</h4>"""
        if(data):
            for item in data:
                userid = str(item[0])
                email = str(item[1])
                date = str(item[2])
                room = str(item[3])
                xcoord = str(item[4])
                ycoord = str(item[5])
                page = page + """<p class="results">
                User Id: """ + userid + """<br>
                Email: """ + email + """<br>
                Date: """ + date + """<br>
                Room: """ + room + """<br>
                X Coord: """ + xcoord + """<br>
                Y Coord: """ + ycoord + """<br>
                </p><br>"""
        else:
            page = page + """<h4 class="successText">
            """ + str(data) + """ </h4> """
elif(query == "buildings"):
    print("Content-type: text/html\n")
    page = page + """<fieldset>
    <legend>""" + query.upper() + """</legend>"""
    req = ''
    if(form.getvalue("building")):
        b_id = form.getvalue("building")
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/buildings?building_id=" + b_id)
        data = req.json()
        #print(data)
        building = str(data["Building"])
        rooms = str(data["Number_of_Rooms"])
        numscans = str(data["Number_of_Scans"])
        unique = str(data["Unique_Students"])
        scans = str(data["Scans_per_Day"])
        page = page + """<p class="results">
        Building: """ + building + """<br>
        Number of Rooms: """ + rooms + """<br>
        Number of Scans: """ + numscans + """<br>
        Number of Unique Students: """ + unique + """<br>
        Scans per Day: """ + scans + """<br>
        </p><br>"""
    else:
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/buildings")
        data = req.json()
        if(req):
            for item in data:
                for att, val in item.items():
                    #print("Item1: ", att)
                    #print("Item2: ", val)
                    page = page + """<p class="results">
                    """ + str(att) + """: """ + str(val) + """\n"""
                page = page + """</p><br>"""
        else:
            page = page + """<p class="results">
            """ + req.text + """ or can't find building id
            </p><br>"""
elif(query == "rooms"):
    print("Content-type: text/html\n")
    page = page + """<fieldset>
    <legend>""" + query.upper() + """</legend>"""
    req = ''
    if(form.getvalue("roomid")):
        r_id = form.getvalue("roomid")
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/rooms?room_id=" + r_id)
        data = req.json()
        #print(data)
        roomid = str(data["Room"])
        cap = str(data["Capacity"])
        name = str(data["Building_Name"])
        ratio = str(data["Aspect_Ratio"])
        unique = str(data["Unique_Students"])
        scans = str(data["Scans_per_Day"])
        page = page + """<p class="results">
        Room ID: """ + roomid + """<br>
        Capacity: """ + cap + """<br>
        Building Name: """ + name + """<br>
        Room Ratio: """ + ratio + """<br>
        Number of Unique Students: """ + unique + """<br>
        Scans per Day: """ + scans + """<br>
        </p><br>"""
    else:
        req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/rooms")
        data = req.json()
        if(req):
            for item in data:
                for att, val in item.items():
                    #print("Item1: ", att)
                    #print("Item2: ", val)
                    page = page + """<p class="results">
                    """ + str(att) + """: """ + str(val) + """\n"""
                page = page + """</p><br>"""
        else:
            page = page + """<p class="results">
            """ + req.text + """ or can't find room id
            </p><br>"""
elif(query == "userRecords"):
    print("Content-type: text/html\n")
    page = page + """<fieldset>
    <legend>User Records</legend>"""
    email = form.getvalue("email")
    limit = form.getvalue("limit")
    req = requests.get("https://contact-api-internal-dev-3sujih4x4a-uc.a.run.app/user_records?email=" + email + "&limit=" + limit)
    data = req.json()
    #print(data)
    if(req.status_code == 400):
        page = page + """<h4 class="successText">
        """ + str(data["detail"]) + """</h4>"""
    else:
        if(data):
            for item in data:
                userid = str(item[0])
                email = str(item[1])
                date = str(item[2])
                room = str(item[3])
                xcoord = str(item[4])
                ycoord = str(item[5])
                page = page + """<p class="results">
                User Id: """ + userid + """<br>
                Email: """ + email + """<br>
                Date: """ + date + """<br>
                Room: """ + room + """<br>
                X Coord: """ + xcoord + """<br>
                Y Coord: """ + ycoord + """<br>
                </p><br>"""
        else:
            page = page + """<h4 class="successText">
            """ + str(data) + """ </h4> """
page = page + """</fieldset>
</form>
</body>"""
print(page)
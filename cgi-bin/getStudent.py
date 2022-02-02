#!/usr/bin/python3
import cgi
import requests

req = requests.get("https://contact-api-dev-3sujih4x4a-uc.a.run.app/student")
data = req.json()

personal_id = data["personal_id"]
lname = data["last_name"]
fname = data["first_name"]
email = data["email"]
print("Content Type: text/html\n\n")
print(req.json())

registrationPage = """
<html class="bkAnchor">

<head>
  <title>Capstone 2021: Contact Tracing System (Prototype)</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" type="text/css" href="../css/index.css" />
</head>

<body>
  <form id="scanData" action="" method="POST">
    <div id="logo">
      <img id="icon" src="https://www.logolynx.com/images/logolynx/82/82590470b83eb44be69e8598efa845a7.png" />
      <p id="title">PSU Contact Tracing</p>
    </div>

    <fieldset>
      <legend>Register New User</legend>
      <label for="student_id">Student ID:</label>
      <input type="text" id="student_id" name="student_id" value=""" + personal_id + """ /><br />
      <label for="fname">First Name:</label>
      <input type="text" id="fname" name="fname" value="""+ fname + """ /><br />
      <label for="lname">Last Name:</label>
      <input type="text" id="lname" name="lname" value="""+ lname + """ /><br />
      <label for="email">Email:</label>
      <input type="text" id="email" name="email" value=""" + email + """ /><br />
      <p id="submitButton">
        <label for="sendData">Press submit to create a new user</label>
        <br /><br />
        <input type="submit" id="submitScanData" value="Submit" />
      </p>
      <p>
        <a href="index.html">Return to Scan Entry</a>
      </p>
    </fieldset>
  </form>

  <!-- begin javascript section -->
  <!-- end javascript section -->
</body>

</html>
"""

print(registrationPage)




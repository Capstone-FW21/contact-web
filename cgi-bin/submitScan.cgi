#!/usr/bin/python3
import cgi
import requests

form = cgi.FieldStorage()
room_id = form.getvalue("roomNumber")
email = form.getvalue("email")

page = """
<html class="bkAnchor">

<head>
    <title>Capstone 2021: Contact Tracing System (Prototype)</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="../../index.css" />
    <div id="logo">
        <img id="icon" src="https://www.logolynx.com/images/logolynx/82/82590470b83eb44be69e8598efa845a7.png" />
        <p id="title">PSU Contact Tracing</p>
    </div>
</head>

<body>
"""

req = requests.get("https://contact-api-dev-3sujih4x4a-uc.a.run.app/room?room_id=" + room_id)
data = req.json()
print("Content-type: text/html\n")
ratio = data.get("aspect_ratio")
rwidth = int(ratio[0])
rheight = int(ratio[1])
rsize = rwidth + rheight
width_scale = rwidth / rsize
height_scale = rheight / rsize
#fixme: requires pillow installed in python
#i already happen to know the img dims, therefore the magic numbers below
#base_image = PIL.Images.open("classroom-layout.jpg")
#img_width, img_height = base_image.size
img_width = 400
img_height = 400
new_width = img_width * width_scale
new_height = img_width * height_scale

#add some scaling in case the room dims are small or strange
new_width = new_width * 1.5
new_height = new_height * 1.5

page = page + """
    <form id="seatSelector" action="../cgi-bin/transmitData.cgi" method="POST">
    <fieldset>
	<legend>Room Scan</legend>
          <label for="email">Email:</label>
          <p><strong>""" + email + """</strong></p>
          <label for="email">Room Number:</label>
          <p><strong>""" + room_id + """</strong></p>
	  <p style="text-align: center;"><canvas id="seatChooser" width=" """
page = page + str(new_width + 20)
page = page + """px" height=" """
page = page + str(new_height + 20)
page = page + """px"></canvas></p>
	  <p id="seatPositionDisplay">
		<label for="seatPosition">Please select an approximate position of your seat:</label><br />
		<label for="seatXValue">X:</label>
		<input type="number" id="seat_xPos" name="seatXPosition" value=0 /><br />
		<label for="seatyValue">Y:</label>
		<input type="number" id="seat_yPos" name="seatYPosition" value=0 />
	</p>
        <p id="submitButton">
          <label for="sendData">Press Submit to send your scan to our database:</label>
          <br /><br />
          <input type="submit" id="submitScanData" value="Submit"/>
	</p>
    </fieldset>
    </form>
        <script type="text/javascript" language="javascript">
                <!--
		var boxWidth = """
page = page + str(new_width)
page = page + """ ;
                var boxHeight = """
page = page + str(new_height)
page = page + """ ;
		var boxPadding = 10;
                var gridSize = 25;

		var roomMap = document.getElementById("seatChooser");
		var ctx = roomMap.getContext("2d");
		function getCursorPosition(roomMap, event) {
			const rect = roomMap.getBoundingClientRect();
			const x = event.clientX - rect.left;
			const y = event.clientY - rect.top;
			document.getElementById("seat_xPos").value = Math.round(x);
			document.getElementById("seat_yPos").value = Math.round(y);
		}
		roomMap.addEventListener('mousedown', function(e) {
			getCursorPosition(roomMap, e);
		})
		function drawBoard() {
			for (var x = 0; x <= boxWidth; x+= gridSize) {
				ctx.moveTo(0.5 + x + boxPadding, boxPadding);
				ctx.lineTo(0.5 + x + boxPadding, boxHeight + boxPadding);
			}
			for (var x = 0; x <= boxHeight; x+= gridSize) {
				ctx.moveTo(boxPadding, 0.5 + x + boxPadding);
				ctx.lineTo(boxWidth + boxPadding, 0.5 + x + boxPadding);
			}
			ctx.strokeStyle = "grey";
			ctx.stroke();
		}
		drawBoard();
                //-->
	</script>
</body>
</html>
"""

print(page)


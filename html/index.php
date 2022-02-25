<!DOCTYPE html>
<html class="bkAnchor">
  <head>
    <title>Capstone 2021: Contact Tracing System (Prototype)</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../index.css" />
    <script type="text/javascript">
      function writeCookie() {
        emailVal = escape(document.getElementById("email").value) + ";";
        document.cookie = "email=" + emailVal;
      }
      function readCookie() {
        var key, value, i, email;
        var cookieArray = document.cookie.split(":");
        for (i = 0; i < cookieArray.length; i++) {
          key = cookieArray[i].substr(0, cookieArray[i].indexOf("="));
          value = cookieArray[i].substr(cookieArray[i].indexOf("=") + 1);
          key = key.replace(/^\s+|\s+$/g, "");
          if (key == "email") {
            //alert("Email is " + value);
            email = value;
          }
        }
        if (email) {
          document.getElementById("email").value = email;
        }
      }
      function toggleSeatChooser() {
		var chooser = document.getElementById('scanData');
		var oldButton = document.getElementById('openSeatChooser');
		chooser.style.display = "inline";
		oldButton.style.display = "none";
      }
    </script>
  </head>
  <body>
        <form id="scanData" action="../cgi-bin/submitScan.cgi" method="POST" onsubmit="writeCookie()">
	<!-- page logo -->
	<div id="logo">
        <img id ="icon" src="https://www.logolynx.com/images/logolynx/82/82590470b83eb44be69e8598efa845a7.png">
        <p id="title">PSU Contact Tracing</p>
	</div>
	<!-- call php methods to read the cookie -->
	<?php
	$email = $_GET['email'];
	$room_id = $_GET['room_id'];
	?>
	<!-- put together the input form -->
	<fieldset>
	<legend>Room Scan</legend>
          <label for="email">Email:</label>
          <input type="text" id="email" name="email" value='<?php echo $email; ?>' /><br /><br />
          <label for="roomNumber">Room Number:</label>
	  <input type="text" id="room_id" name="roomNumber" value='<?php echo $room_id; ?>'/><br />
        <p id="submitButton">
          <label for="sendData">Press Submit to send your scan to our database:</label>
          <br /><br />
          <input type="submit" id="submitScanData" value="Submit"/>
        </p>

        <p>Need an account? <a href="registration.html">Sign Up</a></p>
	<p><a href="admin/admin.html">Admin</a></p>
	</fieldset>
	</form>
    <script>
		window.onload = readCookie();
    </script>
  </body>
</html>
<!--
	<script type="text/javascript">
		var boxWidth = 400;
		var boxHeight = 400;
		var boxPadding = 10;

		var roomMap = document.getElementById("seatChooser");
		var ctx = roomMap.getContext("2d");
		function getCursorPosition(roomMap, event) {
			const rect = roomMap.getBoundingClientRect();
			const x = event.clientX - rect.left;
			const y = event.clientY - rect.top;
			//console.log("x: " + x + "y: " + y);
			//document.getElementById("clickLocation").innerHTML = "x: " + x + ", y: " + y;
			document.getElementById("seat_xPos").value = Math.round(x);
			document.getElementById("seat_yPos").value = Math.round(y);
		}
		roomMap.addEventListener('mousedown', function(e) {
			getCursorPosition(roomMap, e);
		})
		function drawBoard() {
			for (var x = 0; x <= boxWidth; x+= 40) {
				ctx.moveTo(0.5 + x + boxPadding, boxPadding);
				ctx.lineTo(0.5 + x + boxPadding, boxHeight + boxPadding);
			}
			for (var x = 0; x <= boxHeight; x+= 40) {
				ctx.moveTo(boxPadding, 0.5 + x + boxPadding);
				ctx.lineTo(boxWidth + boxPadding, 0.5 + x + boxPadding);
			}
			ctx.strokeStyle = "black";
			ctx.stroke();
		}
		drawBoard();
	</script>
-->

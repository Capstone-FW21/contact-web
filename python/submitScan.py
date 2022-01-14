#!/usr/bin/python

# import requests
# url = 'https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data/'

# x = requests.post(url, {{email : test}, {room_id : testRoom}})

# print x.text


#!/usr/bin/python

import requests
import cgi

#this should get the data from the html form
form = cgi.FieldStorage()
email = form.getvalue('email') #'JamesFord1642124200.629766@fake.com' #
room_id = form.getvalue('roomNumber#!/usr/bin') #'room_1' #

#This seemed to work when I uncomment the values from the above email 
# and room id rather than trying to get the form data. 
url = 'https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data?email='+ email + '&room_id=' + room_id

#This url works with the paramaters placed in it already
#x = requests.post('https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data?email=JamesFord1642124200.629766%40fake.com&room_id=room_1')

x = requests.post(url)

print(x.json())



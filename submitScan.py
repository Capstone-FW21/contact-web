#!/usr/bin/python

import requests
url = 'https://contact-api-dev-3sujih4x4a-uc.a.run.app/record_data/'

x = requests.post(url, {{email : test}, {room_id : testRoom}})

print x.text

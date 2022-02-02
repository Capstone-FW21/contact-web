#!/usr/bin/python3
import cgi
import requests
form = cgi.FieldStorage()
email = form.getvalue("email")
print("Content-type: text/html\n\n")
url = "http://34.134.138.81/"
s = requests.Session()
cookie_obj= requests.cookies.create_cookie(domain=url, name='email', value=email)
s.cookies.set_cookie(cookie_obj)
r = requests.get(url, s.cookies)
print(r.text)
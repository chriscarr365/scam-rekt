import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url1 = 'http://www.orlenok-kmw.ru/verifynow/Hotmail%20Office%20New%20Code%20(3)/next.php'
url2 = 'http://www.orlenok-kmw.ru/verifynow/Hotmail%20Office%20New%20Code%20(3)/next2.php'
names = json.loads(open('C:/Users/ChrisC/Desktop/names2.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@dundee.ac.uk'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url1, allow_redirects=False, data={
        'userid': username,
        'pass': password,
        'formimage1.x': 99,
        'formimage1.y': 15,
        })
    requests.post(url2, allow_redirects=False, data={    
        'userid': username,
        'pass': password,
        'formimage1.x': 0,
        'formimage1.y': 0,
        })
    print ("sending username {0} and password {1}".format(username, password))
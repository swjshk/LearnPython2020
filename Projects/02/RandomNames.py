import os
import json
import random
import string

namefile = 'names.json'
names = json.loads(open(namefile).read())
random.seed(os.urandom(1024))

def generate_user():
    username = '{}.{}{}@gmail.com'.format(
        random.choice(names),random.choice(names),random.choice(string.digits))

    password = ''.join(random.choice(string.digits + string.ascii_letters) 
        for i in range(random.choice([5,6,7,8,9,10])))
    
    print('user = {:30}\npassword = {:20}\n'.format(username,password))

for i in range(10):
    generate_user()

### learn
# random
# json.loads()
# random.choice()ß
# string
# regex

# https://www.freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries/

# dictionary list
users = {
    "Julian_Id": {
        "username": "Julian",
        "email": "julian@gmail.com",
        "password": "qwertyu",
        "bio": "Some guy from the internet"
    },
    "Clarissa_Id": {
        "username": "Clarissa",
        "email": "clarissa@icloud.com",
        "password": "2qwertyu",
        "bio": "Sweet potato is life"
    }
}

my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

'''for item in my_dict:
    print(item)
    print(type(item)) '''

'''
for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print(key, value)'''

'''for k in users.keys():
    print(k)'''

'''for v in users.values(): 
    print(v)'''

"""for key, val in users.items():
    #print(key)
    #print(val)
    for n in val.items():
        print(n[1])"""

for item in users.items(): 
    #print(item[0])
    #print(item[1])
    if item[0] == 'Clarissa_Id':
        print('Welcome '+item[0])
        print(item[1])
    else:
        print("Sorry "+item[0])
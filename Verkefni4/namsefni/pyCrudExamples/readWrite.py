# https://www.freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries/

my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 2025,
    "Subjects": ["OS", "CN", "DBMS"]
}
# Read
print(my_dict)
print(my_dict['Name']) # item in list

# Write
my_dict['College'] = 'NSEC' # new list item
print(my_dict) 

# Update
my_dict['Name'] = 'Ólafur Ragnarsson' # overwrite 
another_dict = {'Branch': 'IT'}
my_dict.update(another_dict) # merge 2 dictionaries
print(my_dict)

# Delete
remove = my_dict.pop('Roll') 
print(my_dict)
del my_dict['Name'] 
print(my_dict)
my_dict.clear()
print(my_dict)



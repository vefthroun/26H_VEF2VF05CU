print('daemi 1')

foo = [1, 0.2, "bar"]
for i in foo:
    print(type(i))

print('daemi 2')

class MyClass:
    ...

def myfunc():
    ...

myint = 777
mystr = "Hello"
myobj = MyClass()

mylst = [
   MyClass, myfunc, myint, mystr, myobj
] 

# Nice one-liner
print(*map(type, mylst), sep="\n")

#https://stackoverflow.com/questions/35028272/how-to-print-types-within-a-list

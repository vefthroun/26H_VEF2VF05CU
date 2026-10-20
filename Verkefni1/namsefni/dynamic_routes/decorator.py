'''A Python decorator is a powerful and flexible tool that allows you to 
modify the behavior of a function or a method without changing its actual 
code. Decorators are often used to add functionality to existing code in a 
clean and readable way.'''

def jólaskraut(func):
    def umbúðir():
        #"Something is happening before the function is called."
        print(1+1, 'jólaseríur')
        func()
        #"Something is happening after the function is called."
        print(4*4, 'jólakúlur og jólastjarna')
    return umbúðir

'''Decorators are widely used in Python for various purposes, 
such as logging, access control, memoization, and more. 
They help keep your code DRY (Don't Repeat Yourself) and enhance readability.'''

@jólaskraut
def hóhóhó():
    print("Hér er jólatré")
    
hóhóhó()

''' Run file
In VSC Run `Command+K+S` to open keyboard shortcuts.
Then type `Python: Run Python File in Terminal`. Select it.
You can then type whatever key binding you want to use to run your code.
'''

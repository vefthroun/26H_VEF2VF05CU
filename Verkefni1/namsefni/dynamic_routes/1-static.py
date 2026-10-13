# 1. Imports
from flask import Flask, render_template
"""
The render_template() function invokes the Jinja template engine that comes bundled with the Flask framework. 
Jinja substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.
HTML special characters are escaped automatically to prevent XSS attacks.
"""

# 2. App Initialization
# The __name__ variable is a special Python variable. It gets the value "__main__"
# when the script is executed directly. When the script is imported as a module,
# __name__ gets the module's name. Flask uses this to know where to look for
# resources like templates and static files.

app = Flask(__name__)

# 3. Decorators and View Functions
# A decorator in Python is a function that takes another function and extends
# its behavior without explicitly modifying it. In Flask, @app.route() is a
# decorator that tells the application which URL should trigger our function.

# This decorator binds the URL "/" (the root of our site) to the index() function.
@app.route('/')
def index():
    """This is a view function. It's responsible for generating a response
    for a web request. Here, it renders the 'template1.html' template."""
    return render_template("template1.html")

# This decorator binds the URL "/about" to the about() function.
@app.route('/about')
def about():
    #This is another view function. It renders the 'about.html' template.
    return render_template('about.html')

# 4. Main entry point
# The following block of code will only run if the script is executed directly
# (e.g., by running `python 1-static.py` in the terminal). 
    
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

# app.run() starts the built-in Flask development server.
# debug=True, enables debug mode, which provides helpful error messages
# use_reloader=True, automatically reloads the server when you make changes to the code.
# NEVER use debug=True in a production environment.
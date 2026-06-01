from flask import Flask
# escapes characters so it is safe to use in HTML, https://pypi.org/project/MarkupSafe/
from markupsafe import escape 
app = Flask(__name__)

"""
Hægt er að búa til URL sem eru dýnamísk (ekki harðkóðuð).
https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules

Dynamic Routes & Variable Rules
You can use filters to be more specific.

    string: (default) accepts any text without a slash
    int:    accepts positive integers
    float:  accepts positive floating point values
    path:   like string but also accepts slashes
    uuid:   accepts UUID strings
"""
# Basic static route
@app.route('/')
def index():
 return "This is a basic flask application"

# Hægt er að nota færibreytur (parameters) til að búa til dynamic route 
# Skilar það sem þú skrifa í URL t.d. /product/cookie
@app.route('/product/<name>')
def demo1(name):   # name færibreytan inniheldur streng  (sjáfgefið gildi)
   return "The product is %s" % (name) # The product is cookie
                                       # string formatting: https://www.learnpython.org/en/String_Formatting

# Route with multiple parameters 
@app.route('/create/<first_name>/<last_name>')
def create(first_name, last_name):    
  return 'Hello ' + first_name + ',' + last_name

# Notum filterinn int: til að leyfa bara heiltölur t.d /post/3 (þ.e. ekki bókstafi og sértákn)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(type(post_id))          # <class 'int'>
    return 'Post: %d' % post_id   # Post: 3

# Dynamically generate article URLs based on the publication date.
# dæmi: http://127.0.0.1:5000/2020/3/Covid
@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    #... Logic goes here
    return "%d, %d, %s" % (year, month, title) # tuple

# Flask allows you to create a URL route that matches any path by using the special path:variable_name converter in your URL rule. 
# This will match any path after /path/, and pass it as a string to your view function.
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}' # escape() is used to escape characters so it is safe to use in HTML (cross-site scripting attacks) 


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

                                    

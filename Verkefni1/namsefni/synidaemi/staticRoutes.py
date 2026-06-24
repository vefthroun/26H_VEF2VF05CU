from flask import Flask
app = Flask(__name__)

# You can bind more than one route to a single callback (Chaining Decorators)
@app.route('/')
@app.route('/index')
def index():
    return "Halló Heimur! index"

# dæmi um undirsíðu
@app.route('/demo1')
def demo1():
    # skilum textastreng í vafra
    return "Halló Heimur! demo1"

# blöndum saman html elementum og texta í streng sem við skilum.
@app.route('/demo2')
def demo2():
    return "<h1>Halló Heimur! demo2</h1>"

# Við getum skilað html vefsíðu sem streng
@app.route('/demo3')
def demo3():
    # breyta sem geymir html í strengjaformi
    html = '''
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
          <h1>Halló</h1>
          <a href="/sida1">Tengill</a>  <!-- tengill á routið (undirsíða) /sida1 -->
    </body>
    '''
    return html


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  


   

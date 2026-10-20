from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'author': {'username': 'John', 'title':'Student'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan', 'title':'Teacher'},
            'body': 'The Avengers movie was so cool!'
        }
        ,
        {
            'author': {'username': 'Trump', 'title':'Idiot'},
            'body': 'I´m GROOT!'
        }
    ]
    #print(posts)
    return render_template('for-if.html', posts=posts)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
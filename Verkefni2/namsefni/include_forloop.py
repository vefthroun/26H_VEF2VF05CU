from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ,
        {
            'author': {'username': 'Trump'},
            'body': 'I´m GROOT!'
        }
    ]
    return render_template('include_forloop.html', posts=posts)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
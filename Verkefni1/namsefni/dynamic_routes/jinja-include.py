from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    user = {
       'name': 'Gunnar',
       'school': 'Tækniskólinn'
    }
    return render_template('include.html', title='Tölvubraut', user=user)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    

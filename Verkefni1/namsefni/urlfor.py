
from flask import Flask, url_for
app = Flask(__name__)


# Í stað þess að harðkóða tengla í html t.d. <a href="/sida1"> Tengill á síðu 1</a>
# Þá getum við notað url_for fall fyrir url bindingu (auðveldara að uppfæra tengla)
# https://youtu.be/Ofy_jRHE3no?list=PLXmMXHVSvS-CoYS177-UvMAQYRfL3fBtX


@app.route('/')
@app.route('/heimaerbest')
def home():
    return "<a href=" + url_for('sida2') + ">Link To Gunnar</a>"    # dæmi um html hlekk: 

@app.route('/sida1/') # ath! /.../
def sida1():
    # vísar í routið sem geymir home fallið og skilar því + seinna urlinu
    return url_for("home")  # /

@app.route('/sida2')
def sida2():
    # vísar í routið sem geymir sida3 fallið og skilar því urli ásamt færibreytu
    return url_for("sida3", name="Gunnar") 
 
# /sida3 birtist ekki nema í gegnum /sida2
@app.route('/sida3/<string:name>')
def sida3(name):
    return  name # birtir /sida3/Gunnar

# Vísun í static möppu sem inniheldur CSS skrá
# í jinja2 template: url_for('static', filename='style.css') 

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

from flask import Flask
app = Flask(__name__)
from tinydb import TinyDB
db = TinyDB('data/db.json', indent = 2, encoding='utf-8', ensure_ascii=False)
# indent = 2 makes the json file more human readable
# encoding and ensure_ascii makes it possible to use special characters
# db.purge() # Uncomment to clear the database

@app.route('/')
def index():
    return "<a href='/read'>Lesa</a> | <a href='/create'>Skrifa</a> | <a href='/update'>Uppfæra</a> | <a href='/delete'>Eyða</a>"

@app.route('/read')
def read():
    for i in db:
        print(i)
    return "Allir í db - skoðið terminal"

@app.route('/create')
def create():
    plus1 = len(db) +1
    print(plus1)
    db.insert({
            "uid":plus1,
            "name":"Jóhannes",
            "email":"joh@nnes",
            "bio":"Skírn er mín sérgrein"})
    for i in db:
        print(i)
    return "Nýr notandi er í db.json - skoðið terminal"

@app.route('/update')
def update():
    from tinydb import Query
    user = Query()
    db.update({'name':'Jesú', 'email':'jes@ja', 'bio':'Töfrabrögð eru mín sérgrein, sumir kalla þau kraftaverk'}, user.uid == 1 )
    # db.update({ updated field: updated information }, stable field: information)
    for i in db:
        print(i)
    return "Notandi uppfærður í db - skoðið terminal"

@app.route('/delete')
def delete():
    from tinydb import Query
    dl = Query()
    db.remove(dl.uid == 2)
    # db.remove( Query() field regex )
    return "Notandi fjarlægður úr db - skoðið terminal"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True) 
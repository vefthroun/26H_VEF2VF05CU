from flask import Flask
# Escape-virknin afkóðar stafi svo öruggt sé að birta þá í HTML.
# https://pypi.org/project/MarkupSafe/
from markupsafe import escape

app = Flask(__name__)

"""
Hægt er að búa til dýnamískar vefslóðir (URL) í stað þess að harðkóða þær.
https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules

Hægt er að nota síur til að afmarka hvaða gildi slóðin tekur við:

    string: (sjálfgefið) tekur við texta sem inniheldur ekki skástrik
    int:    tekur við jákvæðum heiltölum
    float:  tekur við jákvæðum kommutölum
    path:   virkar eins og string en tekur einnig við skástrikum
    uuid:   tekur við UUID-auðkennum
"""

# Einföld, föst leið
@app.route('/')
def index():
    return "This is a basic flask application"

# Hægt er að nota færibreytur til að búa til dýnamíska leið.
# Færibreytan name fær gildið úr vefslóðinni, t.d. /product/kaka.
@app.route('/product/<name>')
def show_product(name):
    return f"The product is {name}"

# Leið með fleiri en einni færibreytu
@app.route('/create/<first_name>/<last_name>')
def create(first_name, last_name):
    return f"Hello {first_name},{last_name}"

# int-sían leyfir aðeins heiltölur, t.d. /post/3, en ekki bókstafi eða sértákn.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(type(post_id))  # <class 'int'>
    return f"Post: {post_id}"

# Býr til vefslóðir greina út frá útgáfuári, mánuði og titli.
# Dæmi: http://127.0.0.1:5000/2020/3/Covid
@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    return f"{year}, {month}, {title}"

# path-sían leyfir skástrik í slóðinni og sendir allt eftir /path/ sem streng
# til fallsins.
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # escape() sér til þess að sértákn séu örugg þegar þau eru birt í HTML.
    return f"Subpath {escape(subpath)}"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

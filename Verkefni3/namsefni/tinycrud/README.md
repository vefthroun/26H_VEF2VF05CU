# TinyDB 

Í stuttu máli: Ef þú þarft einfaldan  API gagnagrunn sem virkar án mikillar fyrirhafnar þá gæti TinyDB verið rétti kosturinn fyrir þig.

* https://tinydb.readthedocs.io/en/latest/
* https://www.tutorialspoint.com/tinydb/index.htm

---

Til að búa til þessa spjallsíðu þurfum við að tengja saman **Flask** fyrir vefumgjörðina, **sessions** fyrir örugga aðgangsstýringu og **TinyDB** sem JSON gagnagrunn.

Hér er hvernig þú getur útfært þetta verkefni:

### 1. Uppsetning og Gagnagrunnur (TinyDB)
TinyDB geymir gögnin í hreinni JSON skrá (`db.json`). Til að tryggja að hún sé óaðgengileg öðrum en appinu, er hún geymd í rótarmöppu verkefnisins en **ekki** í `static` möppunni, því Flask þjónar aðeins skrám úr `static` beint til notenda.

```python
from flask import Flask, render_template, request, session, redirect, url_for, flash
from tinydb import TinyDB, Query

app = Flask(__name__)
app.secret_key = 'mjog-leyndur-lykill' # Nauðsynlegt fyrir session
db = TinyDB('db.json')
posts_table = db.table('posts')
users_table = db.table('users')
User = Query()
Post = Query()
```

### 2. Forsíða (index.html) - Birta alla pósta
Á forsíðunni notarðu `db.all()` til að sækja alla pósta úr TinyDB og birta þá. Samkvæmt kröfunni er enginn breytingahnappur hér, heldur aðeins lestur.

```python
@app.route('/')
def index():
    all_posts = posts_table.all() # Sækir alla pósta
    return render_template('index.html', posts=all_posts)
```

### 3. Session Aðgangsstýring og Innskráning
Til að verja prófílsíðuna notarðu `session` til að geyma `user_id` og `role` (notandi eða vefstjóri).

```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    # Hér myndir þú leita að notanda í users_table
    user = users_table.get(User.username == username)
    if user:
        session['user_id'] = user.doc_id # doc_id er sjálfkrafa ID hjá TinyDB
        session['role'] = user.get('role', 'user')
        return redirect(url_for('profile'))
    return "Innskráning mistókst", 401
```

### 4. Prófílsíða (profile.html) - CRUD fyrir eigin pósta
Hér geta notendur búið til nýja pósta með `insert()`, uppfært þá með `update()` eða eytt þeim með `remove()`. Lykilatriðið er að sía póstana þannig að notandi sjái aðeins sína eigin.

```python
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    
    # Sækja aðeins pósta þessa notanda
    user_posts = posts_table.search(Post.author_id == session['user_id'])
    return render_template('profile.html', posts=user_posts)

@app.route('/post/new', methods=['POST'])
def new_post():
    if 'user_id' in session:
        posts_table.insert({
            'author_id': session['user_id'],
            'content': request.form.get('content')
        })
    return redirect(url_for('profile'))
```

### 5. Aðgangur Vefstjóra (Admin)
Vefstjórinn hefur sérstaka rás þar sem athugað er hvort `session['role'] == 'admin'`. Hann getur eytt hvaða pósti eða notanda sem er.

```python
@app.route('/admin/delete_post/<int:post_id>')
def admin_delete_post(post_id):
    if session.get('role') == 'admin':
        posts_table.remove(doc_ids=[post_id])
        flash("Pósti eytt af vefstjóra")
    return redirect(url_for('index'))

@app.route('/admin/delete_user/<int:user_id>')
def admin_delete_user(user_id):
    if session.get('role') == 'admin':
        users_table.remove(doc_ids=[user_id])
        # Einnig mætti eyða öllum póstum notandans
        posts_table.remove(Post.author_id == user_id)
    return redirect(url_for('index'))
```

### Öryggisatriði úr heimildum:
*   **HTML Escaping:** Flask og Jinja2 sjá sjálfkrafa um að hreinsa (escape) það sem notendur skrifa í póstana sína til að koma í veg fyrir sprautuhótanir (injection attacks).
*   **Secret Key:** Mikilvægt er að hafa sterkan `secret_key` svo notendur geti ekki falsað session-kökurnar sínar og gefið sér admin-réttindi.
*   **TinyDB Query:** Notaðu `Query()` hlutinn frá TinyDB til að gera leitirnar öruggar og skýrar.

from flask import Flask
app = Flask(__name__)

globalGildi = ' og Jón Jónsson'
# breyta
@app.route('/demo1')
def demo1():
    data = "Gunnar"
    print(data)
    return  "<h1>Halló " + data + "!</h1>"

# tuple
@app.route('/demo2')
def demo2():
    data = ("Gunnar", "Daníel")
    print(data)
    return  "<h1>Halló " + data[0] + " og " + data[1] + "!</h1>"

# dictionary https://realpython.com/python-dicts/
@app.route('/demo3')
def demo3():
    data = {'username': 'Gunnar'}
    print(data)
    print(globalGildi)
    return  "<h1>Halló " + data['username'] + globalGildi + "!</h1>"
    # líka hægt að nota get aðferð, data.get('username')  skilar NONE en ekki villumeldingu ef það vantar gildi

# listi
@app.route('/demo4')
def demo4():
    data = ["Gunnar", "Daníel"]
    print(data) 
    return  "<h1>Halló " + data[0] +  " og " + data[1] + "!</h1>"  

# dictionary með lista
@app.route('/demo5')
def demo5():
    safn = {"users":["Gunnar", "Daníel","Guðmundur","Karl"]}
    print(safn["users"])  # listi
    return  "<h1>Halló " + safn["users"][2] + " og " + safn["users"][1] + "!</h1>" 

if __name__ == '__main__':
    # run, starts a built-in development server
    app.run(debug=True, use_reloader=True)  
    

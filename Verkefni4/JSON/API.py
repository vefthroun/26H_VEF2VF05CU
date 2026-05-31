from flask import Flask, render_template, json

import json
import urllib.request

# Fixing the SSL CERTIFICATE_VERIFY_FAILED Error
# Ef vesen með Mac: Applications Folder -> Python folder, and click on the Install Certificates.command file
import certifi # þarf að gera pip install certifi
import ssl           
certifi_context = ssl.create_default_context(cafile=certifi.where()) # muna að bæta svo við "context=certifi_context" í seinni param. í urllib.request

app = Flask(__name__)

# genres request þarf að vera globalt, sent í öll route
with urllib.request.urlopen("https://api.tvmaze.com/singlesearch/shows?q=iceguys", context=certifi_context) as url:  # vantar runu fyrir key
   data = json.loads(url.read())
   # data = json.loads(url.read().decode('utf-8'))

print(data['summary'])    # Action & Adventure
#print (json.dumps(data, indent=2))  # læsilegra

@app.route('/')
def genre():
    #return render_template('index.html', data=data)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

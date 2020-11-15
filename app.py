from flask import Flask,render_template,redirect,url_for,request,jsonify,flash
from requests import get
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        ip=request.form["ip"]
        url = 'https://ipapi.co/{}/json/'
        loc = get(url.format(ip))
        res = loc.json()
        if 'country' not in res:
            flash("This Ip address doesn't exist.")
        return render_template("index.html", data=res)


    else:
        url='http://bot.whatismyipaddress.com/'
        loc=get(url)
        data = loc.content
        ip = data.decode("utf-8")
        url = 'https://ipapi.co/{}/json/'
        loc = get(url.format(ip))
        res = loc.json()
        return render_template("index.html", data=res)

if __name__ == '__main__':
    app.run(debug=True)

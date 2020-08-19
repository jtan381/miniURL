from flask import Flask, redirect, render_template, request
import os
from url_shortener import URL_Shortener

url_shortener = URL_Shortener()

# Create Flask app.
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def insertURL():
    formData =  request.form
    miniURL = url_shortener.shortener_url(formData)
    return """<div><p> orginalURL: {} </p> <p> miniURL: http://jj-miniurl.tools/{} </p></div>""".format(formData['orginalURL'], miniURL)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if(short_url in url_shortener.url2miniurl.values()):
        orginalLink = list(url_shortener.url2miniurl.keys())[list(
            url_shortener.url2miniurl.values()).index(short_url)]
        return redirect(orginalLink)
    else:
        return 'bad request!', 400



@app.route('/remove')
def removeURL():
    return ""


@app.route('/status')
def retriveURL():
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80")

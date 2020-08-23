#Flask framwork
from flask import Flask, redirect, render_template, request
from urllib.parse import urlparse
from url_shortener import URL_Shortener
import os

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
    return render_template("insert.html".format(miniURL), orginalURL = formData['orginalURL'], miniURL =miniURL)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    orginalLink = url_shortener.getOrginalURL(short_url)
    if(orginalLink):
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

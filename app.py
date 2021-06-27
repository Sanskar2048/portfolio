from flask import Flask, render_template, redirect
import json

with open('config.json', 'r', encoding="utf8") as c:
    para= json.load(c)
home_para= para["home"]
portfolio_para= para["portfolio"]

#portfolio
app = Flask(__name__)

theme="light dark"

@app.route('/')
def index():
    return render_template('index.html', home_para=home_para ,theme=theme)


@app.route('/contact')
def contact():
    return render_template('contact.html', theme=theme)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', portfolio_para=portfolio_para, theme=theme)

@app.route('/resume')
def resume():
    return render_template('resume.html',theme=theme)

@app.route('/theme')
def themechanger():
    global theme
    if theme == 'light':
        theme='light dark'
    else:
        theme='light'
    return redirect("/")

if __name__ == "__main__" :
    app.run(debug = True)
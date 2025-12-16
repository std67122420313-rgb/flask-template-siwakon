from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  #title = 'Home Page'
  return render_template('index.html' , title='My Home Page')

@app.route('/about')
def about():
  title = 'About Page'
  name = 'siwakon'
  email = 'std.67122420313@ubru.ac.th'
  mobile = '099-874-1883'
  age = 20
  return render_template('about.html',title=title, name=name,email=email, mobile=mobile,age=age)

@app.route('/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['ไก่ทอด','ชาบู','ข้าวผัด']
  return render_template('favorite_foods.html',title=title,foods=foods)


@app.route('/favorite/sport')
def favorite_sport():
  title = 'Favorite sport Page'
  sport = ['ฟุตบอล','แบดมินตัน','บาสเกสบอล']
  return render_template('favorite_foods.html',title=title,sport=sport)
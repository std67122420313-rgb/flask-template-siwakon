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
def favorite_sports():
  title = 'Favorite sport Page'
  sports = ['ฟุตบอล','แบดมินตัน','บาสเกสบอล']
  return render_template('favorite_sport.html',title=title, sports=sports)


@app.route('/favorite/movies')
def favorite_movies():
  title = 'Favorite movies Page'
  movies = ['ไอรอนแมน','มาสไรเดอร์','อุลตร้าแมน','อวาตาล','กังฟูแพนด้า']
  return render_template('favorite_movies.html',title=title, movies=movies)
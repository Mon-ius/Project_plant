from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/input_0')
def input_0():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input0.html')
@app.route('/input_1')
def input_1():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input1.html')
@app.route('/input_2')
def input_2():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input2.html')
@app.route('/input_3')
def input_3():
    if had_sigin():
        redirect_to(url_for('/login'))
    return render_template('input3.html')

if __name__ == '__main__':
  app.run('127.0.0.1', debug=True)
 
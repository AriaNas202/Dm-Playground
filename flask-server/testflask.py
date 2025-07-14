from flask import Flask, url_for, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello,buddy!"

@app.route('/nas')
def abc():
    return redirect(url_for('index'))

app.run(debug=True)


#notes
# pip install flask
#then he upgraded pip or whatever
#dont need to restart the server when you make changes, just change code and refresh page!
#can also do app.run(debug=True, port=8000) to choose flask server port

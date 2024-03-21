from flask import Flask
app=Flask(__name__)


@app.route('/')
def home():
     return '<h1>helloworld</h1>'

@app.route('/new')
def new():
     return '<h1>hai am new</h1>'
app.run()
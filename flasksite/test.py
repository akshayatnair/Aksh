from flask import Flask
new=Flask(__name__)

@new.route('/profile/<int:id>')

def profile(id):
    return '<h1> this profile is page %d </h1>' %id

new.run(debug=True)
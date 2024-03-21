from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)

@app.route('/books')
def books():
    books=[{'name': 'book1','author':'abc','cover':"https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-1-CRC.png"},
           {'name': 'book2','author':'abc2','cover':"https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-2-CRC.png"},
           {'name': 'book3','author':'abc3','cover':"https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png"}]
    return render_template('book.html',books=books)

app.run(debug=True)
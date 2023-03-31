from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/classes')
def classes():
    return render_template("classes.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/news')
def news():
    return render_template("news.html")

if __name__=='__main__':
    
    app.run(debug=True,port=3000)
    
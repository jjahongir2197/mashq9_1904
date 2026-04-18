from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return "<h1>Biz bilan bog'lanish: example@email.com</h1>"

if __name__ == '__main__':
    app.run(debug=True)

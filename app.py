from flask import Flask, render_template

app = Flask(__name__)

# হোমপেজ
@app.route('/')
def home():
    return render_template('index.html')

# টিপস পেজ
@app.route('/tips')
def tips():
    return render_template('tips.html')

# অ্যাবাউট পেজ
@app.route('/about')
def about():
    return render_template('about.html')


if __name__== "__main__":
    app.run(debug=True)

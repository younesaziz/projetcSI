from flask import Flask ,  render_template , request 


app = Flask(__name__)

app.secret_key = 'development key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/activity')
def activity():
    return render_template('activites.html')

if __name__ == "__main__":
    app.run( debug=True)
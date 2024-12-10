from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/companies')
def company():
    return render_template('companies.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/nonprofits')
def other():
    return render_template('nonprofits.html')

@app.route('/reserach')
def research():
    return render_template('research.html')

if __name__ == "__main__":
    app.run(debug=True)
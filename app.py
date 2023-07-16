from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/responsibilities')
def responsibilities():
    return render_template('responsibilities.html')

@app.route('/test_scores')
def test_scores():
    return render_template('test_scores.html')

@app.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)

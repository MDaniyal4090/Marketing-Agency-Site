from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#routes for service and contact pages
@app.route('/service')
def service():
    return render_template('services.html')

@app.route('/contact')  
def contact():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
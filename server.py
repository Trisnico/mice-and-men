from flask import Flask, render_templates, redirect, request, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_templates("index.html")

@app.route('/ninjas')
def ninjas():
    return render_templates("ninjas.html")

@app.route('/dojos/new', methods=['POST'])
def dojos():
    return render_templates("dojo.html")
    name = request.form('name')
    email = requst.form('email')
    return redirect('/')


app.run(debug=True)
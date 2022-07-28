from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Frisbee"
]

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=['post'])
def register():

    # validate name
    name = request.form.get('name')
    if not name:
        return render_template('error.html', message="Missing name")

    # validate submission
    sport = request.form.get('sport')
    if not sport:
        return render_template('error.html', message="Missing sport")
    
    if sport not in SPORTS:
        return render_template('error.html', message="Invalid sport")

    # Remember REGISTRANTS
    REGISTRANTS[name] = sport

    # confirm registration
    return redirect("/registration")    


@app.route('/registration')
def registeration():
    return render_template('registration.html', registrants = REGISTRANTS)
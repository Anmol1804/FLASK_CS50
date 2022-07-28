from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/greet", methods=["post"])
def greet():
    name = request.form.get('name', 'world')
    return render_template('greet.html', name=name)


# if __name__ == '__main__':
#     app.run(debug=True)


# import sys
# print(sys.path)
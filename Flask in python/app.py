from flask import Flask

'''

'''

###wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best flask course ! This should be an amazing course"


@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__ == '__main__':
    app.run(debug = True)

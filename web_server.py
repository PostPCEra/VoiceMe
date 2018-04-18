from flask import Flask, render_template, request

from logic import  check_age
# ----------------------------------------------------------------------
# having a separate 'app' folder and 'router.py' in 'app' folder is causing confusion, so have a single file
# ----------------------------------------------------------------------

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET'])
@app.route("/hi", methods=['GET'])
def display_form():
        text = render_template("hi.html")
        return text


@app.route("/hi", methods=['POST'])
def check_data():
        data = request.form  # this came from web browser in the form of dictionary
        name = data['name']
        age = int(data['age'])
        user_data = {'name': name, age: age}

        message = check_age(age)

        text = render_template("hi_response.html",
                               target="handle_hi",
                               name = name,
                               message = message)
        return text


@app.route("/bye")
def bye():
    text = render_template("bye.html")
    return text


if __name__ == "__main__":
    app.run(debug=True)   # this debug flag detects "code file chagnes & start Flash server automatically"
    #app.run()

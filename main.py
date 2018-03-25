from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot"><b>Rotate by:</b></label>
            <input id="rot" type="text" name="rot" />


            <textarea name="text"></textarea>



            <input type="submit" value="Submit Querey" /> 
        </form>
    </body>
</html>
"""

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    return "<h1>rot: " + rot + " text: " + text + "</h1>"



@app.route("/")
def index():
    return form

app.run()
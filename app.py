import os
from flask import Flask

app = Flask(__name__)
MESSAGE = os.environ.get("MESSAGE_ACCUEIL", "Bonjour depuis mon conteneur !")

@app.route("/")
def index():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

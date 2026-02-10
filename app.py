from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Deploy automático via Cloud Build funcionando!\n"

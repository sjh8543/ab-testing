from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Wellcome to AB testing engine"

@app.route("/admin")
def admin():
    return "It's admin URL"

@app.route("/collecting")
def collecting():
    return "It's collecting URL"

@app.route("/reporting")
def reporting():
    return "It's reporting URL"

@app.route("/routing")
def routing():
    return "It's routing URL"

if __name__ == "__main__":
    app.run()

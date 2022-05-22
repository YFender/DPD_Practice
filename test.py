import flask

app = flask.Flask(__name__)

@app.get("/")
def a():
    print(flask.request)
    return flask.redirect("/ddd")

@app.post("/")
def b():
    print(flask.request.json)
    return "dsa"

if __name__ == "__main__":
    app.run(port=5050)
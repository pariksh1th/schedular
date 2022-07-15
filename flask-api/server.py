from flask import Flask
from firestoreDB import testing

app = Flask(__name__)

@app.route("/data/<username>")
def hello_world(username):
    return testing(username)




if __name__ == '__main__':
    app.run(debug=True)
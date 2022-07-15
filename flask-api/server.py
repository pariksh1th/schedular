from flask import Flask
from firestoreDB import testing, sec_test, sec_names, test_user
from main import returnTable

app = Flask(__name__)

@app.route("/data/<username>")
def hello_world(username):
    return sec_test(username, sec_names)

@app.route("/data/tt")
def ttReturn():
    return sec_test(test_user, sec_names)






if __name__ == '__main__':
    app.run(debug=True)
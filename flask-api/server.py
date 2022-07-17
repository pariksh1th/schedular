
from flask import Flask
from firestoreDB import testing, sec_test, sec_names, test_user
# from main import returnTable
from main import returnTable

testOuput = {'CSE3A': [['EC105L', 'CS207tut', 'MA201tut', 'MA201L', 't'], ['EC105L', 'CS202l', 'MA201L', 'CS202L'], ['CS202L', 'CS202l', 'L', 'L'], ['CS201L', 'CS207l/EC105l', 'CS207L', 'CS202tut'], ['CS201L', 'CS207l/EC105l', 'CS207L', 'HS206L']], 'CSE3B': [['MA201L', 'MA201tut', 'CS202tut', 'CS202L', 't'], ['EC105L', 'CS207l/EC105l', 'EC105L', 'L'], ['MA201L', 'CS207l/EC105l', 'HS206L', 'L'], ['HS206L', 'CS202l', 'CS202L', 'L'], ['CS201L', 'CS202l', 'CS201L', 't']], 'CSE5A': [['CS304tut', 'CS304L', 'CS303L', 'ElectiveTut'], ['CS303l', 'ElectiveL', 'CS309L', 'CS303tut'], ['L', 'BasketL', 'CS309L', 'BasketTut'], ['CS309tut', 'BasketL', 'CS304L', 'L'], ['CS303l', 'ElectiveL', 'CS303L', 't']], 'CSE5B': [['CS303l', 'L', 'CS304L', 'ElectiveTut'], ['CS304tut', 'ElectiveL', 'CS303L', 'CS309tut'], ['CS304L', 'BasketL', 'CS303L', 'BasketTut'], ['CS303l', 'BasketL', 'CS309L', 'L'], ['t', 'ElectiveL', 'CS309L', 'CS303tut']]}



app = Flask(__name__)

@app.route("/data/<username>")
def hello_world(username):
    return sec_test(username, sec_names)

@app.route("/data/tt")
def ttReturn():
    return sec_test(test_user, sec_names)


@app.route("/data/model")
def model():
    return returnTable()





if __name__ == '__main__':
    app.run(debug=True)
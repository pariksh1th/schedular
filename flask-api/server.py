
from flask import Flask


# testOuput = {'CSE3A': [['EC105L', 'CS207tut', 'MA201tut', 'MA201L', 't'], ['EC105L', 'CS202l', 'MA201L', 'CS202L'], ['CS202L', 'CS202l', 'L', 'L'], ['CS201L', 'CS207l/EC105l', 'CS207L', 'CS202tut'], ['CS201L', 'CS207l/EC105l', 'CS207L', 'HS206L']], 'CSE3B': [['MA201L', 'MA201tut', 'CS202tut', 'CS202L', 't'], ['EC105L', 'CS207l/EC105l', 'EC105L', 'L'], ['MA201L', 'CS207l/EC105l', 'HS206L', 'L'], ['HS206L', 'CS202l', 'CS202L', 'L'], ['CS201L', 'CS202l', 'CS201L', 't']], 'CSE5A': [['CS304tut', 'CS304L', 'CS303L', 'ElectiveTut'], ['CS303l', 'ElectiveL', 'CS309L', 'CS303tut'], ['L', 'BasketL', 'CS309L', 'BasketTut'], ['CS309tut', 'BasketL', 'CS304L', 'L'], ['CS303l', 'ElectiveL', 'CS303L', 't']], 'CSE5B': [['CS303l', 'L', 'CS304L', 'ElectiveTut'], ['CS304tut', 'ElectiveL', 'CS303L', 'CS309tut'], ['CS304L', 'BasketL', 'CS303L', 'BasketTut'], ['CS303l', 'BasketL', 'CS309L', 'L'], ['t', 'ElectiveL', 'CS309L', 'CS303tut']]}

# test_user = '46N64qo1bxe7VrcXadiztikzFDs2'



app = Flask(__name__)
# test_user = ''

@app.route("/data/<username>")
def hello_world(username):
    from main import returnTable
    # global test_user
    # test_user = username
    # print(test_user)
    return returnTable(username)


# tes = {'Section 5': {'Uma': ['Clou', '2-1-0'], 'Vivekraj': ['Com gra', '2-1-0'], 'Sadhvi': ['Com desi', '2-1-0']},}






if __name__ == '__main__':
    app.run(debug=True)
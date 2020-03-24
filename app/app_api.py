from flask import request
from flask import Flask
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return '<p> Hello World</p>'

@app.route('/all/')
def all():
    r = requests.get('http://127.0.0.1:5000/graphql', json={'query': '{allMatches {edges {node{ matchName matchDate matchScore matchState }}}}'})

    return r.json()

@app.route('/date/', methods=['GET'])
def date():
    date = str(request.args.get('date'))
    #return date
    r = requests.get('http://127.0.0.1:5000/graphql', json={'query': 'query{findMatch(date:' + date + ') {id }}'})

    return r.json()

@app.route('/date/<name>')
def my_view_func(name):
    return name

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080,debug=True)


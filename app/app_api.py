import json
from datetime import datetime

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_API_HOST = "127.0.0.1"
DB_API_PORT = "5000"
DB_API = "http://{}:{}/graphql".format(DB_API_HOST,DB_API_PORT)

@app.route('/get_all')
def all():
     query = "{matchesList {edges {node{ matchName matchDate matchScore matchStatus }}}}"
     r = requests.get(DB_API, json={'query': query})
     response = json.loads(r.text)

     return jsonify(response)

@app.route('/filter_by_date', methods=['GET'])
def date():
     date = str(request.args.get('date'))
     query = 'query{findMatch(date: "' + date + '"){ matchId matchName matchDate matchScore matchStatus}}'
     r = requests.get(DB_API, json={'query': query})
     response = json.loads(r.text)
     return jsonify(response)

@app.route('/filter_by_id', methods=['GET'])
def id():
     match_id = str(request.args.get('id'))
     query = 'query{matches(matchId: "' + match_id + '"){ matchId matchName matchDate matchScore matchStatus}}'
     r = requests.get(DB_API, json={'query': query})
     response = json.loads(r.text)
     return jsonify(response)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080,debug=True)

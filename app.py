
from flask import Flask, request, jsonify
from marshmallow import ValidationError

from global_path import build_query
from model import QueryRequestValue



app = Flask(__name__)




@app.route('/perform_query', methods = ["POST"])
def perform_query():

    try:
        reque = QueryRequestValue().load(request.json)
    except ValidationError as e:
        return e.messages, 400


    result = None
    for query in reque['queries']:
        result = build_query(
            cmd = query['cmd'],
            param = query['value'],
            data = result,
        )



    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)



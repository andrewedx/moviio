from flask import Flask, jsonify, request
from flask_restful import Api, reqparse
import database

app = Flask(__name__)
api = Api(app)

post_args = reqparse.RequestParser()
post_args.add_argument("imdbID", type=str, required=True,
                       help="imdbID is required")
post_args.add_argument('Title', type=str, required=True,
                       help="Title is required")
post_args.add_argument('Year', type=str, required=True,
                       help="Year is required")
post_args.add_argument('Type', type=str, required=True,
                       help="Type is required")
post_args.add_argument('Poster', type=str, required=True,
                       help="Poster is required")

delete_args = reqparse.RequestParser()
delete_args.add_argument(
    "imdbID", type=str, required=True, help="imdbID is required")


@app.route('/')
def home():
    return jsonify({'message': 'The API is running'})


@app.route('/local', methods=['GET', 'POST', 'DELETE'])
def local():
    if request.method == 'GET':
        data = database.select()
        return jsonify(data)

    if request.method == 'POST':
        print("inserting data")
        args = post_args.parse_args()
        resp = database.insert(args)
        print(resp)
        return jsonify({"message": f"{resp}"})

    if request.method == 'DELETE':
        arg = request.args.get("id")

        if type(arg) != str or arg == "":
            return jsonify({"message": "Invalid ID Type"})
        resp = database.delete(arg)
        return jsonify({"message": f"{resp}"})


if __name__ == '__main__':
    app.run(debug=True)

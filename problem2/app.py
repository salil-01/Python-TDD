from flask import Flask, request, jsonify

weather_data = [{'San Francisco': {'temperature': 14, 'weather': 'Cloudy'}},
                {'New York': {'temperature': 20, 'weather': 'Sunny'}},
                {'Los Angeles': {'temperature': 24, 'weather': 'Sunny'}},
                {'Seattle': {'temperature': 10, 'weather': 'Rainy'}},
                {'Austin': {'temperature': 32, 'weather': 'Hot'}},
                ]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_data():
    return jsonify({"msg": weather_data}), 200


@app.route("/<string:city>", methods=["GET"])
def get_single_city(city):
    for item in weather_data:
        if city in item:
            return jsonify({"msg": item}), 200

    return jsonify({"msg": "City Not Found"}), 404


@app.route("/", methods=["POST"])
def create():
    data = request.json
    weather_data.append(data)
    return jsonify("City Added Successfully"), 200


@app.route("/<string:city>", methods=["PUT"])
def update(city):
    # print(city)
    data = request.json
    print(data)
    for items in weather_data:
        if city in items:
            weather_data.remove(items)
            weather_data.append(data)
            print(weather_data)
            return jsonify({"msg": "City Updated Successfully"}), 200

    return jsonify({"msg": "City Not Found"}), 404


@app.route("/<string:city>", methods=["DELETE"])
def delete(city):
    print(city)
    for items in weather_data:
        if city in items:
            weather_data.remove(items)
            return jsonify("City Deleted Successfully"), 200

    # print(weather_data)
    return jsonify({"msg": "City Not Found"}), 404

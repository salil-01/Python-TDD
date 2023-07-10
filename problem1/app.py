from flask import Flask, jsonify

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


# def create_app():
#     app = Flask(__name__)
#     @app.route("/weather/<string:city>")
#     def get_weather(city):
#         if(weather_data[city]):
#             return jsonify({"res":weather_data[city]}), 200
#         else:
#             return jsonify({"msg":"City Not Found"}), 404
#     if __name__ == "__main__":
#         app.run()

# create_app()
app = Flask(__name__)
@app.route("/")
def home_page():
    return jsonify({"msg":"Hi"})


@app.route("/weather/<string:city>")
def get_weather(city):
    if(weather_data[city]):
        return jsonify({"msg":weather_data[city]}), 200
    else:
        return jsonify({"msg":"City Not Found"}), 404
if __name__ == "__main__":
    app.run()
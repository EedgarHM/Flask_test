from flask import Flask
from get_distance import distance


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Moscow Ring Road </h1>\n" \
           "<p>For calculate distance beetwen two points go to /distance/coordinate_1,coordinate2" \
           " <br>eg. localhost/distance/37.842762,55.774558</p>"


if __name__ == "__main__":
    app.register_blueprint(distance)
    app.run(debug=True)

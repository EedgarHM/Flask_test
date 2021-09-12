# Operation Manual 

``` 
========================================
	author : Edgar Hernandez
========================================

########################################
#		Important Note                #
########################################
The coordinates must be entered in long, lat form to coincide with the coordinates of the road ring, since they come backwards. I also want to comment that the distance can vary a bit since when making the request to the Api, it returns one or more values, if the exact value of the coordinate is not found in the result of the api, the program will take the first or only existing element returned by the api
```



## Requeriments

* Flask
* Python 3.8+
* Geopy
* Pytest



## Main.py



```python
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
```






import flask
import requests
from constants import COORDINATES_RING_ROAD, API_KEY, MKAD_KM

from utils import coordinates_is_valid, calc_coordinates

distance = flask.Blueprint('distance', __name__)


@distance.route('/distance/<coord_b>', methods=['GET'])
def calc_distance(coord_b):
    """"
        Funcion que muestra información sobre el calculo de la distancia
        entre dos puntos
    """

    # Change data type from coords to compare with the new value and save in new list
    new_mkad_km = [f"{str(mk[1])},{str(mk[2])}" for mk in MKAD_KM]

    # Flag to check if the coordinate exists and is equal to the one that will bring the result of the api
    exist_coordinate = True

    # Check if the coordinates is valid
    if coordinates_is_valid(coord_b):

        # if the coordinate exists write in the file log
        if coord_b in new_mkad_km:
            with open('file_log.txt', mode='a') as log:
                log.write(f"Coordinates {coord_b} exists in MKAD File\n")
            return flask.jsonify({"InformationMessage": "Value Exists in MKAD"})

        else:

            # get api request passing apikey and coordinates
            result = requests.get(
                f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={coord_b}\
                    &format=json&lang=en_US&rspn=0&sco=longlat")

            # transform the result in json format
            result = result.json()

            # obtain all posibles result from the array featureMember
            items = result['response']['GeoObjectCollection']['featureMember']

            # The list of items is traversed and the coordinates of the first object are assigned
            for item in items:
                item_coordinate = item['GeoObject']['Point']['pos'].split(' ')

                # the coordinate is transformed and the comma is added to make the comparison
                new_coordinate_item = f"{item_coordinate[0]},{item_coordinate[1]}"

                # if the value is found, the element is returned in a new variable
                if new_coordinate_item == coord_b:
                    coor_point_b = new_coordinate_item
                else:
                    exist_coordinate = False  # If the value was not found, then change the flag

            # If the value was not found we assign it the only element that can have the result of the query
            if not exist_coordinate:
                distance_point_b = result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
                    'pos'].split(' ')

            # Change position from longitude and latitude
            coor_point_b = (distance_point_b[1], distance_point_b[0])
            distance_result = calc_coordinates(coordinate_a=COORDINATES_RING_ROAD, coordinate_b=coor_point_b)

            with open('file_log.txt', mode='a') as log:
                log.write(f"Distance Beetwen Ring Road and {coord_b} is approximate: {distance_result}\n")
            return flask.jsonify({"ApproximateDistance": distance_result, "Element": result['response']})
    else:
        error = 'Error, invalid input data, need be in format float, eg. 37.842762,55.774558 or be a valid coordinates'
        return flask.jsonify({"ErrorMessage": error})

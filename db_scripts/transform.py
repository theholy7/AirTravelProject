#! ~/miniconda3/bin/python


""" Transform.py has the objective of creating a new database with
Airline - flight - source airport (name and coordinates) - destinations airport (name and coordinates)"""


import sqlite3
from classes import *
import csv
from pprint import pprint
import math


# public static double distance(double lat1, double lat2, double lon1,
#         double lon2, double el1, double el2) {

#     final int R = 6371; // Radius of the earth

#     Double latDistance = Math.toRadians(lat2 - lat1);
#     Double lonDistance = Math.toRadians(lon2 - lon1);
#     Double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
#             + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
#             * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
#     Double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
#     double distance = R * c * 1000; // convert to meters

#     double height = el1 - el2;

#     distance = Math.pow(distance, 2) + Math.pow(height, 2);

#     return Math.sqrt(distance);
# }

def calulate_distance (source_lat, source_lon, source_alt, destination_lat, destination_lon, destination_alt):
    
    earth_radius = 6731 #earth radius

    lat_distance = math.radians(destination_lat - source_lat)
    lon_distance = math.radians(destination_lon - source_lon)

    aux_1 = math.sin(lat_distance / 2) * math.sin(lat_distance / 2) \
    + math.cos(math.radians(source_lat)) * math.cos(math.radians(destination_lat)) \
    * math.sin(lon_distance / 2) * math.sin(lon_distance / 2);

    aux_2 = 2 * math.atan2(math.sqrt(aux_1), math.sqrt(1-aux_1));

    distance = earth_radius * aux_2 * 1000 # Convert to meters

    height = source_alt - destination_alt

    distance = math.pow(distance, 2) + math.pow(height, 2)

    return math.sqrt( distance )






def main():
    try:
        #Try to connect
        print("Trying to connect to database...")

        conn = sqlite3.connect(r"../database/openflight.db")

        c = conn.cursor()

        print("Connection established!")


        c.execute( "CREATE TABLE results AS "
                    "SELECT routes.airline, routes.stops, routes.equipment, "
                    "initialairport.airport_id as sourceid, initialairport.name as sourcename, initialairport.city as sourcecity, initialairport.country as sourcecountry, initialairport.latitude as sourcelatitude, initialairport.longitude as sourcelongitude, initialairport.altitude as sourcealtitude, "
                    "finalairport.airport_id as finalid, finalairport.name as finalname, finalairport.city as finalcity, finalairport.country as finalcountry, finalairport.latitude as finallatitude, finalairport.longitude as finallongitude, finalairport.altitude as finalaltitude "
                    "FROM routes "
                    "INNER JOIN airports initialairport ON  initialairport.airport_id = routes.source_id "
                    "INNER JOIN airports finalairport on finalairport.airport_id = routes.destination_id; ")

        conn.commit()
    except sqlite3.OperationalError as e:
        print("Couldn't connect to database: {}".format(e.args[0]))





if __name__ == '__main__':
    main()

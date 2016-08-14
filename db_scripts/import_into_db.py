#! ~/miniconda3/bin/python

import sqlite3
from classes import *
import csv
from pprint import pprint


def main():
    try:
        #Try to connect
        print("Trying to connect to database...")

        conn = sqlite3.connect(r"../database/openflight.db")

        c = conn.cursor()

        print("Connection established!")

        #Build required tables
        print("Preparing airport table...")

        try:
                #criar table dos airports
            c.execute("CREATE TABLE airports (airport_id INTEGER PRIMARY KEY, name TEXT, city TEXT, country TEXT, IATA TEXT, "
                "ICAO TEXT, latitude REAL, longitude REAL, altitude REAL, timezone REAL, dst TEXT, tz TEXT);");

            # ler o csv
            with open('../data/airports.dat.txt', 'r') as csvfile:
                 filereader = csv.reader(csvfile, delimiter=',')
                 for row in filereader:
                    
                    #print(row)
                    airportDict = Airport.csvToDict(row)
                    
                    #pprint(airportDict)
                    airport = Airport(**airportDict)
                    airport.addToTable(c)
        except sqlite3.OperationalError as e:
            print("{}".format(e.args[0]))
        
        

        #linha a linha criar um objecto airport e mete-lo na table airport dentro da db

        # Save (commit) the changes
        conn.commit()

        print("Preparing airline table...")

        c.execute("CREATE TABLE airlines (airline_id INTEGER PRIMARY KEY, name TEXT, alias TEXT, IATA TEXT, ICAO TEXT, callsign TEXT, "
            "country TEXT, active TEXT);");

        with open('../data/airlines.dat.txt', 'r') as csvfile:
             filereader = csv.reader(csvfile, delimiter=',')
             for row in filereader:
                
                #print(row)
                airlineDict = Airline.csvToDict(row)
                pprint(airlineDict)
                
                #pprint(airportDict)
                airline = Airline(**airlineDict)
                airline.addToTable(c)


        # Save (commit) the changes
        conn.commit()

        print("Preparing route table...")

        c.execute("CREATE TABLE routes (airline TEXT, airline_id INTEGER, "
            "source TEXT, source_id INTEGER, "
            "destination TEXT, destination_id INTEGER , "
            "codeshare TEXT, stops INTEGER, equipment TEXT, FOREIGN KEY(airline_id) REFERENCES airlines(airline_id),"
            "FOREIGN KEY(source_id, destination_id) REFERENCES airports(airport_id, airport_id));");

        with open('../data/routes.dat.txt', 'r') as csvfile:
             filereader = csv.reader(csvfile, delimiter=',')
             for row in filereader:
                
                #print(row)
                routesDict = Route.csvToDict(row)
                #pprint(routesDict)
                
                #pprint(airportDict)
                route = Route(**routesDict)
                route.addToTable(c)
        
        # Save (commit) the changes
        conn.commit()


    except sqlite3.OperationalError as e:
        print("Couldn't connect to database: {}".format(e.args[0]))


if __name__ == '__main__':
    main()
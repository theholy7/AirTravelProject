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
        
        #criar table dos airports
        c.execute("CREATE TABLE airports (airport_id TEXT, name TEXT, city TEXT, country TEXT, IATA TEXT, "
            "ICAO TEXT, latitude REAL, longitude, REAL, altitude REAL, timezone REAL, dst TEXT, tz TEXT);");

        # ler o csv
        with open('../data/airports.dat.txt', 'r') as csvfile:
             filereader = csv.reader(csvfile, delimiter=',')
             for row in filereader:
                
                #print(row)
                airportDict = Airport.csvToDict(row)
                
                #pprint(airportDict)
                airport = Airport(**airportDict)
                airport.addToTable(c)

        #linha a linha criar um objecto airport e mete-lo na table airport dentro da db

        # Save (commit) the changes
        conn.commit()

        print("Preparing airline table...")

        c.execute("CREATE TABLE airlines (airline_id TEXT, name TEXT, alias TEXT, IATA TEXT, ICAO TEXT, callsign TEXT, "
            "country TEXT, active TEXT);");


        # Save (commit) the changes
        conn.commit()

        print("Preparing route table...")

        c.execute("CREATE TABLE airlines (airline_id TEXT, name TEXT, alias TEXT, IATA TEXT, ICAO TEXT, callsign TEXT, "
            "country TEXT, active TEXT);");

        
        # Save (commit) the changes
        conn.commit()


    except sqlite3.OperationalError as e:
        print("Couldn't connect to database: {}".format(e.args[0]))


if __name__ == '__main__':
    main()
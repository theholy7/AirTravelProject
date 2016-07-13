#! ~/miniconda3/bin/python

class Airport(object):
    """Class to define an airport object. Pass arguments with a dict.

    Airport ID  Unique OpenFlights identifier for this airport.

    Name    Name of airport. May or may not contain the City name.

    City    Main city served by airport. May be spelled differently from Name.

    Country Country or territory where airport is located.

    IATA/FAA    3-letter FAA code, for airports located in Country "United States of America".
    3-letter IATA code, for all other airports. Blank if not assigned.

    ICAO    4-letter ICAO code. Blank if not assigned.

    Latitude    Decimal degrees, usually to six significant digits. Negative is South, positive is North.

    Longitude   Decimal degrees, usually to six significant digits. Negative is West, positive is East.

    Altitude    In feet.

    Timezone    Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.

    DST Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown).

    Tz database time zone   Timezone in "tz" (Olson) format, eg. "America/Los_Angeles". """

    def __init__(self, **kwargs):
        """airportID, name, city, country, IATA, ICAO, latitude, longitude, altitude, timezone, DST, tz"""
        
        super(Airport, self).__init__()
        
        self.airportID = kwargs.get('airportID');
        self.name = kwargs.get('name');
        self.city = kwargs.get('city');
        self.country = kwargs.get('country');
        self.IATA = kwargs.get('IATA');
        self.ICAO = kwargs.get('ICAO');
        self.latitude = kwargs.get('latitude');
        self.longitude = kwargs.get('longitude');
        self.altitude = kwargs.get('altitude');
        self.timezone = kwargs.get('timezone');
        self.DST = kwargs.get('DST');
        self.tz = kwargs.get('tz');

    def addToTable(self, cursor):
        print("INSERT INTO airports (airport_id, name, city, country, IATA, ICAO, latitude, longitude, altitude, timezone, dst, tz) VALUES "
            "('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, '{}', '{}');".format(
                self.airportID,
                self.name,
                self.city,
                self.country,
                self.IATA,
                self.ICAO,
                self.latitude,
                self.longitude,
                self.altitude,
                self.timezone,
                self.DST,
                self.tz
                ))

        cursor.execute("INSERT INTO airports (airport_id, name, city, country, IATA, ICAO, latitude, longitude, altitude, timezone, dst, tz) VALUES "
            "( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (
                self.airportID,
                self.name,
                self.city,
                self.country,
                self.IATA,
                self.ICAO,
                self.latitude,
                self.longitude,
                self.altitude,
                self.timezone,
                self.DST,
                self.tz
                )
            )


    @staticmethod
    def csvToDict(args):
        airportDict = dict(zip(['airportID', 'name', 'city', \
        'country', 'IATA', 'ICAO', \
        'latitude', 'longitude', 'altitude', \
        'timezone', 'DST', 'tz'], args))

        return airportDict

class Airline(object):
    """Class to define Airline. Pass arguments with a dict.
    
    Airline ID  Unique OpenFlights identifier for this airline.
    Name    Name of the airline.
    Alias   Alias of the airline. For example, All Nippon Airways is commonly known as "ANA".
    IATA    2-letter IATA code, if available.
    ICAO    3-letter ICAO code, if available.
    Callsign    Airline callsign.
    Country Country or territory where airline is incorporated.
    Active  "Y" if the airline is or has until recently been operational, "N" if it is defunct. This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as "Y".

    """
    def __init__(self, **kwargs):
        super(Airline, self).__init__()
        self.airlineID = kwargs.get('airlineID');
        self.name = kwargs.get('name');
        self.alias = kwargs.get('alias');
        self.IATA = kwargs.get('IATA');
        self.ICAO = kwargs.get('ICAO');
        self.callsign = kwargs.get('callsign');
        self.country = kwargs.get('country');
        self.active = kwargs.get('active');



    @staticmethod
    def csvToDict(args):
        airlineDict = dict(zip(['airlineID', 'name', 'alias', \
        'IATA', 'ICAO', 'callsign', \
        'country', 'active'], args))

        return airlineDict


class Route(object):
    """Class to define a Route. Pass arguments with a dict.
    Airline 2-letter (IATA) or 3-letter (ICAO) code of the airline.
    Airline ID  Unique OpenFlights identifier for airline (see Airline).
    Source airport  3-letter (IATA) or 4-letter (ICAO) code of the source airport.
    Source airport ID   Unique OpenFlights identifier for source airport (see Airport)
    Destination airport 3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
    Destination airport ID  Unique OpenFlights identifier for destination airport (see Airport)
    Codeshare   "Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
    Stops   Number of stops on this flight ("0" for direct)
    Equipment   3-letter codes for plane type(s) generally used on this flight, separated by spaces

    """
    def __init__(self, **kwargs):
        super(Route, self).__init__()        
        self.airline = kwargs.get('airline');
        self.airlineID = kwargs.get('airlineID');
        self.source = kwargs.get('source');
        self.sourceID = kwargs.get('sourceID');
        self.destination = kwargs.get('destination');
        self.destinationID = kwargs.get('destinationID');
        self.codeshare = kwargs.get('codeshare');
        self.stops = kwargs.get('stops');
        self.equipment = kwargs.get('equipment');

    @staticmethod
    def csvToDict(*rgs):
        routeDict = dict(zip(['airline', 'airlineID', 'source', \
        'sourceID', 'destination', 'destinationID', \
        'codeshare', 'stops', 'equipment'], args))

        return routeDict

    
#! ~/miniconda3/bin/python

class Airport(object):
	"""Class to define an airport object. Pass arguments with a dict.

	Airport ID	Unique OpenFlights identifier for this airport.

	Name	Name of airport. May or may not contain the City name.

	City	Main city served by airport. May be spelled differently from Name.

	Country	Country or territory where airport is located.

	IATA/FAA	3-letter FAA code, for airports located in Country "United States of America".
	3-letter IATA code, for all other airports. Blank if not assigned.

	ICAO	4-letter ICAO code. Blank if not assigned.

	Latitude	Decimal degrees, usually to six significant digits. Negative is South, positive is North.

	Longitude	Decimal degrees, usually to six significant digits. Negative is West, positive is East.

	Altitude	In feet.

	Timezone	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.

	DST	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown).

	Tz database time zone	Timezone in "tz" (Olson) format, eg. "America/Los_Angeles". """

	def __init__(self, **kwargs):
		"airportID, name, city, country, IATA, ICAO, latitude, longitude, altitude, timezone, DST, tz"
		
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


	@staticmethod
	def csvToDict(*args):
		airportDict = dict(zip(['airportID', 'name', 'city', \
			'country', 'IATA', 'ICAO', \
			'latitude', 'longitude', 'altitude', \
			'timezone', 'DST', 'tz'], *args))

		return airportDict
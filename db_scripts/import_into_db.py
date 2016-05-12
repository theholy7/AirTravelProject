#! ~/miniconda3/bin/python

import sqlite3


def main():
	try:
		print("Trying to connect to database...")

		conn = sqlite3.connect("../database/openflight.db")

		print("Connection established!")

	except sqlite3.OperationalError as e:
		print("Couldn't connect to database: {}".format(e.args[0]))


if __name__ == '__main__':
	main()
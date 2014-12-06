# -*- coding: utf-8-*-

import logging
import argparse
import sys
from Objects.arduinoPlug import arduinoPlug
# need spidev, wiringpi2

# Argument on startup
parser = argparse.ArgumentParser(description='Domotic server center')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
args = parser.parse_args()

'''
Basic conventions :

Object are to be a name, an address
Message have to be an Object and an order
'''


class ServerDomotique(object):
	def __init__(self):
		self._logger = logging.getLogger(__name__)

		# Contains all object associated with there address
		# (e.g the place on the plug)
		plug_number = 0
		plug_number = int(raw_input("How many plug on you arduino controlled \
plug ? "))
		while plug_number == 0:
			print 'it should be more than 0'
			plug_number = int(raw_input("How many plug on you arduino controlled \
plug ? "))
		self.arduinoPlug = arduinoPlug(nb_plug=plug_number)

	def handleforever(self):
		while True:
			order = raw_input('what order would you like to send ? ')
			plug = raw_input('on which plug ? ')
			if order != "" and plug != "":
				self.arduinoPlug.send_order(int(plug), order)
			else:
				break


if __name__ == "__main__":

	print "Server Domotique started"

	logging.basicConfig()
	logger = logging.getLogger()

	if args.debug:
		logger.setLevel(logging.DEBUG)

	try:
		app = ServerDomotique()
	except:
		logger.exception("Error occured!", exc_info=True)
		print "Make sure that the SPI is enable by editing : \
		/etc/modprobe.d/raspi-blacklist.conf"
		sys.exit(1)

	app.handleforever()

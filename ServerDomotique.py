# -*- coding: utf-8-*-
from nrf24 import Nrf24
import logging
import argparse
import sys

#need spidev, wiringpi2

#Argument on startup
parser = argparse.ArgumentParser(description='Domotic server center')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
args = parser.parse_args()


class ServerDomotique(object):
	def __init__(self):
		self.objects=dict()
		self._logger = logging.getLogger(__name__)
		
		self.flag=0
		
		#Nrf24
		self.nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
		self.nrf.config()
		self.nrf.setRADDR("server_rec")
		self.nrf.setTADDR("server_send")
		
		
	def testingNRF(self):
		while True:
			if self.flag==0:
				if not self.nrf.isSending():
					self._logger.info("NRF trying to send information")
					self.nrf.send(map(ord,"Helloooo"))
					self.flag=1
			else:
				if self.nrf.dataReady():
					self._logger.info("NRF received DATA")
					print self.nrf.getData()
					self.flag=0
					break
				
				
				
if __name__ == "__main__":

	print "Server Domotique started"

	logging.basicConfig()
	logger = logging.getLogger()

	if args.debug:
		logger.setLevel(logging.DEBUG)
		
	try:
		app=ServerDomotique()
	except:
		logger.exception("Error occured!", exc_info=True)
		sys.exit(1)
	
	app.testingNRF()
	
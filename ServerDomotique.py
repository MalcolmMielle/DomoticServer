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

'''
Basic conventions : 
	Object are to a name, an address
	Message have to be an Object and an order

'''

class PriseArduino(object):
	def __init__(self, nbOfPlug):
		self.nbOfPlug=nbOfPlug
		
	#Return the formated order that the plug can understand
	def write(self, plug, order):
		return str(plug)+";"+str(order)
	
	


class ServerDomotique(object):
	def __init__(self):
		self.instance=list()
		self.instance.append(NRFinstance())
		
	
	def testing(self):
		for instance in self.instance:
			instance.testing()
		
	
class NRFinstance(object):
	def __init__(self):
		self._logger = logging.getLogger(__name__)
		self.flag=0
		self.obj=list()
		
		#Nrf24
		self.nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
		self.nrf.config()
		self.nrf.setRADDR("server_rec")
		self.nrf.setTADDR("server_send")
		
	def write(self, order):
		for obj in self.obj:
			if isinstance(obj, PriseArduino):
				self._logger.info("Working with a Prise Arduino")
				order_new=obj.write(order)
				self._logger.info("Seding the object through NRF")
				self.nrf.send(map,(ord,order_new))
		
		
	def testing(self):
		while True:
			if self.flag==0:
				if not self.nrf.isSending():
					self._logger.info("NRF trying to send information")
					self.nrf.send(map(ord,"Helloooo"))
					self.flag=1
			else:
				if self.nrf.dataReady():
					self._logger.info("NRF received DATA "+ str())
					print self.nrf.getData()
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
		print "Make sure that the SPI is enable by editing : /etc/modprobe.d/raspi-blacklist.conf"
		sys.exit(1)
	
	app.testing()
	
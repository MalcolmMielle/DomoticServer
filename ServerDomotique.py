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
	Object are to be a name, an address
	Message have to be an Object and an order

'''

#Base Object class
class BaseObject(object):
	def __init__(self):
		if type(self) == BaseObject:
			raise Exception("AbstractClass is an abstract class and cannot be instantiated.")
	
	def write(self, address, order):
		raise NotImplementedError


class PriseArduino(BaseObject):
	def __init__(self, nbOfPlug):
		self.nbOfPlug=nbOfPlug
		
	#Return the formated order that the plug can understand
	def write(self, address, order):
		return str(address)+";"+str(order)
	
	


class ServerDomotique(object):
	def __init__(self):
		self._logger = logging.getLogger(__name__)
		self.instance=list()
		self.instance.append(NRFinstance(self._logger))
		
	
	#TODO test function
	def getAllObject(self):
		all=list()
		for instance in self.instance:
			all=all+instance.obj
		return all
	
	def testing(self):
		for instance in self.instance:
			self._logger.info("Testing instance "+str(instance))
			instance.testing()
		
	
class NRFinstance(object):
	def __init__(self,_loger):
		self._logger =_loger
		self.flag=0
		self.obj=list()
		
		#Nrf24
		self.nrf = Nrf24(cePin=2,csnPin=3,channel=10,payload=8)
		self.nrf.config()
		self.nrf.setRADDR("server_rec")
		self.nrf.setTADDR("server_send")
		
	def write(self, order):
		for obj in self.obj:
			try:
				isinstance(obj,BaseObject)
			except:
				self._logger.error(type(obj) +" did not enerited from BaseObject")
				raise
			try:
				self._logger.info("Working with a "+type(obj).__name__)
				order_new=obj.write(order)
				self._logger.info("Sending the order : '"+order+" through NRF")
				self.nrf.send(map,(ord,order_new))
			except:
				self._logger.warning("Something went wrong while using object "+type(obj))
		
		
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
	
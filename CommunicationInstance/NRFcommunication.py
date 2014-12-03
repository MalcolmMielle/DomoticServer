from nrf24 import Nrf24
import Objects.BaseObject
import CommunicationInstance.NRFcommunication
import logging


	
class NRFinstance(object):
	def __init__(self,_loger=logging.getLogger(__name__)):
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
	
	def returnorder(self, order):
		print order
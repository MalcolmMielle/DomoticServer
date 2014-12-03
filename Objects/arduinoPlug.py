from Lamp import Lamp
from CommunicationInstance.NRFcommunication import NRFinstance
import logging
import copy

#Dictionary of available object
DICT_CLASS=dict()
DICT_CLASS['LAMP']=Lamp(1)

def isExistingClass(demand):
	demand=demand.upper()
	for key in DICT_CLASS:
		if key==demand:
			return DICT_CLASS[key]
	return False

class arduinoPlug(object):
	def __init__(self, NB_PLUG=4, _loger=logging.getLogger(__name__)):
		self._logger = _loger
		#Contains all object associated with there address (e.g the place on the plug)
		self.arduinoPlug=list()
		for nb, ad in enumerate(range(NB_PLUG)):
			print 'On plug number '+str(nb)
			input=raw_input('What object : ')
			classtype=isExistingClass(input)
			while classtype==False:
				print 'Wrong input'
				input=raw_input('What object : ')
				classtype=isExistingClass(input)
			obj=copy.copy(classtype)
			obj.id=nb
			self.arduinoPlug.append(obj)
		self._logger.info(self.arduinoPlug)
		self.nrf=NRFinstance(self._logger)

	def testing(self):
		self.nrf.testing()
		
	def handleforever(self):
		pass
		
	def __repr__(self):
		return "arduinoPlug of size "+str(len(self.arduinoPlug))
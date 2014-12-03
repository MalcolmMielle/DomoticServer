from Lamp import Lamp
from CommunicationInstance.NRFcommunication import NRFinstance

NB_PLUG=3


''' 
	Dict example :
	'lamp'=Lamp object, adresse =1
	'fridge'=Fridge object, adresse = 2
	'lamp salon'=Lamp object, adresse = 3
'''

class arduinoPlug(object):
	def __init__(self, _loger):
		self._logger = _loger
		
		#Contains all object associated with there address (e.g the place on the plug)
		self.arduinoPlug=list()
		for nb, ad in enumerate(range(NB_PLUG)):
			print 'On plug number '+str(nb)
			input=raw_input('What object : ')
			self.arduinoPlug.append(Lamp(nb))
		print self.arduinoPlug
		
		self.nrf=NRFinstance(self._logger)
	
	#TODO test function
	def getAllObject(self):
		all=list()
		for instance in self.arduinoPlug:
			all=all+instance.obj
		return all

	def testing(self):
		self.nrf.testing()
			
from Lamp import Lamp
import logging
import copy

# Dictionary of available object. All Object must inhertite of BaseObject
DICT_CLASS = dict()
DICT_CLASS['LAMP'] = Lamp(1)


def isExistingClass(demand):
	demand = demand.upper()
	for key in DICT_CLASS:
		if key == demand:
			return DICT_CLASS[key]
	return False


class arduinoPlug(object):
	def __init__(self, nb_plug=None):
		self._logger = logging.getLogger(__name__)
		# Contains all object associated with there address
		# (e.g the place on the plug)
		self.arduinoPlug = list()
		for nb, ad in enumerate(range(nb_plug)):
			print 'On plug number ' + str(nb)
			input = raw_input('What object : ')
			classtype = isExistingClass(input)

			while classtype is False:
				print 'Wrong input'
				print 'On plug number ' + str(nb)
				input = raw_input('What object : ')
				classtype = isExistingClass(input)

			obj = copy.copy(classtype)
			obj.id = nb
			self.arduinoPlug.append(obj)
		self._logger.info(self.arduinoPlug)

		# TODO ucomment for the pi + pass it as an attribute ?
		# self.nrf=NRFinstance(self._logger)

	def send_order(self, id, order):
		try:
			obj = self.arduinoPlug[id]
			order = obj.format_order(order)
			self._logger.info("sending the order " + order)
			# TODO uncomment for the pi
			# self.nrf.write(order)
		except Exception, e:
			print "Error in executing send_order: %s" % str(e)

	def testing(self):
		self.nrf.testing()

	def __repr__(self):
		return "arduinoPlug of size " + str(len(self.arduinoPlug))

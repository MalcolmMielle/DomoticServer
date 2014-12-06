import BaseObject
import logging


class Lamp(BaseObject.BaseObject):
	def __init__(self, id):
		super(Lamp, self).__init__()
		self._logger = logging.getLogger(__name__)
		self._id = str(id)
		self.order = dict()
		self.order['on'] = 'on'
		self.order['off'] = 'off'
		self.order['more'] = 'more'
		self.order['less'] = 'less'

	# getter
	@property
	def id(self):
		return self._id

	# setter
	@id.setter
	def id(self, value):
		self._id = str(value)

	# Return the formated order that the plug can understand
	def format_order(self, order):
		for key in self.order:
			if order == key:
				self._logger.info("Formating the message " + order)
				return self._id + ";" + str(self.order[key])
		raise Exception("The order was not understand for a " + str(type(self)))

	def __repr__(self):
		return "Lamp object of id : " + self._id

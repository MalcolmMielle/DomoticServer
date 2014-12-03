import BaseObject


class Lamp(BaseObject.BaseObject):
	def __init__(self, id):
		super(Lamp, self).__init__()
		self._id=id
		
	#getter
	@property
	def id(self):
		return self._id
	
	#setter
	@id.setter
	def id(self, value):
		self._id=str(value)
		
	#Return the formated order that the plug can understand
	def format_order(self, order):
		return self._id+";"+str(order)
	
	def __repr__(self):
		return "Lamp object of id : "+self._id
	
	
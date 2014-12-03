import BaseObject


class Lamp(BaseObject.BaseObject):
	def __init__(self, id):
		super(Lamp, self).__init__()
		self._id=str(id)
		self.order=dict()
		self.order['on']='on_arduino'
		self.order['off']='off_arduino'
		self.order['more']='more'
		self.order['less']='less'
		
		
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
		for key in self.order:
			if order==key:
				return self._id+";"+str(self.order[key])	
		raise Exception("The order was not understand for a " +type(self))
	
	def __repr__(self):
		return "Lamp object of id : "+self._id
	
	
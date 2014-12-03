import BaseObject


class Lamp(BaseObject.BaseObject):
	def __init__(self, name):
		super(Lamp, self).__init__()
		self.name=name
		
	#Return the formated order that the plug can understand
	def write(self, address, order):
		return str(address)+";"+str(order)
	
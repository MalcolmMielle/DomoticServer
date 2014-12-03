import BaseObject


class Lamp(BaseObject.BaseObject):
	def __init__(self, id):
		super(Lamp, self).__init__()
		self.id=str(id)
		
	#Return the formated order that the plug can understand
	def format_order(self, order):
		return self.id+";"+str(order)
	
	def __repr__(self):
		return "Lamp object of id : "+self.id
	
	
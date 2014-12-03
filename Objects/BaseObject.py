



#Base Object class
class BaseObject(object):
	def __init__(self):
		if type(self) == BaseObject:
			raise Exception("AbstractClass is an abstract class and cannot be instantiated.")
	
	def write(self, address, order):
		raise NotImplementedError
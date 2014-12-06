import unittest
from Objects.Lamp import Lamp
from Objects.arduinoPlug import arduinoPlug

# To launch the test :
# from the unit folder : python -m unittest discover -t ..


class RandomTest(unittest.TestCase):

	def test_Lamp(self):
		print 'test lamp'
		"""Test le fonctionnement de la class 'Lamp'."""
		lamp = Lamp(1)
		self.assertEqual(str(1), lamp.id)
		lamp.id = 52
		# Verifie que 'elt' est dans 'liste'
		self.assertEqual(str(52), lamp.id)

		self.assertIn('on', lamp.order)
		self.assertEqual('52;on_arduino', lamp.format_order('on'))

		with self.assertRaises(Exception):
			lamp.format_order('wrong_order')

	def test_Arduino(self):
		print 'test arduino'
		obj = list()
		obj.append(Lamp(0))
		obj.append(Lamp(1))
		ard = arduinoPlug(2, obj)
		print ard.send_address

from RF24 import *
import Objects.BaseObject
import CommunicationInstance.NRFcommunication
import logging
import time

# Dependant on https://github.com/TMRh20/RF24

millis = lambda: int(round(time.time() * 1000))


class NRFinstance(object):
	def __init__(self, send_adress=None, receive_adress=None):
		self._logger = logging.getLogger(__name__)
		self.flag = 0

		# Nrf24
		self.radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_8MHZ)
		self.pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]
		self.radio.begin()
		self.radio.enableDynamicPayloads()
		self.radio.setRetries(5, 15)
		self.radio.openWritingPipe(self.pipes[0])
		self.radio.openReadingPipe(1, self.pipes[1])

	def write(self, order):
		# The payload will always be the same, what will change is how much of it we send.
		# First, stop listening so we can talk.
		self.radio.stopListening()

		# Take the time, and send it.  This will block until complete
		print 'Now sending length ', order, ' ... ',
		self.radio.write(order)

		# Now, continue listening
		self.radio.startListening()

	def read(self):
		# Wait here until we get a response, or timeout
		started_waiting_at = millis()
		timeout = False
		while (not self.radio.available()) and (not timeout):
			if (millis() - started_waiting_at) > 500:
				timeout = True

		# Describe the results
		if timeout:
			raise Exception('failed, response timed out.')
		else:
			# Grab the response, compare, and send to debugging spew
			len = self.radio.getDynamicPayloadSize()
			receive_payload = self.radio.read(len)

			# Spew it
			print 'got response size=', len, ' value="', receive_payload, '"'
		return receive_payload

	def testing(self):
		while True:
			if self.flag == 0:
				if not self.nrf.isSending():
					self._logger.info("NRF trying to send information")
					self.write("Helloooo")
					self.flag = 1
			else:
				if self.nrf.dataReady():
					self._logger.info("NRF received DATA " + str())
					print self.read()
					break

import sys
import mainwindow
import argparse
import logging
from PyQt4 import QtGui
from Objects.arduinoPlug import arduinoPlug
from Objects.Lamp import Lamp

# Argument on startup
parser = argparse.ArgumentParser(description='Domotic server center')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
args = parser.parse_args()


class MainWindow(QtGui.QMainWindow):
	def __init__(self, serverDomotic):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.num_plug = 132
		self.server = serverDomotic
		self.initUi()

	def initUi(self):
		# self.btn.move(20, 20)
		# self.le = QtGui.QLineEdit(self)
		# self.ui.pushButton.clicked.connect(self.ChangeNumberPlug)
		self.ui.pushButton.clicked.connect(self.sendONorder)
		self.le = QtGui.QLabel(str(self.num_plug), self)
		self.le.move(200, 20)
		self.setWindowTitle('Input dialog')

	def sendONorder(self):
		self.server.send_order(0, "on")

	def ChangeNumberPlug(self):
		num, ok = QtGui.QInputDialog.getInt(self, 'Input Dialog', 'Nb of plug:')
		if ok:
			self.num_plug = num
			# update the value inside the box
			self.le.setNum(self.num_plug)
			print 'type : ' + str(type(num)) + 'and texte : ' + str(self.num_plug)

	def accept(self):
		pass

	def reject(self):
		pass


class MainWindow_old(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow_old, self).__init__()
		self.ui = mainwindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.advanceSlider)

	def advanceSlider(self):
		self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

	def accept(self):
		pass

	def reject(self):
		pass


def main():
	print "Server Domotique started"

	logging.basicConfig()
	logger = logging.getLogger()

	if args.debug:
		logger.setLevel(logging.DEBUG)

	try:
		app = QtGui.QApplication(sys.argv)
	except:
		logger.exception("Error occured!", exc_info=True)
		print "Make sure that the SPI is enable by editing : \
		/etc/modprobe.d/raspi-blacklist.conf"
	# List of object
	obj = list()
	obj.append(Lamp(0))
	obj.append(Lamp(1))
	# TODO replace this by a server_domotique object
	arduplug = arduinoPlug(2, obj)
	other = MainWindow(arduplug)
	other.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

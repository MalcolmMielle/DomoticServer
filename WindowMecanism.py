import sys
from PyQt4 import QtGui
import mainwindow


class InitWindow(QtGui.QWidget):
	def __init__(self):
		super(InitWindow, self).__init__()
		self.num_plug = 132
		self.initUi()

	def initUi(self):
		self.btn = QtGui.QPushButton('Add number of plug : ', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.ChangeNumberPlug)

		# self.le = QtGui.QLineEdit(self)
		self.le = QtGui.QLabel(str(self.num_plug), self)
		self.le.move(200, 20)

		self.setGeometry(300, 300, 500, 150)
		self.setWindowTitle('Input dialog')
		self.show()

	def ChangeNumberPlug(self):
		num, ok = QtGui.QInputDialog.getInt(self, 'Input Dialog', 'Nb of plug:')
		if ok:
			self.num_plug = num
			# update the value inside the box
			self.le.setNum(self.num_plug)
			print 'type : ' + str(type(num)) + 'and texte : ' + str(self.num_plug)


class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.num_plug = 132
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)
		# self.resize(50,30)
		# self.ui.pushButton.clicked.connect(self.advanceSlider)
		self.center()
		print 'centered'
		self.btn = QtGui.QPushButton('Add number of plug : ', self)

		self.btn.move(20, 20)
		self.btn.clicked.connect(self.ChangeNumberPlug)

		# self.le = QtGui.QLineEdit(self)
		self.le = QtGui.QLabel(str(self.num_plug), self)
		self.le.move(200, 20)

		self.setGeometry(300, 300, 500, 150)
		self.setWindowTitle('Input dialog')

	def ChangeNumberPlug(self):
		num, ok = QtGui.QInputDialog.getInt(self, 'Input Dialog', 'Nb of plug:')
		if ok:
			self.num_plug = num
			# update the value inside the box
			self.le.setNum(self.num_plug)
			print 'type : ' + str(type(num)) + 'and texte : ' + str(self.num_plug)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def advanceSlider(self):
		self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)


def main():
	app = QtGui.QApplication(sys.argv)
	other = MainWindow()
	other.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

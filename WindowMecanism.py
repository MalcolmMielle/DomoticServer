import sys
from PyQt4 import QtGui
import mainwindow


class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.ChangeNumberPlug)
		self.num_plug = 132
		self.initUi()

	def initUi(self):
		# self.btn.move(20, 20)
		# self.le = QtGui.QLineEdit(self)
		self.le = QtGui.QLabel(str(self.num_plug), self)
		self.le.move(200, 20)
		self.setWindowTitle('Input dialog')

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
	app = QtGui.QApplication(sys.argv)
	other = MainWindow()
	other.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

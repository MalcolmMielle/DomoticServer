import sys
from PyQt4 import QtGui
import mainwindow

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)
		#self.resize(50,30)
		self.ui.pushButton.clicked.connect(self.advanceSlider)
		self.center()

	def center(self):
		qr=self.frameGeometry()
		cp=QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def advanceSlider(self):
		self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

app = QtGui.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())

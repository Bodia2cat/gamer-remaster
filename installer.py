#Windows Update 1.1-beta
from PyQt5 import QtWidgets
from design import Ui_MainWindow  
import sys
import os
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        self.ui.progressBar.setValue(0)
        print("[+] Install is started")
        self.ui.progressBar.setValue(50)
        os.system("pip install colorama")
        self.ui.progressBar.setValue(100)
        self.ui.label_2.setText("Все зависимости установленны")
            
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
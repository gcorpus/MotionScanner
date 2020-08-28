from PySide2.QtWidgets import *
from PySide2.QtGui import *


class MotionScannerController(QWidget):

    def __init__(self, parent=None):         
        super(MotionScannerController, self).__init__(parent)  
        self.SetupUI()

    def SetupUI(self):
        self.setWindowTitle("Motion scanner")
        self.resize(1000,800)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = MotionScannerController()  
    # setup stylesheet
    app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())
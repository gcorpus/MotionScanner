import sys
from PySide2.QtWidgets import *
from MotionScanner.Controller.motion_scanner_controller import MotionScannerController

if __name__ == '__main__':
    print('Enter to app')
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = MotionScannerController()
    # setup stylesheet
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    app.setStyleSheet(open('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/stylesheet.css').read())
    #Show babel
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())



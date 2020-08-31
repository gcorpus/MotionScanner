import sys
from PySide2.QtWidgets import *
from MotionScanner.Controller.motion_scanner_controller import MotionScannerController

 # Create the Qt Application     
app = QApplication(sys.argv)     
# Create babel  
controller = MotionScannerController()  
# setup stylesheet
# app.setStyleSheet(qdarkgraystyle.load_stylesheet())
#Show babel
controller.show()     
# Run the main Qt loop     
sys.exit(app.exec_())
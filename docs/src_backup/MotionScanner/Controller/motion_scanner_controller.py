from PySide2.QtWidgets import *
from PySide2.QtGui import *
from .scanner_parameters_controller import ScannerParametersController
from .user_profile_controller import UserProfileController
from ..Lib.motion_scanner_lib import MotionScannerLib



class MotionScannerController(QDialog):

    def __init__(self, parent=None):         
        super(MotionScannerController, self).__init__(parent)  
        self.SetupUI()
        self.Initialize()
        # self._dialog.show()

    def SetupUI(self):
        self.setWindowTitle("Motion Scanner")
        self.resizeWidget(self,760,940)

        self._main_layout = QVBoxLayout(self)
        self._dialog = QMainWindow()

        # self._scanner_controls_dock = QDockWidget()
        
        self._scanner_controls_layout = QVBoxLayout()

        self._scanner_controls_group = QGroupBox()
        # self.resizeWidget(self._scanner_controls_group,640,640)

        self._scanner_controls_widget = ScannerParametersController()
        self._user_profile_widget = UserProfileController(user={'_id':'2323943','name':'Oso Blanco','heigth':'100 cm', 'weight':'10 kg','roles':['Dancer, Coach'],'disciplines':['Ballet','Fitness'],'routines':['Swan']})

        self._button_layout = QHBoxLayout()
        self._scanner_video_button = QPushButton('Scanner Video')
        self._scanner_video_button.setFixedSize(660,70)
        self._scanner_video_button.setStyleSheet("""background-color:#907BA6;font-size: 20px;font-weight: bold;""")

        self._button_layout.addStretch()
        self._button_layout.addWidget(self._scanner_video_button)
        self._button_layout.addStretch()

        self._scanner_controls_layout.addWidget(self._user_profile_widget)
        self._scanner_controls_layout.addWidget(self._scanner_controls_widget)
        self._scanner_controls_layout.addLayout(self._button_layout)
        self._scanner_controls_layout.addStretch()

        self._scanner_controls_group.setLayout(self._scanner_controls_layout)

        # self._scanner_controls_dock.setWidget(self._scanner_controls_group)
        # self._scanner_controls_dock.setFloating(False)

        # self._aux = QLabel('hfhdbfhdf')

        # self._dialog.setCentralWidget(self._aux)
        # self._dialog.addDockWidget(Qt.RightDockWidgetArea, self._scanner_controls_dock)

        self._main_layout.addWidget(self._scanner_controls_group)

    def Initialize(self):

        self._scanner_video_button.clicked.connect(MotionScannerLib.GetRealTimeWebCamVideo)

    def resizeWidget(self,widget,width,height):
        widget.setMinimumSize(width,height)
        widget.setMaximumSize(width,height)


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
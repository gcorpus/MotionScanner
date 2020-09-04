from PySide2.QtWidgets import *
from MotionScanner.Controller import AvatarController, UserProfileController, WebCamController, MeasurementMenuController, \
    ColorSetterController


class MotionScannerController(QWidget):

    def __init__(self, parent=None):
        super(MotionScannerController, self).__init__(parent)
        self._setupUI()
        self.initialize()

        self._low_hue = 0
        self._high_hue = 179
        self._low_saturation = 0
        self._high_saturation = 255
        self._low_value = 0
        self._high_value = 255

    def setLowHue(self, value):
        self._low_hue = value

    def setHighHue(self, value):
        self._high_hue = value

    def setLowSaturation(self, value):
        self._low_saturation = value

    def setHighSaturation(self, value):
        self._high_saturation = value

    def setLowValue(self, value):
        self._low_value = value

    def setHighValue(self, value):
        self._high_value = value

    def _setupUI(self):
        self.setWindowTitle("Motion Scanner")

        self._main_layout = QVBoxLayout(self)

        # Building menu
        menu_layout = QHBoxLayout()

        menu_bar = QMenuBar(self)
        settings_menu = menu_bar.addMenu('Settings')
        help_menu = menu_bar.addMenu('Help')

        action_markers = QAction('Color setter', self)
        action_markers.setShortcut('Ctrl+T')
        action_markers.triggered.connect(self._callColorSetter)

        action_exit = QAction('Exit', self)
        action_exit.setShortcut('Ctrl+E')
        action_exit.triggered.connect(self._callExit)

        action_manual = QAction('Manual',self)
        action_manual.setShortcut('Ctrl+N')
        action_manual.triggered.connect(self._callManual)

        action_about = QAction('About', self)
        action_about.setShortcut('Ctrl+A')
        action_about.triggered.connect(self._callAbout)

        settings_menu.addAction(action_markers)
        settings_menu.addAction(action_exit)

        help_menu.addAction(action_manual)
        help_menu.addAction(action_about)

        menu_layout.addWidget(menu_bar)

        # Create layout of main components | HORIZONTAL
        self._content_layout = QHBoxLayout()

        self._real_time_scanner_group = QGroupBox()
        self._real_time_scanner_layout = QVBoxLayout()

        self._measurement_widget = MeasurementMenuController()
        self._real_time_scanner_widget = WebCamController(type_='COLOR_RANGE', width=1280, height=720)

        self._real_time_scanner_layout.addWidget(self._measurement_widget)
        self._real_time_scanner_layout.addWidget(self._real_time_scanner_widget)
        self._real_time_scanner_layout.addStretch()

        self._real_time_scanner_group.setLayout(self._real_time_scanner_layout)

        self._content_layout.addWidget(self._real_time_scanner_group)

        # Create layout of data-controls | VERTICAL
        self._data_controls_layout = QVBoxLayout()

        self._user_profile_widget = UserProfileController(
            user={'_id': '2323943', 'name': 'Greek', 'heigth': '1.61 m', 'weight': '61 kg',
                  'roles': ['Dancer, Coach'], 'disciplines': ['Ballet', 'Fitness'], 'routines': ['Swan']})

        self._avatar_widget = AvatarController()

        self._play_scan_button = QPushButton('Scanning')
        self._play_scan_button.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._play_scan_button.setMinimumHeight(40)

        self._stop_scan_button = QPushButton('Stop scan')
        self._stop_scan_button.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._stop_scan_button.setMinimumHeight(40)

        self._test_button = QPushButton('TEST')

        self._data_controls_layout.addWidget(self._user_profile_widget)
        self._data_controls_layout.addWidget(self._play_scan_button)
        self._data_controls_layout.addWidget(self._stop_scan_button)
        self._data_controls_layout.addWidget(self._test_button)
        self._data_controls_layout.addWidget(self._avatar_widget)
        self._data_controls_layout.addStretch()

        self._content_layout.addLayout(self._data_controls_layout)

        self._main_layout.addLayout(menu_layout)
        self._main_layout.addLayout(self._content_layout)

    def initialize(self):
        self._play_scan_button.clicked.connect(lambda: self._real_time_scanner_widget.startVideoScanner(
                                                low_hue=self._low_hue, high_hue=self._high_hue,
                                                low_saturation=self._low_saturation, high_saturation=self._high_saturation,
                                                low_value=self._low_value, high_value=self._high_value))

        self._stop_scan_button.clicked.connect(lambda: self._real_time_scanner_widget.stopVideoStream())
        
        self._test_button.clicked.connect(self._test)

    def _callColorSetter(self):
        self._real_time_scanner_widget.stopVideoStream()
        _dialog = ColorSetterController(motion_scanner_controller=self)
        _dialog.Show()

    def _callExit(self):
        self.close()

    def _callManual(self):
        pass

    def _callAbout(self):
        pass
    
    def _test(self):
        print(self._avatar_widget.Head.isActived)
        print(self._avatar_widget.LeftShoulder.isActived)
        print(self._avatar_widget.Chest.isActived)
        print(self._avatar_widget.RightShouler.isActived)

        print(self._measurement_widget.isLength)
        print(self._measurement_widget.isSpeed)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    controller = MotionScannerController()
    controller.show()
    sys.exit(app.exec_())
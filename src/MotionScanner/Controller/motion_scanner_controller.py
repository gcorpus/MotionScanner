from PySide2.QtWidgets import *
from MotionScanner.Controller import AvatarController, UserProfileController, WebCamController, MeasurementMenuController, \
    ColorSetterController


class MotionScannerController(QWidget):

    def __init__(self, parent=None):
        super(MotionScannerController, self).__init__(parent)
        self._setupUI()
        self.Initialize()

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
        action_markers.triggered.connect(self._CallColorSetter)

        action_exit = QAction('Exit', self)
        action_exit.setShortcut('Ctrl+E')
        action_exit.triggered.connect(self._CallExit)

        action_manual = QAction('Manual',self)
        action_manual.setShortcut('Ctrl+N')
        action_manual.triggered.connect(self._CallManual)

        action_about = QAction('About', self)
        action_about.setShortcut('Ctrl+A')
        action_about.triggered.connect(self._CallAbout)

        settings_menu.addAction(action_markers)
        settings_menu.addAction(action_exit)

        help_menu.addAction(action_manual)
        help_menu.addAction(action_about)

        menu_layout.addWidget(menu_bar)

        # Create layout of main components | HORIZONTAL
        self._content_layout = QHBoxLayout()

        self._real_time_scanner_group = QGroupBox()
        self._real_time_scanner_layout = QVBoxLayout()

        self._measurement_control_widget = MeasurementMenuController()
        self._real_time_scanner_widget = WebCamController(width=1280, height=720)

        self._real_time_scanner_layout.addWidget(self._measurement_control_widget)
        self._real_time_scanner_layout.addWidget(self._real_time_scanner_widget)
        self._real_time_scanner_layout.addStretch()

        self._real_time_scanner_group.setLayout(self._real_time_scanner_layout)

        self._content_layout.addWidget(self._real_time_scanner_group)

        # Create layout of data-controls | VERTICAL
        self._data_controls_layout = QVBoxLayout()

        self._user_profile_widget = UserProfileController(
            user={'_id': '2323943', 'name': 'Greek', 'heigth': '1.61 m', 'weight': '61 kg',
                  'roles': ['Dancer, Coach'], 'disciplines': ['Ballet', 'Fitness'], 'routines': ['Swan']})

        self._avatar_controls_widget = AvatarController()

        self._play_scan_button = QPushButton('Scanning')
        self._play_scan_button.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._play_scan_button.setMinimumHeight(40)

        self._data_controls_layout.addWidget(self._user_profile_widget)
        self._data_controls_layout.addWidget(self._play_scan_button)
        self._data_controls_layout.addWidget(self._avatar_controls_widget)
        self._data_controls_layout.addStretch()

        self._content_layout.addLayout(self._data_controls_layout)

        self._main_layout.addLayout(menu_layout)
        self._main_layout.addLayout(self._content_layout)

    def Initialize(self):
        self._play_scan_button.clicked.connect(lambda: self._real_time_scanner_widget.StartVideoScanner(type_='RGB'))

    def _CallColorSetter(self):
        self._real_time_scanner_widget.StopVideoStream()
        _dialog = ColorSetterController()
        _dialog.Show()

    def _CallExit(self):
        self.close()

    def _CallManual(self):
        pass

    def _CallAbout(self):
        pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    controller = MotionScannerController()
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    controller.show()
    sys.exit(app.exec_())
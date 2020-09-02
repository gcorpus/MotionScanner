from PySide2.QtWidgets import *
from PySide2.QtGui import *
from MotionScanner.Controller import ICheckbox


class MeasurementMenuController(QWidget):

    def __init__(self, parent=None):
        super(MeasurementMenuController, self).__init__(parent)
        self.setupUI()

    def setupUI(self):
        self._main_layout = QVBoxLayout(self)

        self._measurement_menu_group = QGroupBox('Measurement Parameters')
        self._measurement_menu_layout = QHBoxLayout()

        self._length_checkbox = ICheckbox(label='Length')
        self._angle_checkbox = ICheckbox(label='Angles')
        self._speed_checkbox = ICheckbox(label='Speed')
        self._motion_path_checkbox = ICheckbox(label='Motion path')
        self._metadata_checkbox = ICheckbox(label='Metadata')
        self._performance_checkbox = ICheckbox(label='Performance')
        self._audio_step_checkbox = ICheckbox(label='Audio steps')

        self._measurement_menu_layout.addWidget(self._length_checkbox)
        self._measurement_menu_layout.addWidget(self._angle_checkbox)
        self._measurement_menu_layout.addWidget(self._speed_checkbox)
        self._measurement_menu_layout.addWidget(self._motion_path_checkbox)
        self._measurement_menu_layout.addWidget(self._metadata_checkbox)
        self._measurement_menu_layout.addWidget(self._performance_checkbox)
        self._measurement_menu_layout.addWidget(self._audio_step_checkbox)
        self._measurement_menu_group.setLayout(self._measurement_menu_layout)
        self._main_layout.addWidget(self._measurement_menu_group)

        self._measurement_menu_group.setStyleSheet("""font-family:Helvetica;color:black;font-size:20px;""")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # Create babel
    controller = MeasurementMenuController()
    # setup stylesheet
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    # Show babel
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from MotionScanner.Lib.Widgets import ICheckbox, ICombobox
from MotionScanner.Lib.Catalogs import BodyChunksCatalog


class MeasurementMenuController(QWidget):

    def __init__(self, parent=None):
        super(MeasurementMenuController, self).__init__(parent)

        self._setupUI()

    @property
    def isLine(self):
        return self._line_checkbox.isActived

    @property
    def isLength(self):
        return self._length_checkbox.isActived

    @property
    def isAngle(self):
        return self._angle_checkbox.isActived

    @property
    def isSpeed(self):
        return self._speed_checkbox.isActived

    @property
    def isMotionPath(self):
        return self._motion_path_checkbox.isActived

    @property
    def isMetadata(self):
        return self._metadata_checkbox.isActived

    @property
    def isPerformance(self):
        return self._performance_checkbox.isActived

    @property
    def isAudioStep(self):
        return self._audio_step_checkbox

    def _setupUI(self):
        self._main_layout = QVBoxLayout(self)

        self._measurement_menu_group = QGroupBox('Measurement Parameters')

        self._measurement_menu_layout = QVBoxLayout()
        self._measurement_menu_combobox = QHBoxLayout()
        self._measurement_menu_checkbox = QHBoxLayout()

        self._discipline_combobox = ICombobox(label='Discipline', items=BodyChunksCatalog.Tags)
        self._sequence_combobox = ICombobox(label='Sequence')
        self._movement_combobox = ICombobox(label='Movement')
        self._position_combobox = ICombobox(label='Position')

        self._measurement_menu_combobox.addWidget(self._discipline_combobox)
        self._measurement_menu_combobox.addWidget(self._sequence_combobox)
        self._measurement_menu_combobox.addWidget(self._movement_combobox)
        self._measurement_menu_combobox.addWidget(self._position_combobox)

        self._line_checkbox = ICheckbox(label='Lines')
        self._length_checkbox = ICheckbox(label='Length')
        self._angle_checkbox = ICheckbox(label='Angles')
        self._speed_checkbox = ICheckbox(label='Speed')
        self._motion_path_checkbox = ICheckbox(label='Motion path')
        self._metadata_checkbox = ICheckbox(label='Metadata')
        self._performance_checkbox = ICheckbox(label='Performance')
        self._audio_step_checkbox = ICheckbox(label='Audio steps')

        self._measurement_menu_checkbox.addWidget(self._metadata_checkbox)
        self._measurement_menu_checkbox.addWidget(self._motion_path_checkbox)
        self._measurement_menu_checkbox.addWidget(self._length_checkbox)
        self._measurement_menu_checkbox.addWidget(self._line_checkbox)
        self._measurement_menu_checkbox.addWidget(self._angle_checkbox)
        self._measurement_menu_checkbox.addWidget(self._speed_checkbox)
        self._measurement_menu_checkbox.addWidget(self._performance_checkbox)
        self._measurement_menu_checkbox.addWidget(self._audio_step_checkbox)

        self._measurement_menu_layout.addLayout(self._measurement_menu_combobox)
        self._measurement_menu_layout.addLayout(self._measurement_menu_checkbox)

        self._measurement_menu_group.setLayout(self._measurement_menu_layout)
        self._main_layout.addWidget(self._measurement_menu_group)

        self._measurement_menu_group.setStyleSheet("""font-family:Helvetica;color:black;font-size:20px;""")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    controller = MeasurementMenuController()
    controller.show()
    sys.exit(app.exec_())
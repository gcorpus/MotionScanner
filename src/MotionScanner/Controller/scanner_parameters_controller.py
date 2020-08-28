from PySide2.QtWidgets import *
from PySide2.QtGui import *
from body_button_widget import BodyButtonWidget


class ScannerParametersController(QWidget):

    def __init__(self, parent=None):         
        super(ScannerParametersController, self).__init__(parent)  
        self.SetupUI()


    def SetupUI(self):
        self._main_layout = QVBoxLayout(self)
        self._title_layout = QVBoxLayout()
        self._controls_layout = QHBoxLayout()

        self._controls_group = QGroupBox('Measurement parameters')
        self._main_controls_layout = QVBoxLayout()

        self._length_checkbox = QCheckBox('Length')
        self._angle_checkbox = QCheckBox('Angles')
        self._speed_checkbox = QCheckBox('Speed')
        self._path_checkbox = QCheckBox('Motion path')
        self._metadata_checkbox = QCheckBox('Metadata')
        self._performance_evaluation_checkbox = QCheckBox('Performance evaluation')
        self._audio_steps_checkbox = QCheckBox('Audio steps')

        self._main_controls_layout.addWidget(self._length_checkbox)
        self._main_controls_layout.addWidget(self._angle_checkbox)
        self._main_controls_layout.addWidget(self._speed_checkbox)
        self._main_controls_layout.addWidget(self._path_checkbox)
        self._main_controls_layout.addWidget(self._metadata_checkbox)
        self._main_controls_layout.addWidget(self._performance_evaluation_checkbox)
        self._main_controls_layout.addWidget(self._audio_steps_checkbox)
        self._main_controls_layout.addStretch()

        self._controls_group.setLayout(self._main_controls_layout)

        self._avatar_layout = QVBoxLayout()
        self._avatar_group = QGroupBox()
        self.resizeWidget(self._avatar_group,300,600)
        self._avatar_group.setStyleSheet("""background-image: url(../Lib/human_figure_36.jpg)""")

        self._avatar_vertical_layout = QVBoxLayout()

        # HEAD
        self._head_layout = QHBoxLayout()
        self._head_button = BodyButtonWidget(width=45,height=45)
        self._head_layout.addStretch()
        self._head_layout.addWidget(self._head_button)
        self._head_layout.addStretch()

        # SHOULDERS
        self._sholuder_layout = QHBoxLayout()
        self._left_shoulder_button = BodyButtonWidget(width=45,height=45)
        self._chest_button = BodyButtonWidget(width=45,height=45)
        self._right_shooulder_button = BodyButtonWidget(width=45,height=45)
        self._sholuder_layout.addStretch()
        self._sholuder_layout.addWidget(self._left_shoulder_button)
        self._sholuder_layout.addWidget(self._chest_button)
        self._sholuder_layout.addWidget(self._right_shooulder_button)
        self._sholuder_layout.addStretch()

        # ELBOWS
        self._elbow_layout = QHBoxLayout()
        self._left_elbow_button = BodyButtonWidget()
        self._right_elbow_button = BodyButtonWidget()
        self._elbow_layout.addStretch()
        self._elbow_layout.addWidget(self._left_elbow_button)
        self._elbow_layout.addStretch()
        self._elbow_layout.addWidget(self._right_elbow_button)
        self._elbow_layout.addStretch()

        # WRIST
        self._wrist_layout = QHBoxLayout()
        self._left_wrist_button = BodyButtonWidget()
        self._left_hip_button = BodyButtonWidget()
        self._center_button = BodyButtonWidget()
        self._right_hip_button = BodyButtonWidget()
        self._right_wrist_button = BodyButtonWidget()
        self._wrist_layout.addStretch()
        self._wrist_layout.addWidget(self._left_wrist_button)
        self._wrist_layout.addWidget(self._left_hip_button)
        self._wrist_layout.addWidget(self._center_button)
        self._wrist_layout.addWidget(self._right_hip_button)
        self._wrist_layout.addWidget(self._right_wrist_button)
        self._wrist_layout.addStretch()

        # KNEES
        self._knee_layout = QHBoxLayout()
        self._left_knee_button = BodyButtonWidget()
        self._right_knee_button = BodyButtonWidget()
        self._knee_layout.addStretch()
        self._knee_layout.addWidget(self._left_knee_button)
        self._knee_layout.addWidget(self._right_knee_button)
        self._knee_layout.addStretch()

        # ANKLES
        self._ankle_layout = QHBoxLayout()
        self._left_ankle_button = BodyButtonWidget()
        self._right_ankle_button = BodyButtonWidget()
        self._ankle_layout.addStretch()
        self._ankle_layout.addWidget(self._left_ankle_button)
        self._ankle_layout.addWidget(self._right_ankle_button)
        self._ankle_layout.addStretch()

        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._head_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._sholuder_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._elbow_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._wrist_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._knee_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._ankle_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()

        self._avatar_group.setLayout(self._avatar_vertical_layout)
        self._avatar_layout.addWidget(self._avatar_group)

        self._controls_layout.addWidget(self._controls_group)
        self._controls_layout.addLayout(self._avatar_layout)

        self._main_layout.addLayout(self._title_layout)
        self._main_layout.addLayout(self._controls_layout)


    def resizeWidget(self,widget,width,height):
        widget.setMinimumSize(width,height)
        widget.setMaximumSize(width,height)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = ScannerParametersController()  
    # setup stylesheet
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())
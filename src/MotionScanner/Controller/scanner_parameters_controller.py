from PySide2.QtWidgets import *
from PySide2.QtGui import *
from body_button import BodyButton


class ScannerParametersController(QWidget):

    def __init__(self, parent=None):         
        super(ScannerParametersController, self).__init__(parent)  
        self.SetupUI()
        self.setStyleSheet(open('../Lib/stylesheet.css').read())


    def SetupUI(self):
        self._main_layout = QVBoxLayout(self)
        self._title_layout = QVBoxLayout()
        self._controls_layout = QHBoxLayout()

        self._controls_group = QGroupBox()
        self.resizeWidget(self._controls_group,350,600)
        self._controls_group.setStyleSheet("""background: #757575;""")
        self._main_controls_layout = QVBoxLayout()

        width = 300
        height = 50

        self._measurement_parameters = BodyButton(label='Measurement', width=width, height=height, isParameter=True)
        self._length_parameter = BodyButton(label='Length', width=width, height=height, isParameter=True)
        self._angle_parameter = BodyButton(label='Angles', width=width, height=height, isParameter=True)
        self._speed_parameter = BodyButton(label='Speed', width=width, height=height, isParameter=True)
        self._path_parameter = BodyButton(label='MotionPath', width=width, height=height, isParameter=True)
        self._metadata_parameter = BodyButton(label='Metadata', width=width, height=height, isParameter=True)
        self._performance_evaluation_parameter = BodyButton(label='Performance', width=width, height=height, isParameter=True)
        self._audio_steps_parameter = BodyButton(label='AudioSteps', width=width, height=height, isParameter=True)
        self._aux_button = BodyButton(label='', width=width, height=20, isParameter=True)

        self._main_controls_layout.addWidget(self._measurement_parameters)
        self._main_controls_layout.addWidget(self._aux_button)
        self._main_controls_layout.addWidget(self._length_parameter)
        self._main_controls_layout.addWidget(self._angle_parameter)
        self._main_controls_layout.addWidget(self._speed_parameter)
        self._main_controls_layout.addWidget(self._path_parameter)
        self._main_controls_layout.addWidget(self._metadata_parameter)
        self._main_controls_layout.addWidget(self._performance_evaluation_parameter)
        self._main_controls_layout.addWidget(self._audio_steps_parameter)
        self._main_controls_layout.addStretch()

        self._controls_group.setLayout(self._main_controls_layout)

        self._avatar_layout = QVBoxLayout()
        self._avatar_group = QGroupBox()
        self.resizeWidget(self._avatar_group,300,600)
        self._avatar_group.setStyleSheet("""background-image: url(../Lib/Images/human_figure_36.jpg)""")

        self._avatar_vertical_layout = QVBoxLayout()

        # HEAD
        self._head_layout = QHBoxLayout()
        self._head_button = BodyButton(width=45,height=45)
        self._head_layout.addStretch()
        self._head_layout.addWidget(self._head_button)
        self._head_layout.addStretch()

        # SHOULDERS
        self._sholuder_layout = QHBoxLayout()
        self._left_shoulder_button = BodyButton(width=45,height=45)
        self._chest_button = BodyButton(width=45,height=45)
        self._right_shooulder_button = BodyButton(width=45,height=45)
        self._sholuder_layout.addStretch()
        self._sholuder_layout.addWidget(self._left_shoulder_button)
        self._sholuder_layout.addWidget(self._chest_button)
        self._sholuder_layout.addWidget(self._right_shooulder_button)
        self._sholuder_layout.addStretch()

        # ELBOWS
        self._elbow_layout = QHBoxLayout()
        self._left_elbow_button = BodyButton(width=50,height=50)
        self._right_elbow_button = BodyButton(width=50,height=50)
        self._elbow_layout.addStretch()
        self._elbow_layout.addWidget(self._left_elbow_button)
        self._elbow_layout.addStretch()
        self._elbow_layout.addWidget(self._right_elbow_button)
        self._elbow_layout.addStretch()

        # WRIST
        self._wrist_layout = QHBoxLayout()
        self._left_wrist_button = BodyButton()
        self._left_hip_button = BodyButton()
        self._center_button = BodyButton()
        self._right_hip_button = BodyButton()
        self._right_wrist_button = BodyButton()
        self._wrist_layout.addStretch()
        self._wrist_layout.addStretch()
        self._wrist_layout.addWidget(self._left_wrist_button)
        self._wrist_layout.addStretch()
        self._wrist_layout.addWidget(self._left_hip_button)
        self._wrist_layout.addStretch()
        # self._wrist_layout.addWidget(self._center_button)
        self._wrist_layout.addWidget(self._right_hip_button)
        self._wrist_layout.addStretch()
        self._wrist_layout.addWidget(self._right_wrist_button)
        self._wrist_layout.addStretch()
        self._wrist_layout.addStretch()

        # KNEES
        self._knee_layout = QHBoxLayout()
        self._left_knee_button = BodyButton()
        self._right_knee_button = BodyButton()
        self._knee_layout.addStretch()
        self._knee_layout.addWidget(self._left_knee_button)
        self._knee_layout.addWidget(self._right_knee_button)
        self._knee_layout.addStretch()

        # ANKLES
        self._ankle_layout = QHBoxLayout()
        self._left_ankle_button = BodyButton()
        self._right_ankle_button = BodyButton()
        self._ankle_layout.addStretch()
        self._ankle_layout.addWidget(self._left_ankle_button)
        self._ankle_layout.addWidget(self._right_ankle_button)
        self._ankle_layout.addStretch()

        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._head_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._sholuder_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._elbow_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._wrist_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._knee_layout)
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addStretch()
        self._avatar_vertical_layout.addLayout(self._ankle_layout)
        self._avatar_vertical_layout.addStretch()
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
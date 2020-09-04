from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from MotionScanner.Controller import BodyButton
from MotionScanner.Controller import BodyButton


class AvatarController(QWidget):

    def __init__(self, parent=None):
        super(AvatarController, self).__init__(parent)
        self._setupUI()
        self.setStyleSheet(open('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/stylesheet.css').read())

    @property
    def Head(self):
        return self._head_button

    @property
    def LeftShoulder(self):
        return self._left_shoulder_button

    @property
    def RightShouler(self):
        return self._right_shoulder_button

    @property
    def Chest(self):
        return self._chest_button

    @property
    def LeftElbow(self):
        return self._left_elbow_button

    @property
    def RightElbow(self):
        return self._right_elbow_button

    @property
    def LeftWrist(self):
        return self._left_wrist_button

    @property
    def RightWrist(self):
        return self._right_wrist_button

    @property
    def Center(self):
        return self._center_button

    @property
    def LeftHip(self):
        return self._left_hip_button

    @property
    def RightHip(self):
        return self._right_hip_button

    @property
    def LeftKnee(self):
        return self._left_knee_button

    @property
    def RightKnee(self):
        return self._right_knee_button

    @property
    def LeftAnkle(self):
        return self._left_ankle_button

    @property
    def RightAnkle(self):
        return self._right_ankle_button

    def _setupUI(self):
        self._main_layout = QVBoxLayout(self)
        self._avatar_layout = QVBoxLayout()

        self._avatar_group = QGroupBox()
        self.resizeWidget(self._avatar_group,300,600)
        self._avatar_group.setStyleSheet("""background-image: url(D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/human_figure_36.jpg)""")

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
        self._right_shoulder_button = BodyButton(width=45,height=45)
        self._sholuder_layout.addStretch()
        self._sholuder_layout.addWidget(self._left_shoulder_button)
        self._sholuder_layout.addWidget(self._chest_button)
        self._sholuder_layout.addWidget(self._right_shoulder_button)
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

        self._main_layout.addLayout(self._avatar_layout)

    def resizeWidget(self, widget, width, height):
        widget.setMinimumSize(width, height)
        widget.setMaximumSize(width, height)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    controller = AvatarController()
    controller.show()
    sys.exit(app.exec_())
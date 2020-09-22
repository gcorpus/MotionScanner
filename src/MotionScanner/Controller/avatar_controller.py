from PySide2.QtWidgets import *
# from MotionScanner.Controller import BodyButton
from MotionScanner.Lib import MotionScannerLib


class AvatarController(QWidget):

    def __init__(self, parent=None):
        super(AvatarController, self).__init__(parent)
        self._setupUI()
        self.initialize()
        self.setStyleSheet(open('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/stylesheet.css').read())

    @property
    def Avatar(self):
        return self._avatar_group

    @property
    def JointCombobox(self):
        return self._joint_chunk_combobox

    def _setupUI(self):
        self._main_layout = QVBoxLayout(self)
        self._avatar_layout = QVBoxLayout()

        self._joint_chunk_group = QGroupBox()
        self._joint_chunk_group.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._joint_chunk_layout = QHBoxLayout()
        self._joint_chunk_label = QLabel('Joint chunk:')
        self._joint_chunk_combobox = QComboBox()
        self._joint_chunk_combobox.addItems(['None', 'Head', 'Head-Chest',
                                             'Head-Left-Arm', 'Head-Left-Arm-Hand',
                                             'Head-Right-Arm', 'Head-Right-Arm-Hand',
                                             'Head-Arms', 'Head-Arms-Hands',
                                             'Center', 'Center-Hips',
                                             'Center-Left-Leg', 'Center-Left-Leg-Foot',
                                             'Center-Right-Leg', 'Center-Right-Leg-Foot',
                                             'Center-Legs', 'Center-Legs-Feet',
                                             'Whole-Body',
                                             ''
                                             ])
        self._joint_chunk_layout.addWidget(self._joint_chunk_label)
        self._joint_chunk_layout.addWidget(self._joint_chunk_combobox)
        self._joint_chunk_layout.addStretch()
        self._joint_chunk_group.setLayout(self._joint_chunk_layout)

        self._avatar_group = QGroupBox()
        self.resizeWidget(self._avatar_group, 300, 600)
        self._avatar_group.setStyleSheet("""background-image: url(D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/JointChunks/None.jpg)""")

        self._avatar_vertical_layout = QVBoxLayout()

        # self._avatar_layout.addWidget(self._joint_chunk_group)
        self._avatar_layout.addWidget(self._avatar_group)

        self._main_layout.addLayout(self._avatar_layout)

    def initialize(self):

        self._joint_chunk_combobox.currentIndexChanged.connect(lambda: MotionScannerLib.SetupJointChunkFromCombobox(self))

    def resizeWidget(self, widget, width, height):
        widget.setMinimumSize(width, height)
        widget.setMaximumSize(width, height)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    controller = AvatarController()
    controller.show()
    sys.exit(app.exec_())
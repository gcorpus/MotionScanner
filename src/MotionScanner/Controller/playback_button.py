from PySide2.QtWidgets import *
from PySide2.QtGui import *


class PlaybackButton(QPushButton):

    def __init__(self, name_icon, parent=None):
        super(PlaybackButton, self).__init__(parent)

        self._name_icon = name_icon
        self._icon = QIcon()
        self._function = None
        self.initialize()

    def setFunction(self, function):
        self._function = function

    def initialize(self):
        self.setMinimumHeight(50)
        self._icon.addPixmap(QPixmap('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/{}.png'.format(self._name_icon)))
        self.setIcon(self._icon)
        self.clicked.connect(lambda: self._function())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    controller = PlayButton()
    controller.show()
    sys.exit(app.exec_())






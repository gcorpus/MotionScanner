from PySide2.QtWidgets import *
from PySide2.QtGui import *


class BodyButton(QPushButton):

    def __init__(self, parent=None, label='', width=40, height=40, isActived=False):
        super(BodyButton, self).__init__(parent)

        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)

        self._active_icon = QIcon()
        self._not_active_icon = QIcon()

        self._isActived = isActived
        self._body_part_name = label

        self.setStyleSheet(open('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/stylesheet.css').read())

        self.initialize()

    @property
    def isActived(self):
        return self._isActived

    @isActived.setter
    def isActived(self, value):
        if self._isActived != value:
            self._isActived = value
            self._updateIconStatus()

    @property
    def bodyPartName(self):
        return self._body_part_name

    def initialize(self):

        self._not_active_icon.addPixmap(QPixmap('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/not_active_dot.png'))
        self._active_icon.addPixmap(QPixmap('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/active_dot.png'))
        self.setIcon(self._not_active_icon)

        self.clicked.connect(self._changeStatus)

    def _changeStatus(self):

        if self._isActived:
            self.setIcon(self._not_active_icon)
            self._isActived = False

        else:
            self.setIcon(self._active_icon)
            self._isActived = True

    def _updateIconStatus(self):

        if self._isActived:
            self.setIcon(self._active_icon)

        else:
            self.setIcon(self._not_active_icon)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    controller = BodyButton()
    controller.show()
    sys.exit(app.exec_())






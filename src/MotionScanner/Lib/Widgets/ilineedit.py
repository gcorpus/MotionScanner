from PySide2.QtWidgets import *


class ILineEdit(QWidget):
    def __init__(self, parent=None, label=''):
        super(ILineEdit, self).__init__(parent)

        self._text = label

        self.setupUI()
        # self.initialize()

    @property
    def LineEdit(self):
        return self._lineedit

    def setupUI(self):
        self._layout = QHBoxLayout(self)

        self._label = QLabel('{}:'.format(self._text))
        self._lineedit = QLineEdit()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._lineedit)
        # self._layout.addStretch()
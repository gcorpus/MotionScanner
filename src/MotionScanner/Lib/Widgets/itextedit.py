from PySide2.QtWidgets import *


class ITextEdit(QWidget):
    def __init__(self, parent=None, label=''):
        super(ITextEdit, self).__init__(parent)

        self._text = label
        self.setupUI()

    @property
    def TextEdit(self):
        return self._textedit

    def setupUI(self):
        self._layout = QVBoxLayout(self)

        self._label = QLabel('{}:'.format(self._text))
        self._textedit = QTextEdit()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._textedit)
        self._layout.addStretch()
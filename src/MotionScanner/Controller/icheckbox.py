from PySide2.QtWidgets import *


class ICheckbox(QWidget):
    def __init__(self, parent=None, label=''):
        super(ICheckbox, self).__init__(parent)
        self._text = label
        self.setupUI()
        self.initialize()

    def setupUI(self):
        self._layout = QHBoxLayout(self)

        self._checkbox = QCheckBox()
        self._label = QLabel(self._text)

        self._layout.addWidget(self._checkbox)
        self._layout.addWidget(self._label)
        self._layout.addStretch()

    def initialize(self):
        self._label.setStyleSheet("""font-family:Helvetica;color:black;font-size:20px;""")


if __name__ == '__main__':
    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = ICheckbox(label='Oso')
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

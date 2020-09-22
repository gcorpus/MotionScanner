from PySide2.QtWidgets import *


class ISpinbox(QWidget):
    def __init__(self, parent=None, label='', measure=''):
        super(ISpinbox, self).__init__(parent)

        self._text = label
        self._measure = QLabel(measure)

        self.setupUI()
        self.initialize()

    @property
    def Spinbox(self):
        return self._spinbox

    def setupUI(self):
        self._layout = QHBoxLayout(self)

        self._label = QLabel('{}:'.format(self._text))
        self._spinbox = QDoubleSpinBox()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._spinbox)
        self._layout.addWidget(self._measure)
        self._layout.addStretch()

    def initialize(self):
        self._label.setStyleSheet("""font-family:Helvetica;color:black;font-size:12px;""")

        self._spinbox.setValue(0.0)

        self._spinbox.setMinimum(0.0)
        self._spinbox.setMaximum(200.0)


if __name__ == '__main__':
    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = ISpinbox(label='Oso')
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

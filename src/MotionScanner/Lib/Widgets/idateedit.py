from PySide2.QtWidgets import *


class IDateEdit(QWidget):
    def __init__(self, parent=None, label=''):
        super(IDateEdit, self).__init__(parent)

        self._text = label

        self.setupUI()
        self.initialize()

    @property
    def DateEdit(self):
        return self._dateedit

    def setupUI(self):
        self._layout = QHBoxLayout(self)

        self._label = QLabel('{}:'.format(self._text))
        self._dateedit = QDateEdit()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._dateedit)
        self._layout.addStretch()

    def initialize(self):
        self._label.setStyleSheet("""font-family:Helvetica;color:black;font-size:12px;""")

        self._dateedit.setCalendarPopup(True)
        self._dateedit.setDisplayFormat('dd/MM/yyyy')
        self._dateedit.setFixedWidth(100)


if __name__ == '__main__':
    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = IDateEdit(label='Oso')
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

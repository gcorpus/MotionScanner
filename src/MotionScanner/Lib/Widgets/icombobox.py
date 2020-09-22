from PySide2.QtWidgets import *


class ICombobox(QWidget):
    def __init__(self, parent=None, label='', items=[]):
        super(ICombobox, self).__init__(parent)

        self._text = label
        self._items = items

        self.setupUI()
        self.initialize()

    @property
    def Combobox(self):
        return self._combobox

    def setupUI(self):
        self._layout = QHBoxLayout(self)

        self._label = QLabel('{}:'.format(self._text))
        self._combobox = QComboBox()

        self._layout.addWidget(self._label)
        self._layout.addWidget(self._combobox)
        self._layout.addStretch()

    def initialize(self):
        self._label.setStyleSheet("""font-family:Helvetica;color:black;font-size:12px;""")

        if self._items:
            for item in self._items:
                self._combobox.addItem(item)


if __name__ == '__main__':
    import sys
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create babel
    controller = ICombobox(label='Oso')
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

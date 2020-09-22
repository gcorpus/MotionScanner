from PySide2.QtWidgets import *


class DataLabel(QHBoxLayout):
    def __init__(self, parent=None, name='', data=''):
        super(DataLabel, self).__init__(parent)
        self._name = name
        self._data = data

        self.setupUI()

    def setupUI(self):

        self._name_label = QLabel('{}: '.format(self._name))
        self._data_label = QLabel('{}'.format(self._data))

        self.addWidget(self._name_label)
        self.addWidget(self._data_label)
        self.addStretch()

        self._name_label.setStyleSheet("""font-weight: bold;font-family:Helvetica;font-size:12px;""")
        self._data_label.setStyleSheet("""font-family:Helvetica;font-size:16px;""")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # Create babel
    controller = DataLabel(name='Username', data='Osoblancoso')
    # setup stylesheet
    app.setStyleSheet(open('../stylesheet.css').read())
    #Show babel
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
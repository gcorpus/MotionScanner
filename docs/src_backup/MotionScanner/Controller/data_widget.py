from PySide2.QtWidgets import *
from PySide2.QtGui import *


class DataWidget(QHBoxLayout):
    def __init__(self, parent=None, name='' , data=''):         
        super(DataWidget, self).__init__(parent)  
        self._name = name
        self._data = data

        self.SetupUI()

    def SetupUI(self):

        self._name_label = QLabel('{}: '.format(self._name))
        self._data_label = QLabel('{}'.format(self._data))

        self.addWidget(self._name_label)
        self.addWidget(self._data_label)
        self.addStretch()

        self._name_label.setStyleSheet("""font-weight: bold;""")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = DataWidget(name='Username', data='Osoblancoso')  
    # setup stylesheet
    app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())
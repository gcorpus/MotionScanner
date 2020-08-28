from PySide2.QtWidgets import *
from PySide2.QtGui import *


class BodyButtonWidget(QPushButton):

    def __init__(self, parent=None, label='', width=40, height=40, isActived=False):         
        super(BodyButtonWidget, self).__init__(parent)  

        self.setText(label)
        self.setMinimumSize(width,height)
        self.setMaximumSize(width,height)
        self._isActived = isActived
        
        self.Initialize()
        
    def Initialize(self):

        self._not_actived_icon = QIcon()
        self._not_actived_icon.addPixmap(QPixmap('../Lib/not_actived_dot.png'))

        self._actived_icon = QIcon()
        self._actived_icon.addPixmap(QPixmap('../Lib/actived_dot.png'))

        self.setStyleSheet("""background: transparent;color:black;""")
        self.setIcon(self._not_actived_icon)
        self.clicked.connect(self._ChangeStatus)

    def _ChangeStatus(self):
        
        if self._isActived:
            self.setIcon(self._not_actived_icon)
            self._isActived = False
            
        elif self._isActived == False:
            self.setIcon(self._actived_icon)
            self._isActived = True


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = BodyButtonWidget()  
    # setup stylesheet
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())




        

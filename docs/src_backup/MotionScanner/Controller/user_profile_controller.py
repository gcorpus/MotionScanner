from PySide2.QtWidgets import *
from PySide2.QtGui import *
from .data_widget import DataWidget
import imutils
import cv2


class UserProfileController(QWidget):

    def __init__(self, parent=None, user=None):         
        super(UserProfileController, self).__init__(parent)  
        self._id = user['_id']
        self._username = user['name']
        self._heigth = user['heigth']
        self._weight = user['weight']
        self._roles = user['roles']
        self._disciplines = user['disciplines']
        self._routines = user['routines']

        self.SetupUI()

    def SetupUI(self):
        self.setWindowTitle("User profile")
        self.resize(500,150)

        self._main_layout = QVBoxLayout(self)
        self._sub_main_layout = QHBoxLayout()

        self._data_group = QGroupBox()
        self._data_layout = QVBoxLayout()

        image = cv2.imread('../Lib/Images/profile_image.jpg')
        image = imutils.resize(image, width=150)
        cv2.imwrite('../Lib/Images/profile_image_resize.jpg', image)

        self._profile_image = QPixmap('../Lib/Images/profile_image_resize.jpg')
        self._label_image = QLabel()
        self._label_image.setPixmap(self._profile_image)

        self._user_data = DataWidget(name='Username',data=self._username)
        self._heigth_data = DataWidget(name='Heigth', data=self._heigth)
        self._weight_data = DataWidget(name='Weight', data=self._weight)
        self._role_data = DataWidget(name='Role', data=self._roles)
        self._discipline_data = DataWidget(name='Disciplines', data=self._disciplines)
        self._routine_data = DataWidget(name='Routines', data=self._routines)

        self._data_layout.addLayout(self._user_data)
        self._data_layout.addLayout(self._heigth_data)
        self._data_layout.addLayout(self._weight_data)
        self._data_layout.addLayout(self._role_data)
        self._data_layout.addLayout(self._discipline_data)
        self._data_layout.addLayout(self._routine_data)

        self._data_group.setLayout(self._data_layout)
        self.setStyleSheet("""background-color:#907BA6;font-family:Tahoma;font-size: 14px;""")

        self._sub_main_layout.addWidget(self._label_image)
        self._sub_main_layout.addWidget(self._data_group)

        self._main_layout.addLayout(self._sub_main_layout)

        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = UserProfileController(user={'_id':'2323943','name':'Oso Blanco','heigth':'100 cm', 'weight':'10 kg','roles':['Dancer, Coach'],'disciplines':['Ballet','Fitness'],'routines':['Swan']})  
    # setup stylesheet
    app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())
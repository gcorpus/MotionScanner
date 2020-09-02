from PySide2.QtWidgets import *
from PySide2.QtGui import *
from MotionScanner.Controller import DataWidget
import imutils
import cv2


class UserProfileController(QWidget):

    def __init__(self, parent=None, user=None):
        super(UserProfileController, self).__init__(parent)
        self._id = user['_id']
        self._username = user['name']
        self._height = user['heigth']
        self._weight = user['weight']
        self._roles = user['roles']
        self._disciplines = user['disciplines']
        self._routines = user['routines']

        self.SetupUI()

    def SetupUI(self):
        self.setWindowTitle("User profile")

        self._main_layout = QVBoxLayout(self)

        self._image_data_layout = QHBoxLayout()

        # Create image item
        image = QPixmap('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/profile_image_resize.jpg')
        self._profile_image = QLabel()
        self._profile_image.setPixmap(image)

        self._image_data_layout.addWidget(self._profile_image)

        self._user_data = DataWidget(name='Username', data=self._username)
        self._height_data = DataWidget(name='Height', data=self._height)
        self._weight_data = DataWidget(name='Weight', data=self._weight)

        self._data_one_group = QGroupBox()
        self._data_one_layout = QVBoxLayout()
        self._data_one_layout.addLayout(self._user_data)
        self._data_one_layout.addLayout(self._height_data)
        self._data_one_layout.addLayout(self._weight_data)
        self._data_one_group.setLayout(self._data_one_layout)

        self._image_data_layout.addWidget(self._data_one_group)

        self._role_data = DataWidget(name='Role', data=self._roles)
        self._discipline_data = DataWidget(name='Disciplines', data=self._disciplines)
        self._routine_data = DataWidget(name='Routines', data=self._routines)

        self._data_second_group = QGroupBox()
        self._data_second_layout = QVBoxLayout()
        self._data_second_layout.addLayout(self._role_data)
        self._data_second_layout.addLayout(self._discipline_data)
        self._data_second_layout.addLayout(self._routine_data)
        self._data_second_group.setLayout(self._data_second_layout)

        self._main_layout.addLayout(self._image_data_layout)
        self._main_layout.addWidget(self._data_second_group)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # Create babel
    controller = UserProfileController(
        user={'_id': '2323943', 'name': 'Oso Blanco', 'heigth': '100 cm', 'weight': '10 kg', 'roles': ['Dancer, Coach'],
              'disciplines': ['Ballet', 'Fitness'], 'routines': ['Swan']})
    # setup stylesheet
    app.setStyleSheet(open('../Lib/stylesheet.css').read())
    # Show babel
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

    # self._data_group.setLayout(self._data_layout)
    # self.setStyleSheet("""background-color:#907BA6;font-family:Tahoma;font-size: 16px;""")
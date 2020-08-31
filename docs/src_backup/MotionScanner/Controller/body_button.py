from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from ..Lib.Catalogs.catalog_parameter_label import CatalogParameterLabel


class BodyButton(QPushButton):

    def __init__(self, parent=None, label='', width=40, height=40, isActived=False, isParameter=False):         
        super(BodyButton, self).__init__(parent)  

        self.setText(label)
        self.setMinimumSize(width,height)
        self.setMaximumSize(width,height)
        self.setStyleSheet(open('../Lib/stylesheet.css').read())

        self._isParameter = isParameter
        self._isActived = isActived
        
        self.Initialize()
        
    def Initialize(self):

        if self._isParameter:

            self._active_style = ''
            self._not_active_style = ''

            if self.text() == 'Length':
                self._active_style = """background-image:url('../Lib/Images/length_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/length_not_active.png');border: none;"""

            elif self.text() == 'Angles':
                self._active_style = """background-image:url('../Lib/Images/angle_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/angle_not_active.png');border: none;"""

            elif self.text() == 'Speed':
                self._active_style = """background-image:url('../Lib/Images/speed_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/speed_not_active.png');border: none;"""

            elif self.text() == 'MotionPath':
                self._active_style = """background-image:url('../Lib/Images/motion_path_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/motion_path_not_active.png');border: none;"""

            elif self.text() == 'Metadata':
                self._active_style = """background-image:url('../Lib/Images/metadata_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/metadata_not_active.png');border: none;"""

            elif self.text() == 'Performance':
                self._active_style = """background-image:url('../Lib/Images/performance_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/performance_not_active.png');border: none;"""

            elif self.text() == 'AudioSteps':
                self._active_style = """background-image:url('../Lib/Images/audio_steps_active.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/audio_steps_not_active.png');border: none;"""

            elif self.text() == 'Measurement':
                self._active_style = """background-image:url('../Lib/Images/measurement_parameters_label.png');border: none;"""
                self._not_active_style = """background-image:url('../Lib/Images/measurement_parameters_label.png');border: none;"""

            else:
                self._active_style = """border: none;"""
                self._not_active_style = """border: none;"""

            self.setText('')
            self.setStyleSheet(self._not_active_style)

        else:
            self._active_icon = QIcon()
            self._not_active_icon = QIcon()
            self._not_active_icon.addPixmap(QPixmap('../Lib/Images/not_active_dot.png'))
            self._active_icon.addPixmap(QPixmap('../Lib/Images/active_dot.png'))
            self.setIcon(self._not_active_icon)

        self.clicked.connect(self._ChangeStatus)

    def _ChangeStatus(self):

        if self._isParameter:

            if self._isActived:
                self.setStyleSheet(self._not_active_style)
                self._isActived = False
                
            elif self._isActived == False:
                self.setStyleSheet(self._active_style)
                self._isActived = True

        else:
        
            if self._isActived:
                self.setIcon(self._not_active_icon)
                self._isActived = False
                
            elif self._isActived == False:
                self.setIcon(self._active_icon)
                self._isActived = True


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)     
    # Create babel  
    controller = BodyButton()  
    # setup stylesheet
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()     
    # Run the main Qt loop     
    sys.exit(app.exec_())




        

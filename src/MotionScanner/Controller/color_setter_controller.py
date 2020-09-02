from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import cv2
import numpy
from MotionScanner.Controller import WebCamController
from MotionScanner.Controller import SliderControlWidget
# from web_cam_controller import WebCamController
# from slider_control_widget import SliderControlWidget



class ColorSetterController(QDialog):

    def __init__(self, parent=None):
        super(ColorSetterController, self).__init__(parent)
        self._setupUI()
        self._initialize()

    def _setupUI(self):
        self.setWindowTitle("Color setter")
        self._main_layout = QVBoxLayout(self)

        self._content_layout = QHBoxLayout()

        self._video_canvas_group = QGroupBox('Canvas in binary')
        self._video_canvas_group.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._video_canvas_layout = QVBoxLayout()
        self._video_canvas_widget = WebCamController(width=640, height=480)
        self._video_canvas_layout.addWidget(self._video_canvas_widget)
        self._video_canvas_group.setLayout(self._video_canvas_layout)

        self._slider_control_group = QGroupBox('Color markers controls - HSV')
        self._slider_control_group.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._slider_control_layout = QVBoxLayout()

        self._hue_widget = SliderControlWidget(name='HUE', range=(0,179))
        self._saturation_widget = SliderControlWidget(name='SATURATION', range=(0, 255))
        self._value_widget = SliderControlWidget(name='VALUE', range=(0, 255))

        self._apply_button = QPushButton('Apply')
        self._apply_button.setMinimumHeight(50)

        self._slider_control_layout.addWidget(self._hue_widget)
        self._slider_control_layout.addWidget(self._saturation_widget)
        self._slider_control_layout.addWidget(self._value_widget)
        self._slider_control_layout.addStretch()
        self._slider_control_layout.addWidget(self._apply_button)

        self._slider_control_group.setLayout(self._slider_control_layout)

        self._content_layout.addWidget(self._video_canvas_group)
        self._content_layout.addWidget(self._slider_control_group)

        self._main_layout.addLayout(self._content_layout)

    def _initialize(self):
        self._video_canvas_widget.StartVideoScanner(type_='BINARY',
                                                    hue=self._hue_widget,
                                                    saturation=self._saturation_widget,
                                                    value=self._value_widget)

    def Show(self):
        self.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = ColorSetterController()
    win.show()
    sys.exit(app.exec_())
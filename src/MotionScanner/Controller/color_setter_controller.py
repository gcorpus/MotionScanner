from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import cv2
import numpy
from MotionScanner.Controller import WebCamController
from MotionScanner.Controller import SliderControlWidget



class ColorSetterController(QDialog):

    def __init__(self, motion_scanner_controller,parent=None):
        super(ColorSetterController, self).__init__(parent)
        self._motion_scanner_controller = motion_scanner_controller
        self._setupUI()
        self._initialize()

    def _setupUI(self):
        self.setWindowTitle("Color setter")
        self._main_layout = QVBoxLayout(self)

        self._content_layout = QHBoxLayout()

        self._video_canvas_group = QGroupBox('Canvas in binary')
        self._video_canvas_group.setStyleSheet("""font-family:Helvetica;font-size:16px;""")
        self._video_canvas_layout = QVBoxLayout()
        self._video_canvas_widget = WebCamController(type_='BINARY', width=640, height=480)
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
        self._video_canvas_widget.startVideoScanner(hue_widget=self._hue_widget,
                                                    saturation_widget=self._saturation_widget,
                                                    value_widget=self._value_widget)

        self._apply_button.clicked.connect(self._setHSVValues)

    def _setHSVValues(self):
        self._motion_scanner_controller.setLowHue(self._hue_widget.getLowValue())
        self._motion_scanner_controller.setHighHue(self._hue_widget.getHighValue())
        self._motion_scanner_controller.setLowSaturation(self._saturation_widget.getLowValue())
        self._motion_scanner_controller.setHighSaturation(self._saturation_widget.getHighValue())
        self._motion_scanner_controller.setLowValue(self._value_widget.getLowValue())
        self._motion_scanner_controller.setHighValue(self._value_widget.getHighValue())

        self.Close()

    def Show(self):
        self.exec_()

    def Close(self):
        self._video_canvas_widget.stopVideoStream()
        self.close()

    def closeEvent(self, event):
        self._video_canvas_widget.stopVideoStream()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = ColorSetterController()
    win.show()
    sys.exit(app.exec_())
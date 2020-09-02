from PySide2.QtWidgets import *
from PySide2.QtCore import *


class SliderControlWidget(QWidget):
    def __init__(self, name, range, parent=None):
        super(SliderControlWidget, self).__init__(parent)

        self._name = name
        self._range = range

        self._font_style = """font-family:Helvetica;font-size:14px;"""

        self.setupUI()
        self.initialize()

    def setupUI(self):

        self._main_layout = QVBoxLayout(self)

        self._name_label = QLabel(self._name)

        self._controls_layout = QHBoxLayout()
        self._low_control_layout = QVBoxLayout()
        self._low_slider_layout = QHBoxLayout()
        self._high_control_layout = QVBoxLayout()
        self._high_slider_layout = QHBoxLayout()

        self._low_label = QLabel('Low')
        self._low_value_label = QLabel('0')
        self._low_slider = QSlider(Qt.Horizontal)
        self._low_slider.setMinimum(self._range[0])
        self._low_slider.setMaximum(self._range[1])
        self._low_slider.setValue(self._range[0])

        self._high_label = QLabel('High')
        self._high_value_label = QLabel('0')
        self._high_slider = QSlider(Qt.Horizontal)
        self._high_slider.setMinimum(self._range[0])
        self._high_slider.setMaximum(self._range[1])
        self._high_slider.setValue(self._range[1])

        self._low_control_layout.addWidget(self._low_label)
        self._low_slider_layout.addWidget(self._low_slider)
        self._low_slider_layout.addWidget(self._low_value_label)
        self._low_control_layout.addLayout(self._low_slider_layout)

        self._high_control_layout.addWidget(self._high_label)
        self._high_slider_layout.addWidget(self._high_slider)
        self._high_slider_layout.addWidget(self._high_value_label)
        self._high_control_layout.addLayout(self._high_slider_layout)

        self._controls_layout.addLayout(self._low_control_layout)
        self._controls_layout.addStretch()
        self._controls_layout.addLayout(self._high_control_layout)

        self._main_layout.addWidget(self._name_label)
        self._main_layout.addLayout(self._controls_layout)

    def initialize(self):
        self.updateValues()
        self._low_slider.valueChanged.connect(self.updateValues)
        self._high_slider.valueChanged.connect(self.updateValues)

        # Labels font styles
        self._low_value_label.setStyleSheet(self._font_style)
        self._high_value_label.setStyleSheet(self._font_style)
        self._low_label.setStyleSheet(self._font_style)
        self._high_label.setStyleSheet(self._font_style)
        self._name_label.setStyleSheet("""font-family:Helvetica;font-size:14px;font-weight: bold;""")

    def updateValues(self):
        self._low_value_label.setText(str(self._low_slider.value()))
        self._high_value_label.setText(str(self._high_slider.value()))

    def getLowValue(self):
        return self._low_slider.value()

    def getHighValue(self):
        return self._high_slider.value()


        # self._name_label.setStyleSheet("""font-weight: bold;font-family:Helvetica;font-size:12px;""")
        # self._data_label.setStyleSheet("""font-family:Helvetica;font-size:16px;""")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # Create babel
    controller = SliderControlWidget(name='SATURATION', range=(0, 255))
    # setup stylesheet
    # app.setStyleSheet(open('../Lib/stylesheet.css').read())
    #Show babel
    controller.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
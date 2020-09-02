from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import cv2
import numpy


class WebCamController(QWidget):

    def __init__(self, width, height):
        QWidget.__init__(self)
        self._type = type
        self._size = QSize(width, height)
        self._capture = None

        self._setupUI()
        self._cleanVideoCanvas()

    def _setupUI(self):
        self._frame_label = QLabel()
        self._frame_label.setFixedSize(self._size)

        self._main_layout = QVBoxLayout(self)
        self._main_layout.addWidget(self._frame_label)

    def _setupCamera(self, display):
        self._capture = cv2.VideoCapture(0)
        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, self._size.width())
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self._size.height())

        self._timer = QTimer()
        self._timer.timeout.connect(display)
        self._timer.start(30)

    def _displayVideoStream(self):
        _, frame = self._capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)

        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _displayBinaryVideoStream(self, hue, saturation, value):
        retval, frame = self._capture.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if retval:
            frame = cv2.flip(frame, 1)

            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lower_range = numpy.array([hue.getLowValue(), saturation.getLowValue(), value.getLowValue()])
            high_range = numpy.array([hue.getHighValue(), saturation.getHighValue(), value.getHighValue()])

            mask = cv2.inRange(frame_hsv, lower_range, high_range)
            mask = cv2.erode(mask, None, iterations=1)
            mask = cv2.dilate(mask, None, iterations=2)
            mask = cv2.medianBlur(mask, 13)

            mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

            frame = mask_bgr

            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)

            self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _cleanVideoCanvas(self):
        frame = cv2.imread('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/canvas_169.jpg')
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def StopVideoStream(self):
        if self._capture:
            self._capture.release()
            self._cleanVideoCanvas()

    def StartVideoScanner(self, type_, hue=None, saturation=None, value=None):

        if type_ == 'RGB':
            self._setupCamera(self._displayVideoStream)

        elif type_ == 'BINARY':
            self._setupCamera(lambda :self._displayBinaryVideoStream(hue=hue,
                                                                     saturation=saturation,
                                                                     value=value))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = WebCamController()
    win.show()
    sys.exit(app.exec_())
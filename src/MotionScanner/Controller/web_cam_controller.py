from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import cv2
import numpy
from MotionScanner.Lib import MotionScannerLib


class WebCamController(QWidget):

    def __init__(self, type_, width, height):
        QWidget.__init__(self)
        self._type = type_
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

        success, frame = self._capture.read()
        if success:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)

            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)

        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _displayBinaryVideoStream(self, hue, saturation, value):

        success, frame = self._capture.read()

        if success:
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

    def _displayColorRangeVideoStream(self, low_hue=0, high_hue=179, low_saturation=0, high_saturation=255, low_value=0, high_value=255):

        color_low = numpy.array([low_hue, low_saturation, low_value], numpy.uint8)
        color_high = numpy.array([high_hue, high_saturation, high_value], numpy.uint8)

        success, frame = self._capture.read()

        if success:

            frame = cv2.flip(frame, 1)
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(frame_HSV, color_low, color_high)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                area = cv2.contourArea(c)

                if area > 2000:
                    M = cv2.moments(c)
                    if (M['m00'] == 0): M['m00'] = 1
                    x = int(M['m10'] / M['m00'])
                    y = int(M['m01'] / M['m00'])
                    cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
                    new_contour = cv2.convexHull(c)
                    cv2.drawContours(frame, [new_contour], 0, (255, 0, 0), 3)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)

            self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _cleanVideoCanvas(self):

        frame = cv2.imread('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/canvas_169.jpg')
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def stopVideoStream(self):

        if self._capture:
            self._capture.release()
            self._cleanVideoCanvas()

    def startVideoScanner(self, hue_widget=None, saturation_widget=None, value_widget=None,
                          low_hue=0, high_hue=179, low_saturation=0, high_saturation=255, low_value=0, high_value=255):

        if self._type == 'RGB':
            self._setupCamera(self._displayVideoStream)

        elif self._type == 'BINARY':
            self._setupCamera(lambda: self._displayBinaryVideoStream(hue=hue_widget,
                                                                     saturation=saturation_widget,
                                                                     value=value_widget))

        elif self._type == 'COLOR_RANGE':
            self._setupCamera(lambda: self._displayColorRangeVideoStream(low_hue=low_hue,
                                                                         high_hue=high_hue,
                                                                         low_saturation=low_saturation,
                                                                         high_saturation=high_saturation,
                                                                         low_value=low_value,
                                                                         high_value=high_value))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = WebCamController()
    win.show()
    sys.exit(app.exec_())
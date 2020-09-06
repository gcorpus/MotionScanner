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

        # Scanner viewer attributes
        self._color_low = None
        self._color_high = None
        self._measure_widget = None
        self._avatar_widget = None

        # Motion path attributes
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._alpha_screen = None

        self._setupUI()
        self._cleanVideoCanvas()

    @property
    def MeasureWidget(self):
        return self._measure_widget

    @MeasureWidget.setter
    def MeasureWidget(self, widget):
        self._measure_widget = widget

    @property
    def AvatarWidget(self):
        return self._avatar_widget

    @AvatarWidget.setter
    def AvatarWidget(self, widget):
        self._avatar_widget = widget

    @property
    def ColorLow(self):
        return self._color_low

    @ColorLow.setter
    def ColorLow(self, array):
        self._color_low = numpy.array(array, numpy.uint8)

    @property
    def ColorHigh(self):
        return self._color_high

    @ColorHigh.setter
    def ColorHigh(self, array):
        self._color_high = numpy.array(array, numpy.uint8)

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

    def _setupCameraColorPath(self):

        self._capture = cv2.VideoCapture(0)
        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, self._size.width())
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self._size.height())

        self._timer = QTimer()
        self._timer.timeout.connect(self._displayColorPathVideoStream)
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

    def _displayColorRangeVideoStream(self):

        # Catching current frame and your success value (boolean).
        success, frame = self._capture.read()

        # If frame catching was succeed.
        if success:

            # Flip frame
            frame = cv2.flip(frame, 1)
            # Converting original frame to HSV frame.
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # Creating a mask frame with color range data given.
            mask = cv2.inRange(frame_HSV, self._color_low, self._color_high)
            # Exploring mask frame looking for contours of color range given.
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # For each contour of contours found.
            for c in contours:
                # Catching area data of contour.
                area = cv2.contourArea(c)

                # If area value is greater than 2000
                if area > 2000:

                    # Find center point of contour --
                    M = cv2.moments(c)

                    if (M['m00'] == 0):
                        M['m00'] = 1

                    x = int(M['m10'] / M['m00'])
                    y = int(M['m01'] / M['m00'])
                    # Find center point of contour --

                    # Draw a circle int centre point of contour.
                    cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                    # Define a font type.
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    # Draw text of coordinates x,y, where centre point is.
                    cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

            # Invert color system of frame of BGR to RGB.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Submitting resulting frame to QImage object for convert to image.
            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)

            # Setting resulting current frame to final displayer.
            self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _displayColorPathVideoStream(self):

        success, frame = self._capture.read()

        if success:

            # MOTION-PATH ::
            if self._alpha_screen is None:
                self._alpha_screen = numpy.zeros(frame.shape, dtype=numpy.uint8)

            frame, contours = MotionScannerLib.SetupFrameAndContours(frame, self._color_low, self._color_high)

            for c in contours:

                self._x1, self._y1, frame = MotionScannerLib.FindCenterPointOfContour(c, frame)

                frame = MotionScannerLib.RenameDetectedPoints(self._avatar_widget, frame, self._x1, self._y1)

                self._alpha_screen, self._x1, self._y1, self._x2, self._y2 = MotionScannerLib.AnalizeMeasureParameters(
                                                                                                self._measure_widget, self._alpha_screen,
                                                                                                self._x1, self._y1, self._x2, self._y2)

            if self._measure_widget.isMotionPath:
                # Merge frames
                frame = MotionScannerLib.MergeAlphaScreenToFrame(self._alpha_screen, frame)

            # Invert color system of frame of BGR to RGB.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert frame to QImage
            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)
            # Set result frame
            self._frame_label.setPixmap(QPixmap.fromImage(image))

    def _cleanVideoCanvas(self):

        self._alpha_screen = None

        frame = cv2.imread('D:/Greek/Documentos/GreekosoLab/MotionScanner/src/MotionScanner/Lib/Images/canvas_169.jpg')
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self._frame_label.setPixmap(QPixmap.fromImage(image))

    def stopVideoStream(self):

        if self._capture:
            self._capture.release()
            self._cleanVideoCanvas()

    def startVideoScanner(self, hue_widget=None, saturation_widget=None, value_widget=None):

        if self._type == 'RGB':
            self._setupCamera(self._displayVideoStream)

        elif self._type == 'BINARY':
            self._setupCamera(lambda: self._displayBinaryVideoStream(hue=hue_widget,
                                                                     saturation=saturation_widget,
                                                                     value=value_widget))

        elif self._type == 'COLOR_RANGE':
            self._setupCamera(self._displayColorRangeVideoStream)

        elif self._type == 'COLOR_PATH':
            self._setupCamera(self._displayColorPathVideoStream)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = WebCamController()
    win.show()
    sys.exit(app.exec_())
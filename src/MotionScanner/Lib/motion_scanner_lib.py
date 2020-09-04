import cv2
import numpy
from PySide2.QtGui import *



class MotionScannerLib(object):

    @staticmethod
    def displayRGBVideoStream(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)

        return image

    @staticmethod
    def displayBinaryVideoStream(frame, hue, saturation, value):
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
        return image

    @staticmethod
    def displarColorRangeVideoStream(frame, color_low, color_high):

        frame = cv2.flip(frame, 1)
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_HSV, color_low, color_high)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            area = cv2.contourArea(c)

            if area > 3000:
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

        return image

    @staticmethod
    def GetRealTimeWebCamVideo():
        capture = cv2.VideoCapture(0)
        capture.set(3, 1280)
        capture.set(4, 720)

        while True:

            success, frame = capture.read()
            frame = cv2.flip(frame, 1)

            cv2.imshow('Real-time Scanner', frame)
            print(frame.shape)

            key = cv2.waitKey(1)

            if key == 27:
                break

        capture.release()
        cv2.destroyAllWindows()


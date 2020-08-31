from PySide2.QtWidgets import *
import cv2
import numpy

class MotionScannerLib(object):

    @staticmethod
    def GetRealTimeWebCamVideo():
        capture = cv2.VideoCapture(0)
        capture.set(3, 1280)
        capture.set(4, 720)

        while True:

            success, frame = capture.read()
            frame = cv2.flip(frame, 1)

            cv2.imshow('Webcam Canvas', frame)
            print(frame.shape)

            key = cv2.waitKey(1)

            if key == 27 or canvas_combobox.currentIndex() != 4:
                break

        capture.release()
        cv2.destroyAllWindows()

        canvas_combobox.setCurrentIndex(0)

import cv2


class MotionScannerLib(object):

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


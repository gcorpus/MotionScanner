import cv2
import numpy
from PySide2.QtGui import *


class MotionScannerLib(object):

    @staticmethod
    def SetupFrameAndContours(frame, color_low, color_high):

        frame = cv2.flip(frame, 1)

        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_HSV, color_low, color_high)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        contours = MotionScannerLib.ValidContours(contours)

        return frame, contours

    @staticmethod
    def ValidContours(contours):

        valid_contours = []

        for c in contours:
            area = cv2.contourArea(c)

            if area > 3000:
                valid_contours.append(c)

        return valid_contours

    @staticmethod
    def FindCenterPointOfContour(contour, frame):

        M = cv2.moments(contour)

        if (M['m00'] == 0):
            M['m00'] = 1

        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

        # Draw a circle int centre point of contour.
        cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)

        return x, y, frame

    @staticmethod
    def RenameDetectedPoints(avatar, frame, x, y):

        # Define a font type.
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Draw text of coordinates x,y, where centre point is.
        if avatar.Head.isActived:
            cv2.putText(frame, '{}'.format(avatar.Head.bodyPartName), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

        return frame

    @staticmethod
    def AnalizeMeasureParameters(measures, alpha_screen, x1, y1, x2, y2):

        # If PATH parameter is actived.
        if measures.isMotionPath:

            # Speculating.. if x1 and x2 have value.
            if x1 and x2:
                alpha_screen = cv2.line(alpha_screen, (x1, y1), (x2, y2), (91, 43, 132), 5)
            elif x1:
                alpha_screen = cv2.line(alpha_screen, (x1, y1), (x1, y1), (91, 43, 132), 5)

            # Set new values
            x2 = x1
            y2 = y1

        else:
            x1 = None
            y1 = None
            x2 = None
            y2 = None

        return alpha_screen, x1, y1, x2, y2

    @staticmethod
    def MergeAlphaScreenToFrame(alpha_screen, frame):

        # Merge original frame and drawn alpha frame.
        alpha_screen_gray = cv2.cvtColor(alpha_screen, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(alpha_screen_gray, 10, 255, cv2.THRESH_BINARY)
        thInv = cv2.bitwise_not(th)
        frame = cv2.bitwise_and(frame, frame, mask=thInv)
        frame = cv2.add(frame, alpha_screen)

        return frame

    @staticmethod
    def AnalyzeJointChunk(avatar_widget):
        # JOINT CHUNKS

        # None
        if not avatar_widget.Head.isActived and \
            not avatar_widget.LeftShoulder.isActived and not avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
            not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
            not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
            not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
            not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(0)

        # Head
        elif avatar_widget.Head.isActived and \
            not avatar_widget.LeftShoulder.isActived and not avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
            not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
            not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
            not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
            not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(1)

        # Head-Chest
        elif avatar_widget.Head.isActived and \
            avatar_widget.LeftShoulder.isActived and avatar_widget.Chest.isActived and avatar_widget.RightShoulder.isActived and \
            not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
            not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
            not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
            not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(2)

        # Head-LeftArm
        elif avatar_widget.Head.isActived and \
             avatar_widget.LeftShoulder.isActived and avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
             avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
             avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
             not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
             not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(3)

        # Head-RightArm
        elif avatar_widget.Head.isActived and \
             not avatar_widget.LeftShoulder.isActived and avatar_widget.Chest.isActived and avatar_widget.RightShoulder.isActived and \
             not avatar_widget.LeftElbow.isActived and avatar_widget.RightElbow.isActived and \
             not avatar_widget.LeftWrist.isActived and avatar_widget.RightWrist.isActived and \
             not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
             not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(4)

        # Head-Arms
        elif avatar_widget.Head.isActived and \
             avatar_widget.LeftShoulder.isActived and avatar_widget.Chest.isActived and avatar_widget.RightShoulder.isActived and \
             avatar_widget.LeftElbow.isActived and avatar_widget.RightElbow.isActived and \
             avatar_widget.LeftWrist.isActived and avatar_widget.RightWrist.isActived and \
             not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
             not avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(5)

        # Head-LeftLeg
        elif avatar_widget.Head.isActived and \
             not avatar_widget.LeftShoulder.isActived and not avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
             not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
             not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
             avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and not avatar_widget.RightHip.isActived and \
             avatar_widget.LeftKnee.isActived and not avatar_widget.RightKnee.isActived and \
             avatar_widget.LeftAnkle.isActived and not avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(6)

        # Head-RightLeg
        elif avatar_widget.Head.isActived and \
             not avatar_widget.LeftShoulder.isActived and not avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
             not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
             not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
             not avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and avatar_widget.RightHip.isActived and \
             not avatar_widget.LeftKnee.isActived and avatar_widget.RightKnee.isActived and \
             not avatar_widget.LeftAnkle.isActived and avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(7)

        # Head-Legs
        elif avatar_widget.Head.isActived and \
             not avatar_widget.LeftShoulder.isActived and not avatar_widget.Chest.isActived and not avatar_widget.RightShoulder.isActived and \
             not avatar_widget.LeftElbow.isActived and not avatar_widget.RightElbow.isActived and \
             not avatar_widget.LeftWrist.isActived and not avatar_widget.RightWrist.isActived and \
             avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and avatar_widget.RightHip.isActived and \
             avatar_widget.LeftKnee.isActived and avatar_widget.RightKnee.isActived and \
             avatar_widget.LeftAnkle.isActived and avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(8)

        # Body
        elif avatar_widget.Head.isActived and \
             avatar_widget.LeftShoulder.isActived and avatar_widget.Chest.isActived and avatar_widget.RightShoulder.isActived and \
             avatar_widget.LeftElbow.isActived and avatar_widget.RightElbow.isActived and \
             avatar_widget.LeftWrist.isActived and avatar_widget.RightWrist.isActived and \
             avatar_widget.LeftHip.isActived and not avatar_widget.Center.isActived and avatar_widget.RightHip.isActived and \
             avatar_widget.LeftKnee.isActived and avatar_widget.RightKnee.isActived and \
             avatar_widget.LeftAnkle.isActived and avatar_widget.RightAnkle.isActived:

            avatar_widget._joint_chunk_combobox.setCurrentIndex(9)

        else:
            avatar_widget._joint_chunk_combobox.setCurrentIndex(10)


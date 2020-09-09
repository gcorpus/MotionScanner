import cv2
import numpy
from PySide2.QtGui import *


class MotionScannerLib(object):

    @staticmethod
    def SetupFrameAndContours(frame, color_low, color_high, avatar_widget, contours_data, setup_counter, prev_frame, prev_points, lk_parameters, contours_points):

        frame = cv2.flip(frame, 1)

        # if setup_counter < 150:

        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_HSV, color_low, color_high)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        contours = MotionScannerLib.ValidContours(contours)
        contours_data = MotionScannerLib.IdentifyBodyJoints(contours, avatar_widget)
        frame = MotionScannerLib.RenamePoints(contours_data, frame)

        if contours_data:
            if contours_data[0][3]:
                setup_counter += 1

        # else:
        #     print('READY')
        #     # for c in contours_data:
        #     #     print('X=', c[1], 'Y= ', c[2])
        #     if not prev_points.any():
        #         opticalflow_points = []
        #         for c in contours_points:
        #             print('Final coordinates: ', c[1], c[2])
        #             opticalflow_points.extend(c[1])
        #
        #         print('Optical flow points: ', opticalflow_points)
        #
        #         prev_points = numpy.array(opticalflow_points, dtype=numpy.float32)
        #
        #
        #
        #     current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #     current_points, status, error = cv2.calcOpticalFlowPyrLK(prev_frame, current_frame, prev_points, None, **lk_parameters)
        #     prev_frame = current_frame.copy()
        #     prev_points = current_points
        #
        #     for p in current_points:
        #         x = p[0]
        #         y = p[1]
        #         cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)

        return frame, contours_data, setup_counter, prev_frame, prev_points

    @staticmethod
    def ValidContours(contours):

        valid_contours = []

        for c in contours:
            area = cv2.contourArea(c)

            if area > 3000:
                valid_contours.append(c)

        return valid_contours

    @staticmethod
    def IdentifyBodyJoints(contours, avatar_widget):

        contours_data = MotionScannerLib.FindCenterPointAndPositionOfContour(contours)

        # Head chunk
        if avatar_widget.JointCombobox.currentIndex() == 1:
            if len(contours_data) == 1:
                contours_data[0][3] = 'Head'

        # Head-Chest chunk
        elif avatar_widget.JointCombobox.currentIndex() == 2:
            if len(contours) == 4:
                contours_data = MotionScannerLib.AnalyzePointsData(2, contours_data)

        # Head_LeftArm chunk
        elif avatar_widget.JointCombobox.currentIndex() == 3:
            if len(contours) == 5:
                contours_data = MotionScannerLib.AnalyzePointsData(3, contours_data)

        return contours_data

    @staticmethod
    def FindCenterPointAndPositionOfContour(contours):

        contours_data = []

        for c in contours:

            M = cv2.moments(c)

            if (M['m00'] == 0):
                M['m00'] = 1

            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

            contours_data.append([c, x, y, ''])

        return contours_data

    @staticmethod
    def RenamePoints(contours_data, frame):

        # Define a font type.
        font = cv2.FONT_HERSHEY_SIMPLEX

        for c in contours_data:

            x = c[1]
            y = c[2]

            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
            cv2.putText(frame, '{}'.format(c[3]), (x + 10, y), font, 0.75, (0, 0, 0), 1, cv2.LINE_AA)

        return frame

    @staticmethod
    def AnalyzePointsData(index, contours_data):

        print ('Index', index)
        x_array = []
        y_array = []

        if index == 2:

            for c in contours_data:
                x_array.append(c[1])
                y_array.append(c[2])

            x_less = min(x_array)
            x_greater = max(x_array)
            y_less = min(y_array)

            for c in contours_data:
                if c[1] == x_less:
                    c[3] = 'Left shoulder'

                if c[1] == x_greater:
                    c[3] = 'Right sholuder'

                if c[2] == y_less:
                    c[3] = 'Head'

                if c[3] == '':
                    c[3] = 'Chest'

        elif index == 3:

            joints = []

            for c in contours_data:
                joints.append([c[1], c[2]])

            joints.sort()

            joints_head = joints[-2:]
            joints_arm = joints[:3]

            data = []

            for j in joints_head:
                y_array.append(j[1])

            y_less = min(y_array)

            for j in joints_head:
                if j[1] == y_less:
                    data.append([j[0], j[1], 'Head'])
                else:
                    data.append([j[0], j[1], 'Chest'])

            for j in joints_arm:
                x_array.append(j[0])

            x_less = min(x_array)
            x_greater = max(x_array)

            for j in joints_arm:
                if j[0] == x_less:
                    data.append([j[0], j[1], 'Left wrist'])
                elif j[0] == x_greater:
                    data.append([j[0], j[1], 'Left shoulder'])
                else:
                    data.append([j[0], j[1], 'Left elbow'])

            for c in contours_data:
                if c[1] == data[0][0] and c[2] == data[0][1]:
                    c[3] = data[0][2]
                elif c[1] == data[1][0] and c[2] == data[1][1]:
                    c[3] = data[1][2]
                elif c[1] == data[2][0] and c[2] == data[2][1]:
                    c[3] = data[2][2]
                elif c[1] == data[3][0] and c[2] == data[3][1]:
                    c[3] = data[3][2]
                elif c[1] == data[4][0] and c[2] == data[4][1]:
                    c[3] = data[4][2]

        return contours_data

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
    def SetupJointChunkFromAvatar(avatar_widget):
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

    @staticmethod
    def SetupJointChunkFromCombobox(avatar_widget):
        print('combobox')
        print('Index',avatar_widget._joint_chunk_combobox.currentIndex())

        if avatar_widget._joint_chunk_combobox.currentIndex() == 0:


            avatar_widget.Head.isActived = False

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = False
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 1:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = False
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 2:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = True
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = True

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 3:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = True
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = True
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = True
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 4:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = True

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = True

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = True

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 5:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = True
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = True

            avatar_widget.LeftElbow.isActived = True
            avatar_widget.RightElbow.isActived = True

            avatar_widget.LeftWrist.isActived = True
            avatar_widget.RightWrist.isActived = True

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 6:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = False
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = True
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = True
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = True
            avatar_widget.RightAnkle.isActived = False

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 7:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = False
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = True

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = True

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = True

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 8:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = False
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = True
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = True

            avatar_widget.LeftKnee.isActived = True
            avatar_widget.RightKnee.isActived = True

            avatar_widget.LeftAnkle.isActived = True
            avatar_widget.RightAnkle.isActived = True

        elif avatar_widget._joint_chunk_combobox.currentIndex() == 9:

            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = True
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = True

            avatar_widget.LeftElbow.isActived = True
            avatar_widget.RightElbow.isActived = True

            avatar_widget.LeftWrist.isActived = True
            avatar_widget.RightWrist.isActived = True

            avatar_widget.LeftHip.isActived = True
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = True

            avatar_widget.LeftKnee.isActived = True
            avatar_widget.RightKnee.isActived = True

            avatar_widget.LeftAnkle.isActived = True
            avatar_widget.RightAnkle.isActived = True

        else:
            avatar_widget.Head.isActived = True

            avatar_widget.LeftShoulder.isActived = False
            avatar_widget.Chest.isActived = True
            avatar_widget.RightShoulder.isActived = False

            avatar_widget.LeftElbow.isActived = False
            avatar_widget.RightElbow.isActived = False

            avatar_widget.LeftWrist.isActived = False
            avatar_widget.RightWrist.isActived = False

            avatar_widget.LeftHip.isActived = False
            avatar_widget.Center.isActived = False
            avatar_widget.RightHip.isActived = False

            avatar_widget.LeftKnee.isActived = False
            avatar_widget.RightKnee.isActived = False

            avatar_widget.LeftAnkle.isActived = False
            avatar_widget.RightAnkle.isActived = False





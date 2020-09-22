from MotionScanner.Lib.db_connection import DNCMTRY_DB
from MotionScanner.Lib.Entities import Discipline, Pose, Movement, Sequence, User


class DBQueryLib(object):

    @staticmethod
    def ToDiscipline(objects):

        disciplines = []

        for obj in objects:
            discipline = Discipline()
            discipline.Id = obj['_id']
            discipline.Name = obj['Name']
            discipline.Description = obj['Description']
            discipline.Coaches = obj['Coaches']
            discipline.Sequences = obj['Sequences']
            discipline.CreationDate = obj['CreationDate']
            discipline.ModificationDate = obj['ModificationDate']
            disciplines.append(discipline)

        return disciplines

    @staticmethod
    def ToPose(objects):

        poses = []

        for obj in objects:
            pose = Pose()
            pose.Id = obj['_id']
            pose.Name = obj['Name']
            pose.Discipline = obj['Discipline']
            pose.Level = obj['Level']
            pose.Steps = obj['Steps']
            pose.Images = obj['Images']
            pose.Animation = obj['Animation']
            pose.CreationDate = obj['CreationDate']
            pose.ModificationDate = obj['ModificationDate']
            poses.append(pose)

        return poses

    @staticmethod
    def ToMovement(objects):

        movements = []

        for obj in objects:
            movement = Movement()
            movement.Id = obj['_id']
            movement.Name = obj['Name']
            movement.Discipline = obj['Discipline']
            movement.Level = obj['Level']
            movement.Steps = obj['Steps']
            movement.Modification = obj['Modification']
            movement.Poses = obj['Poses']
            movement.Benefit = obj['Benefit']
            movement.Tips = obj['Tips']
            movement.Images = obj['Images']
            movement.Animation = obj['Animation']
            movement.CreationDate = obj['CreationDate']
            movement.ModificationDate = obj['ModificationDate']
            movements.append(movement)

        return movements

    @staticmethod
    def ToSequence(objects):

        sequences = []

        for obj in objects:
            sequence = Sequence()
            sequence.Id = obj['_id']
            sequence.Name = obj['Name']
            sequence.Discipline = obj['Discipline']
            sequence.Level = obj['Level']
            sequence.Coach = obj['Coach']
            sequence.Movements = obj['Movements']
            sequence.CreationDate = obj['CreationDate']
            sequence.ModificationDate = obj['ModificationDate']
            sequences.append(sequence)

        return sequences

    @staticmethod
    def ToUser(objects):

        users = []

        for obj in objects:
            user = User()
            user.Id = obj['_id']
            user.Name = obj['Name']
            user.Birthdate = obj['Birthdate']
            user.Gender = obj['Gender']
            user.Height = obj['Height']
            user.Weight = obj['Weight']
            user.Roles = obj['Roles']
            user.Disciplines = obj['Disciplines']
            user.Sequences = obj['Sequences']
            user.CreationDate = obj['CreationDate']
            user.ModificationDate = obj['ModificationDate']
            users.append(user)

        return users

    @staticmethod
    def GetAllDisciplines():
        collection = DNCMTRY_DB.Discipline()
        objects = collection.find({})
        return DBQueryLib.ToDiscipline(objects)

    @staticmethod
    def GetAllPoses():
        collection = DNCMTRY_DB.Pose()
        objects = collection.find({})
        return DBQueryLib.ToPose(objects)

    @staticmethod
    def GetAllMovements():
        collection = DNCMTRY_DB.Movement()
        objects = collection.find({})
        return DBQueryLib.ToMovement(objects)

    @staticmethod
    def GetAllSequences():
        collection = DNCMTRY_DB.Sequence()
        objects = collection.find({})
        return DBQueryLib.ToSequence(objects)

    @staticmethod
    def GetAllUsers():
        collection = DNCMTRY_DB.User()
        objects = collection.find({})
        return DBQueryLib.ToUser(objects)

    @staticmethod
    def GetDisciplineTags():
        collection = DNCMTRY_DB.Discipline()
        objects = collection.find({})

        disciplines = ['None']
        for obj in objects:
            disciplines.append(obj['Name'])

        return disciplines


from pymongo import MongoClient


class DNCMTRY_DB(object):

    MONGO_URI = 'mongodb://localhost'

    PRODUCTION = 'PRODUCTION'
    TEST_01 = 'TEST-01'

    COLLECTIONS = ['None', 'Disciplines', 'Movement', 'Pose', 'Sequence', 'User']

    @staticmethod
    def GetCollections():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collections = db.getName()
        print(collections)
        return collections

    @staticmethod
    def connect(db_name):
        client = MongoClient(DNCMTRY_DB.MONGO_URI)
        db = client[db_name]
        return db

    @staticmethod
    def Discipline():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collection = db['Discipline']
        return collection

    @staticmethod
    def Movement():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collection = db['Movement']
        return collection

    @staticmethod
    def Pose():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collection = db['Pose']
        return collection

    @staticmethod
    def Sequence():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collection = db['Sequence']
        return collection

    @staticmethod
    def User():
        db = DNCMTRY_DB.connect(DNCMTRY_DB.TEST_01)
        collection = db['User']
        return collection




from MotionScanner.Lib.Entities import Entity
from MotionScanner.Lib import DNCMTRY_DB
import datetime


class Pose(Entity):

    def __init__(self, *args, **kwargs,):
        super(Pose, self).__init__(DNCMTRY_DB.Pose(), *args, **kwargs)

        self._id = {'_id': kwargs['_id'] if '_id' in kwargs else None}
        self._data = {
            'Name': kwargs['name'] if 'name' in kwargs else '',
            'Discipline': kwargs['discipline'] if 'discipline' in kwargs else None,
            'Level': kwargs['level'] if 'level' in kwargs else 0,
            'Steps': kwargs['steps'] if 'steps' in kwargs else [],
            'Images': kwargs['images'] if 'images' in kwargs else [],
            'Animation': kwargs['animation'] if 'animation' in kwargs else '',
            'CreationDate': datetime.datetime.now(),
            'ModificationDate': datetime.datetime.now()
        }

    @property
    def Id(self):
        return self._id['_id']

    @Id.setter
    def Id(self, value):
        self._id['_id'] = value

    @property
    def Name(self):
        return self._data['Name']

    @Name.setter
    def Name(self, value):
        self._data['Name'] = value

    @property
    def Discipline(self):
        return self._data['Discipline']

    @Discipline.setter
    def Discipline(self, value):
        self._data['Discipline'] = value

    @property
    def Level(self):
        return self._data['Level']

    @Level.setter
    def Level(self, value):
        self._data['Level'] = value

    @property
    def Steps(self):
        return self._data['Steps']

    @Steps.setter
    def Steps(self, list):
        self._data['Steps'] = list

    def AddSteps(self, value):
        self._data['Steps'].append(value)

    @property
    def Images(self):
        return self._data['Images']

    @Images.setter
    def Images(self, list):
        self._data['Images'] = list

    def AddImages(self, value):
        self._data['Images'].append(value)

    @property
    def Animation(self):
        return self._data['Animation']

    @Animation.setter
    def Animation(self, value):
        self._data['Animation'] = value

    @property
    def CreationDate(self):
        return self._data['CreationDate']

    @CreationDate.setter
    def CreationDate(self, value):
        self._data['CreationDate'] = value

    @property
    def ModificationDate(self):
        return self._data['ModificationDate']

    @ModificationDate.setter
    def ModificationDate(self, value):
        self._data['ModificationDate'] = value

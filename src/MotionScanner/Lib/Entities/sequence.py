from MotionScanner.Lib.Entities import Entity
from MotionScanner.Lib import DNCMTRY_DB
import datetime


class Sequence(Entity):

    def __init__(self, *args, **kwargs,):
        super(Sequence, self).__init__(DNCMTRY_DB.Sequence(), *args, **kwargs)

        self._id = {'_id': kwargs['_id'] if '_id' in kwargs else None}
        self._data = {
            'Name': kwargs['name'] if 'name' in kwargs else '',
            'Discipline': kwargs['discipline'] if 'discipline' in kwargs else None,
            'Level': kwargs['level'] if 'level' in kwargs else 0,
            'Coach': kwargs['coach'] if 'coach' in kwargs else None,
            'Movements': kwargs['movements'] if 'movements' in kwargs else [],
            'CreationDate': datetime.datetime.now(),
            'ModificationDate': datetime.datetime.now()
        }

    @property
    def Id(self):
        return self._data['_id']

    @Id.setter
    def Id(self, value):
        self._id['_id'] = value

    @property
    def Name(self):
        return self._data['Name']

    @Name.setter
    def Name(self, value):
        self._data['name'] = value

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
    def Coach(self):
        return self._data['Coach']

    @Coach.setter
    def Coach(self, value):
        self._data['Coach'] = value

    @property
    def Movements(self):
        return self._data['Movements']

    @Movements.setter
    def Movements(self, list):
        self._data['Movements'] = list

    def AddMovements(self, value):
        self._data['Movements'].append(value)

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
    def ModificationDate(self, date):
        self._data['ModificationDate'] = date


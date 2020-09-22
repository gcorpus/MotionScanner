from MotionScanner.Lib.Entities import Entity
from MotionScanner.Lib import DNCMTRY_DB
import datetime


class Discipline(Entity):

    def __init__(self, *args, **kwargs,):
        super(Discipline, self).__init__(DNCMTRY_DB.Discipline(), *args, **kwargs)

        self._id = {'_id': kwargs['_id'] if '_id' in kwargs else None}
        self._data = {
            'Name': kwargs['name'] if 'name' in kwargs else '',
            'Description': kwargs['description'] if 'description' in kwargs else '',
            'Coaches': kwargs['coaches'] if 'coaches' in kwargs else [],
            'Sequences': kwargs['sequences'] if 'sequences' in kwargs else [],
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
    def Description(self):
        return self._data['Description']

    @Description.setter
    def Description(self, value):
        self._data['Description'] = value

    @property
    def Coaches(self):
        return self._data['Coaches']

    @Coaches.setter
    def Coaches(self, list):
        self._data['Coaches'] = list

    def AddCoaches(self, value):
        self._data['Coaches'].append(value)

    @property
    def Sequences(self):
        return self._data['Sequences']

    @Sequences.setter
    def Sequences(self, list):
        self._data['Sequences'] = list

    def AddSequences(self, value):
        self._data['Sequences'].append(value)

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

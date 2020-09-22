from MotionScanner.Lib.Entities import Entity
from MotionScanner.Lib import DNCMTRY_DB
import datetime


class User(Entity):

    def __init__(self, *args, **kwargs,):
        super(User, self).__init__(DNCMTRY_DB.User(), *args, **kwargs)

        self._id = {'_id': kwargs['_id'] if '_id' in kwargs else None}
        self._data = {
            'Name': kwargs['name'] if 'name' in kwargs else '',
            'Birthdate': kwargs['birthdate'] if 'birthdate' in kwargs else None,
            'Gender': kwargs['gender'] if 'gender' in kwargs else 0,
            'Height': kwargs['height'] if 'height' in kwargs else 0.0,
            'Weight': kwargs['weight'] if 'weight' in kwargs else 0.0,
            'Roles': kwargs['role'] if 'role' in kwargs else [],
            'Disciplines': kwargs['discipline'] if 'discipline' in kwargs else [],
            'Sequences': kwargs['sequences'] if 'sequences'in kwargs else [],
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
        self._data['Name'] = value

    @property
    def Birthdate(self):
        return self._data['Birthdate']

    @Birthdate.setter
    def Birthdate(self, value):
        self._data['Birthdate'] = value

    @property
    def Gender(self):
        return self._data['Gender']

    @Gender.setter
    def Gender(self, value):
        self._data['Gender'] = value

    @property
    def Height(self):
        return self._data['Height']

    @Height.setter
    def Height(self, value):
        self._data['Height'] = value

    @property
    def Weight(self):
        return self._data['Weight']

    @Weight.setter
    def Weight(self, value):
        self._data['Weight'] = value

    @property
    def Roles(self):
        return self._data['Roles']

    @Roles.setter
    def Roles(self, list):
        self._data['Roles'] = list

    def AddRoles(self, value):
        self._data['Roles'].append(value)

    @property
    def Disciplines(self):
        return self._data['Disciplines']

    @Disciplines.setter
    def Disciplines(self, list):
        self._data['Disciplines'] = list

    def AddDisciplines(self, value):
        self._data['Disciplines'].append(value)

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





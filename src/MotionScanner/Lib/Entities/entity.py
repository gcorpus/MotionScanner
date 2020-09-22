

class Entity(object):

    def __init__(self, collection, *args, **kwargs,):

        self._collection = collection

        self._id = {}
        self._data = kwargs

    def getId(self):
        return self._id

    def getData(self):
        return self._data

    def getComposedData(self):
        return dict(self._id, **self._data)

    def Crup(self):
        if self._id['_id']:
            self._collection.update(self.getId(), {'$set': self.getData()})
        else:
            self._id['_id'] = self._collection.insert(self.getData())

    def Delete(self):
        result = self._collection.remove(self.getId())
        return result


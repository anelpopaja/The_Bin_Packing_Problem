class Item:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def getId (self):
        return self.id

    def getValue(self):
        return self.value

    def __repr__(self):
        s = "Id: " + str(self.id) + " Value: " + str(self.value)
        return s
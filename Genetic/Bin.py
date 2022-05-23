class Bin:
    def __init__(self, id, capacity, fill):

        # promijeniti listu contents u stack
        self.id = id
        self.capacity = capacity
        self.fill = fill
        self.contents = []

    def getId(self):
        return self.id

    def getFill(self):
        return self.fill

    def setFill(self, fill):
        self.fill = fill

    def getCapacity(self):
        return self.capacity

    def getContents(self):
        return self.contents

    def addElement(self, element):
        self.contents.append(element)
        self.fill += element.getValue()

    def removeElement(self):
        item = self.contents.pop()
        self.fill -= item.getValue()
        return item

    def emptyBinGenerator(n, c):
        listOfEmptyBins = list()
        for i in range (n):
            listOfEmptyBins.append(Bin(i,c,0))
        return listOfEmptyBins

    def __repr__(self):
        s = "Id: " + str(self.id) + ", Capacity: " + str(self.capacity) + ", Contents: " + str(self.contents)
        return s
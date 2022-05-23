import random
from The_Bin_Packing_Problem.Genetic.Bin import Bin
from The_Bin_Packing_Problem.Genetic.Item import Item


class Individual:

    # Initialization
    # capacity of bin, item_count, list of items, *genes
    def __init__(self, *args):
        self.full_bins = 0
        self.capacity = args[0]
        self.item_count = args[1]
        self.bins = Bin.emptyBinGenerator(self.item_count, self.capacity)
        self.items = args[2]
        self.genes = []
        self.fitness = 0
        if len(args) == 3:
            self.setGenes()
            self.fillBins()
            self.binAdjustment()
            self.setFitness()

        # TODO Used for intitializing a child chromosome; I think it's done
        else:
            self.genes = args[3]
            # print("New offspring genes: ", self.genes)
            self.fillBins()
            self.binAdjustment()
            self.setFitness()
            # print("New ofspring fitness: ", self.fitness

        self.full_bins = self.getFullBinCount()

    def getGenes(self):
        return self.genes

    def getFullBinCount(self):
        count = 0
        for bin in self.bins:
            if bin.getFill() > 0:
                count += 1
        return count


    # Randomly populating genes (items) List with the index of a bin they will be placed in
    def setGenes(self):

        for i in range(self.item_count):
            place = random.randint(0, self.item_count - 1)
            self.genes.append(place)
        random.shuffle(self.genes)

        #print("Genes before adjustment", self.genes)

    # Filling bins with items according to the random gene list
    def fillBins(self):
        for i, el in enumerate(self.genes):
            self.bins[el].addElement(self.items[i])
            # self.bins[el-1].setFill((self.bins[el-1].getFill()) + (items[i]))

    # Fitness function
    def setFitness(self):
        k = 2
        used_bins = 0
        sum = 0

        # determining how many bins are taken, i.e. how many bins are being used vs. how many are empty
        for bin in self.bins:
            if (len(bin.contents) != 0):
                used_bins += 1

        for i, bin in enumerate(self.bins):
            fill = bin.getFill()
            capacity = bin.getCapacity()

            value = (fill / capacity) ** k
            sum += value
        self.fitness = sum / used_bins

    def binAdjustment(self):
        temp_items = []
        #print("Bins before adjustment: ", self.bins)

        #print("Chromosome before adjustment 2: ", self.genes)
        for bin in self.bins:
            if (bin.fill > bin.capacity):
                while (bin.fill > bin.capacity):
                    temp_items.append(bin.removeElement())
        if (temp_items):
            self.FFD(temp_items)
            self.genesAjdustment()

    def genesAjdustment(self):

        for bin in self.bins:
            if (bin.getContents()):
                for item in bin.getContents():
                    self.genes[item.getId()] = bin.getId()

    def FFD(self, items):
        sorted_items = sorted(items, key=lambda x: x.getValue(), reverse=True)

        for my_item in sorted_items:
            found_a_bin = False
            item_size = my_item.getValue()
            for my_bin in self.bins:
                if (item_size <= (my_bin.getCapacity() - my_bin.getFill())):
                    my_bin.addElement(my_item)
                    found_a_bin = True
                    break
            if found_a_bin == False:
                # it shouldn't come to this, and if it does something is really wrong
                print("Error!!!!")

    def getFitness(self):
        return self.fitness

    def __repr__(self):
        s = "Capacity: " + str(self.capacity) + "\nBins: " + str(self.bins) + "\nGene list: " + str(
            self.genes) + "\nFitness: " + str(self.fitness) + "\n"
        return s

'''
# Ovo cemo citati iz filea
items = [Item(0, 5), Item(1, 1), Item(2, 3), Item(3, 2), Item(4, 4)]

for i in range(10):
    a = Individual(5, 5, items)
    print(a)
'''
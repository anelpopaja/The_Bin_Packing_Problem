import timeit
import time


import The_Bin_Packing_Problem.FileManipulation.ReadInInstances as ReadInInstances

from The_Bin_Packing_Problem.Genetic.Item import  Item
from The_Bin_Packing_Problem.Genetic.Individual import Individual
from The_Bin_Packing_Problem.Genetic.GenerationNew import GenerationNew

# items = [Item(0, 5), Item(1, 1), Item(2, 3), Item(3, 2), Item(4, 4)]


# path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"
# path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Instances\\"
# path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"
'''
bin_capacity, item_count, dict = ReadInInstances.readInInstances(path + "instance.txt")
print("Bin cap", bin_capacity)
print("Item count ", item_count)
items = []

for i in range (item_count):
    items.append(Item(i,dict["item" + str(i+1)]))



initial_individuals = []
for i in range(GenerationNew.population_count):
    initial_individuals.append(Individual(bin_capacity, item_count, items))

#print(initial_individuals)

#print("We are in main")
GenerationNew.population = initial_individuals
g = GenerationNew(items, bin_capacity, item_count)
#print(g.getPopulation())
for GenerationNew.gen_count in range (1000):
    g = GenerationNew(items, bin_capacity, item_count)

print(g.population[0].getFullBinCount())
 #  print(g)
 '''
def runAlgorithm(bin_capacity, item_count, items):
    resetGenerationNew()
    initial_individuals = []
    start_time = time.time()
    for i in range(GenerationNew.population_count):
        initial_individuals.append(Individual(bin_capacity, item_count, items))
        GenerationNew.population = initial_individuals
    elapsed_time = time.time()
    while(elapsed_time-start_time < 600 and GenerationNew.no_improvement_count < GenerationNew.stagnation_max and GenerationNew.gen_count < GenerationNew.max_gen_count):
        print("Current time: " + str(elapsed_time-start_time) + "\n")
        g = GenerationNew(items, bin_capacity, item_count)
        elapsed_time = time.time()
    return g.bestResult(), round(elapsed_time-start_time, 2)

def resetGenerationNew():
    GenerationNew.no_improvement_count = 0
    GenerationNew.population = []
    GenerationNew.gen_count = 0
    GenerationNew.current_occupied_bins = 0


def run(index):
    file = open("GeneticTestResults" + str(index) + ".txt", "w")
    print("Solving small instances of Genetic algorithm...")
    file.write("small\n")
    list_of_dicts1 = []
    for i in range(15):
        print("Instance ", str(i))
        items = []
        bin_capacity, item_count, dict = ReadInInstances.readInInstances(path + "small\\instance" + str(i) + ".txt")
        for j in range(item_count):
            items.append(Item(j, dict["item" + str(j+1)]))
        result,total_time = runAlgorithm(bin_capacity, item_count, items)
        print("Time to solve instance" + str(i) + ": %.2f " % total_time)
        print("Sorted in ", result, " bins")
        dict = {
            "instance": i,
            "time": round(total_time, 3),
            "result": result
        }
        list_of_dicts1.append(dict)
        file.write(str(i) + " " + str (result) + " " +str(total_time) + "\n")
    list_of_dicts2 = []

    print("Solving medium instances of Genetic algorithm...")
    file.write("medium\n")
    for i in range(15):
        print("Instance ", str(i))
        items = []
        bin_capacity, item_count, dict = ReadInInstances.readInInstances(path + "medium\\instance" + str(i) + ".txt")
        for j in range(item_count):
            items.append(Item(j, dict["item" + str(j + 1)]))
        result,total_time = runAlgorithm(bin_capacity, item_count, items)
        print("Time to solve instance" + str(i) + ": %.2f " % total_time)
        print("Sorted in ", result, " bins")
        dict = {
            "instance": i,
            "time": round(total_time, 3),
            "result": result
        }
        list_of_dicts2.append(dict)
        file.write(str(i) + " " + str (result) + " " +str(total_time) + "\n")

    list_of_dicts3 = []
    print("Solving large instances of Genetic algorithm...")
    file.write("large\n")
    for i in range(15):
        print("Instance ", str(i))
        items = []
        bin_capacity, item_count, dict = ReadInInstances.readInInstances(path + "large\instance" + str(i) + ".txt")
        for j in range(item_count):
            items.append(Item(j, dict["item" + str(j + 1)]))
        result,total_time = runAlgorithm(bin_capacity, item_count, items)
        print("Time to solve instance" + str(i) + ": %.2f " % total_time)
        print("Sorted in ", result, " bins")
        dict = {
            "instance": i,
            "time": round(total_time, 3),
            "result": result
        }
        list_of_dicts3.append(dict)
        file.write(str(i) + " " + str (result) + " " +str(total_time) + "\n")
    file.close()


def writeToFile(index,list1, list2, list3):
    file_name = "GeneticTestResults" + str(index) +".txt"
    f = open(file_name, "w")
    f.write("small\n")
    for el in list1:
        f.write(str(el["instance"]) + " " + str(el["result"]) + " " + str(el["time"]))
        f.write("\n")
        print(el["instance"], " ", el["result"], " ", el["time"])

    f.write("medium\n")
    for el in list2:
        f.write(str(el["instance"]) + " " + str(el["result"]) + " " + str(el["time"]))
        f.write("\n")
        print(el["instance"], " ", el["result"], " ", el["time"])

    f.write("large\n")
    for el in list3:
        f.write(str(el["instance"]) + " " + str(el["result"]) + " " + str(el["time"]))
        f.write("\n")
        print(el["instance"], " ", el["result"], " ", el["time"])
    f.close()





for i in range(0,10):
    run(i)
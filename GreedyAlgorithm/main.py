import sys
sys.path.append('../')

import The_Bin_Packing_Problem.GreedyAlgorithm.firstFitDecreasing as firstFitDecreasing
from The_Bin_Packing_Problem.FileManipulation.ReadInInstances import readInInstances
import timeit

# path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Instances\\"
# path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"
'''
bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "small\instance0.txt")
print("Bin size: " + str(bin_size))
print("Number of Instances: " + str(number_of_instances))
#print("Instances: " + str(dict))
#print(len(firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True)))
'''


##main timer function implementation
def run():
    print("Solving extra instance...")
    bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "instance.txt")
    t = timeit.Timer(lambda: f1(dict, bin_size))
    print("Time to solve instance: " + str(t.timeit(number=1)))

    print("Solving small instances...")
    for i in range(15):
        bin_size, number_of_instances, dict = readInInstances(path + "small\instance" + str(i) + ".txt")
        t = timeit.Timer(lambda: f1(dict, bin_size))
        print("Time to solve instance" + str(i) + ": " + str(t.timeit(number=1)))

    print("Solving medium instances...")
    for i in range(15):
        bin_size, number_of_instances, dict = readInInstances(path + "medium\instance" + str(i) + ".txt")
        t = timeit.Timer(lambda: f1(dict, bin_size))
        print("Time to solve instance" + str(i) + ": " + str(t.timeit(number=1)))

    print("Solving large instances...")
    for i in range(15):
        bin_size, number_of_instances, dict = readInInstances(path + "large\instance" + str(i) + ".txt")
        t = timeit.Timer(lambda: f1(dict, bin_size))
        print("Time to solve instance" + str(i) + ": " + str(t.timeit(number=1)))

def f1(dict, bin_size):
    (firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True))

run()

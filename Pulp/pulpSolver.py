import sys

sys.path.append('../')

from pulp import *
import time
import The_Bin_Packing_Problem.GreedyAlgorithm.firstFitDecreasing as firstFitDecreasing
import The_Bin_Packing_Problem.FileManipulation.ReadInInstances as ReadInInstances



# path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
# path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\"
# path =  "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\"
path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\"
# bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances("C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Pulp\\instance.txt")
def run(path, instance):
    bin_size, number_of_instances, dict = ReadInInstances.readInInstances(path + instance)
        #"C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Pulp\\instance.txt")

    items = []
    for i in dict.keys():
        items.append((i, dict[i]))
    print(items)

    itemCount = number_of_instances

    # Maksimalni dozvoljeni broj korpi
    maxBins = itemCount

    # Velicina korpe
    binCapacity = bin_size

    # print("Bin size: " + str(bin_size))
    # print("Number of instances: " + str(number_of_instances))

    # Indikatorska varijabla je dodijeljena 1 kada se koristi korpa
    y = pulp.LpVariable.dicts('BinUsed', range(maxBins),
                              lowBound=0,
                              upBound=1,
                              cat=LpInteger)

    # Indikatorska varijabla kojoj se dodjeljuje 1 kada se stavka stavi u binNum
    possible_ItemInBin = [(itemTuple[0], binNum) for itemTuple in items
                          for binNum in range(maxBins)]

    x = pulp.LpVariable.dicts('itemInBin', possible_ItemInBin,
                              lowBound=0,
                              upBound=1,
                              cat=LpInteger)

    # Inicijalizacija problema
    prob = LpProblem("Bin Packing Problem", LpMinimize)


    # Dodavanje f-je cilja
    prob += lpSum([y[i] for i in range(maxBins)]), "Cilj: Minimizovati iskoristenost korpi"

    # Ogranicenja:

    # Prvo ograničenje: Za svaku stavku, zbir korpa u kojima se pojavljuje mora biti 1
    for j in items:
        prob += lpSum([x[(j[0], i)] for i in range(maxBins)]) == 1, ("Stavka moze biti samo u jednoj korpi -- " + str(j[0]))

    # Drugo ograničenje: Za svaku korpu, broj stavki u korpi ne može premašiti kapacitet korpe
    for i in range(maxBins):
        prob += lpSum([items[j][1] * x[(items[j][0], i)] for j in range(itemCount)]) <= binCapacity * y[i], (
                    "Suma velicina stavki mora biti manja od kapaciteta korpe -- " + str(i))

    # Zapisujemo model na disk
    prob.writeLP("BinPack.lp")

    # Rjesavanje optimizacije
    start_time = time.time()
    prob.solve(PULP_CBC_CMD(timeLimit=600))
    totalTime = prob.solutionCpuTime
    objValue =  prob.objective.value()
    print("Time to solve instance: ", prob.solutionCpuTime)
    print("Value :", prob.objective.value())





    # Koristene korpe
    for i in range(maxBins):
        print(str(y[i]) + ": " + str(y[i].value()))
    print("Bins used: " + str(sum(([y[i].value() for i in range(maxBins)]))))

    # Ostatak
    bins = {}
    for itemBinPair in x.keys():
        if (x[itemBinPair].value() == 1):
            itemNum = itemBinPair[0]
            binNum = itemBinPair[1]
            if binNum in bins:
                bins[binNum].append(itemNum)
            else:
                bins[binNum] = [itemNum]

    for b in bins.keys():
        print(str(b) + ": " + str(bins[b]))

    return totalTime, objValue
'''
Testing greedy algorithm first
'''

import The_Bin_Packing_Problem.Genetic.Main as GenMain
import The_Bin_Packing_Problem.GreedyAlgorithm.main as GreedyMain

for i in range(10):
    GenMain.run(i)

GreedyMain.run()

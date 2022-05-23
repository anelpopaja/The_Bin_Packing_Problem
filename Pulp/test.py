import pulp
import pulpSolver as pulpSolver

path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\"

'''
list1 = []
time,value = pulpSolver.run(path, "Pulp\\instance.txt")
dict = {
        "instance": 0,
        "time": time,
        "result": value
    }
list1.append(dict)
'''

print("Solving small instances...")
list1 = []
for i in range(15):
    time, value = pulpSolver.run(path, "Instances\\small\\instance" + str(i) + ".txt")
    dict = {
        "instance": i,
        "time": time,
        "result": value
    }
    list1.append(dict)

print("Solving medium instances...")
list2 = []
for i in range(15):
    time, value = pulpSolver.run(path, "Instances\\medium\\instance" + str(i) + ".txt")
    dict = {
        "instance": i,
        "time": time,
        "result": value
    }
    list2.append(dict)

print("Solving large instances...")
list3 = []
for i in range(15):
    time, value = pulpSolver.run(path, "Instances\\large\\instance" + str(i) + ".txt")
    dict = {
        "instance": i,
        "time": time,
        "result": value
    }
    list3.append(dict)


def writeToFile(list1, list2, list3):
    file_name = "PulpTestResults.txt"
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


writeToFile(list1, list2, list3)

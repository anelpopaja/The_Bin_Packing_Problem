import random
# path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Pulp\\"
# path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Pulp\\"
path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\"
f = open(path + "instance.txt", "w+")
f.write("5\n")
f.write("20\n")
for j in range(20):
    f.write(str(random.randint(1, 5)) + "\n")
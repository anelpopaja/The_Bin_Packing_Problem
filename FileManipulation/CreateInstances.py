import random
#path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Instances\\"
#path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"
for i in range(15):
    f = open(path + "small\\instance" + str(i) + ".txt", "w+")
    f.write("10\n")
    f.write("50\n")
    for j in range(50):
        f.write(str(random.randint(1, 10)) + "\n")

for i in range(15):
    f = open(path + "medium\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("500\n")
    for j in range(500):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "large\\instance" + str(i) + ".txt", "w+")
    f.write("200\n")
    f.write("2500\n")
    for j in range(2500):
        f.write(str(random.randint(1, 200)) + "\n")

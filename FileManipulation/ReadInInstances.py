def readInInstances(path):
    dict = {}
    f = open(path, "r")
    bin_size = int(f.readline())
    number_of_instances = int(f.readline())
    n = 1
    for line in f:
        dict["item" + str(n) + ""] = int(line)
        n += 1
    f.close()
    return bin_size, number_of_instances, dict
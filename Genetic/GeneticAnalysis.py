import math

path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Genetic\\NewResults\\"

def deviation(average_result, instance_count, list_of_values):
    temp = 0
    for el in list_of_values:
        temp += ((el - average_result) ** 2)

    result = temp / (instance_count-1)
    return round(math.sqrt(result), 3)

def outputToFile(start, end):
    for j in range(start, end):
        best_result = 5000
        average_result = 0
        average_time = 0
        list_of_values = []
        for k in range(10):
            list_of_values.append(list_final_dict[k][j]["result"])
            average_result += list_final_dict[k][j]["result"]
            average_time += list_final_dict[k][j]["time"]
            if list_final_dict[k][j]["result"] < best_result:
                best_result = list_final_dict[k][j]["result"]

        average_result = round(average_result / 10, 3)
        average_time = round(average_time / 10, 3)

        deviation_value = deviation(average_result, 10, list_of_values)

        output_file.write(
            str(best_result) + " " + str(average_result) + " " + str(deviation_value) + " " + str(average_time) + "\n")


list_final_dict = []

for i in range (10):
    input_file = open(path + "GeneticTestResults" + str(i) + ".txt", "r")
    list_file_dict = []
    for j in range (3):
        input_file.readline()
        for k in range (15):
            index, result, total_time = input_file.readline().split()
            dict = {
                "instance": int(index),
                "result": int(result),
                "time": round(float(total_time), 3)
            }
            list_file_dict.append(dict)
    list_final_dict.append(list_file_dict)
    input_file.close()

output_file = open(path + "Analysis.txt", "w")

print(len(list_final_dict[0]))
analysed_list = []

for i in range(3):
    if i == 0:
        output_file.write("small\n")
        outputToFile(0,15)
    else:
        if i == 1:
            output_file.write("medium\n")
            outputToFile(15,30)
        else:
            output_file.write("large\n")
            outputToFile(30,45)


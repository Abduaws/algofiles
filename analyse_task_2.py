import matplotlib.pyplot as plt

f = open("res.txt", "r")
unique = []
avg_list = dict()
worst_list = dict()
best_list = dict()
for line in f:
    element = ""
    for i in range(0, line.index(",")):
        element += line[i]
    if element not in unique:
        unique.append(line[0])
        avg_list[element] = {"sum" : 0, "count": 0}
        worst_list[element] = -10000
        best_list[element] = 10000
    index = 11 + line.index("|")
    value = ""
    for i in range(index, len(line)):
        value += line[i]
    avg_list[element]["sum"] += int(value)
    avg_list[element]["count"] += 1
    if int(value) > worst_list[element]:
        worst_list[element] = int(value)
    if int(value) < best_list[element]:
        best_list[element] = int(value)
print(worst_list)
best_case = [(key, value) for key, value in best_list.items()]
worst_case = [(key, value) for key, value in worst_list.items()]
avg_case = []
for key, value in avg_list.items():
    avg_case.append((key, value["sum"]/value["count"]))
print(best_case)
print(avg_case)
print(worst_case)
plt.plot([x for x, y in best_case], [y for x, y in best_case])
plt.title("Best Case")
plt.xlabel('Arr Size')
plt.ylabel('Steps')
plt.show()

plt.plot([x for x, y in avg_case], [y for x, y in avg_case])
plt.title("Avg Case")
plt.xlabel('Arr Size')
plt.ylabel('Steps')
plt.show()

plt.plot([x for x, y in worst_case], [y for x, y in worst_case])
plt.title("Worst Case")
plt.xlabel('Arr Size')
plt.ylabel('Steps')
plt.show()

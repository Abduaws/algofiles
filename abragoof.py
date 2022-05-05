def init_arr(height):
    level_list = list()
    for i in range(1, height + 1):
        level_list.append(["*"] * i)
        height -= 1
    return level_list

def solve(level_list, last_element_index):
    for i in range(0, last_element_index):
        level_list.insert(last_element_index+1, [])
        index = len(level_list[i]) - 1
        for j in  range(0, len(level_list[i])):
            level_list[last_element_index+1].append(level_list[i].pop(index-j))
    temp_list = []
    for element in level_list:
        if element: temp_list.append(element)
    return temp_list

arr = init_arr(int(input("enter size:\n")))
print(arr)
solved_arr = solve(arr, len(arr)-1)
print(solved_arr)

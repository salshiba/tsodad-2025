list1 = "INSERT PROVIDED LIST"
list1 = list(map(int, list1.split(",")))
    
def overlap_checker(line1, line2):
    number_line = []
    number_line.append(line1[0])
    number_line.append(line1[1])
    number_line.append(line2[0])
    number_line.append(line2[1])
    number_line.sort()
    number_set = set(number_line)
    if len(number_set) != 4:
        return 0
    if number_line[0] in line1 and number_line[1] in line1:
        return 0
    if number_line[0] in line2 and number_line[1] in line2:
        return 0
    if number_line[1] in line1 and number_line[2] in line2:
        return 1
    if number_line[1] in line2 and number_line[2] in line1:
        return 1
    return 0
    
list2 = []
total = 0
temp = 0
for i in list1:
    if temp == 0:
        temp = i
    else:
        if list2 == []:
            list2.append([temp, i])
            temp = i
        else:
            for j in list2:
                if overlap_checker([temp, i], j):
                    total += 1
            list2.append([temp, i])
            temp = i

cut_list = []
for i in range(max(list1)):
    for j in range(max(list1)):
        cut_list.append([i + 1, j + 1])

max_cut_list = []
for cut in cut_list:
    max_cut = 0
    for _ in list2:
        if overlap_checker(cut, _):
            max_cut += 1
    max_cut_list.append(max_cut)
    
print(max(max_cut_list))

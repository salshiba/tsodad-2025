def fishboner(list1):
    spine = []
    smaller = []
    bigger = []

    spine.append(list1[0])
    smaller.append(0)
    bigger.append(0)

    for i in list1[1:]:
        for j in range(len(spine)):
            if (smaller[j] == 0) and (i < spine[j]):
                smaller[j] = i
                break
            elif (bigger[j] == 0) and (i > spine[j]):
                bigger[j] = i
                break
            elif j == (len(spine) - 1):
                spine.append(i)
                bigger.append(0)
                smaller.append(0)

    return list(map(str, smaller)), list(map(str, spine)), list(map(str, bigger))

def sword_value(list1):

    _, spine, _ = fishboner(list1)
    
    return int("".join(spine))

def all_levels(list1):

    smaller, spine, bigger = fishboner(list1)
    temp = []

    for i in range(len(spine)):
        temp.append(smaller[i] + spine[i] + bigger[i])

    for j in range(len(temp)):
        temp[j] = temp[j].replace('0','')

    return list(map(int, temp))

def sword_compare(dictionary, key1, key2):
    temp1 = all_levels(dictionary[key1].split(","))
    temp2 = all_levels(dictionary[key2].split(","))
    for idx in range(len(temp1)):
        if temp1[idx] > temp2[idx]:
            return 0
        elif temp1[idx] < temp2[idx]:
            return 1
    if key1 > key2:
        return 0
    else:
        return 1

sword_list = "INSERT PROVIDED LIST"

dic1 = {}
dic2 = {}
splitted_list = sword_list.split("\n")

for sword in splitted_list:
    temp = sword.split(":")
    dic1[int(temp[0])], dic2[int(temp[0])] = sword_value(list(map(int, temp[1].split(",")))), temp[1]

sorted_items = sorted(dic1.items(), key=lambda item: item[1], reverse=True)
sorted_list = list(sorted_items)

swapped = 1
while swapped == 1:
    swapped = 0
    temp2 = 0
    for i in range(len(sorted_list)):
        if temp2 == sorted_list[i][1]:
            if sword_compare(dic2, sorted_list[i - 1][0], sorted_list[i][0]) == 1:
                sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
                swapped = 1
        temp2 = sorted_list[i][1]

checksum = 0

for x in range(len(sorted_list)):
    checksum += (x + 1) * sorted_list[x][0]

print(checksum)

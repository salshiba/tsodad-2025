list1 = "INSERT RULES"
list2 = "INSERT PREFIXES"

list1 = list1.split("\n")
list2 = list2.split(",")

dic1 = {}
for i in list1:
    temp = i.split(" > ")
    dic1[temp[0]] = temp[1].split(",")
  
name_list = []
for name in list2:
    flag = 0
    for letter in range(len(name[:-1])):
        if name[letter + 1] in dic1[name[letter]]:
            continue
        flag = 1
        break
    if flag == 0:
        name_list.append(name)

min_limit = 7
max_limit = 11

unique_set = set()
while name_list:
    temp = name_list.pop()
    
    if len(temp) >= min_limit and len(temp) <= max_limit:
        unique_set.add(temp)
    if len(temp) == max_limit:
        continue
    
    last_char = temp[-1]
    for next_char in dic1.get(last_char, []):
        name_list.append(temp + next_char)
      
print(len(unique_set))

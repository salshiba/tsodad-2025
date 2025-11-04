list = "Wyrcyth,Mortor,Ildzyth,Aznarel,Xyrtor,Narsar,Shaemfelix,Ozanzeth,Tarldax,Dorvor,Kharnyn,Silzryn,Nyaris,Axalindor,Maralsyx,Eltmyr,Rynmirath,Gorathulth,Jardin,Jorathonar,Malath,Tyroryn,Tyrvoran,Zraallar,Selthar,Igngarath,Mariral,Aelitheldrith,Thyrosvoran,Thymther"
list = list.split(",")

list2 = "L8,R34,L37,R37,L25,R20,L47,R10,L22,R6,L35,R45,L20,R26,L36,R32,L14,R25,L24,R45,L5,R24,L5,R36,L5,R28,L5,R19,L5,R46,L5,R16,L5,R33,L5,R25,L5,R6,L5,R38,L21,R43,L9,R10,L27,R22,L6,R27,L13,R12,L24,R44,L5,R38,L5,R44,L30,R48,L28"
list2 = list2.split(",")
index = 0
index2 = 0

for i in range(len(list2)):
    index = 0
    if list2[i].startswith("L"):
        index -= int(list2[i][1:])
        while index < - len(list):
            index += len(list)
        list[index], list[index2] = list[index2], list[index]
    else:
        index += int(list2[i][1:])
        while index > len(list):
            index -= len(list)
        list[index], list[index2] = list[index2], list[index]

print(list[0])

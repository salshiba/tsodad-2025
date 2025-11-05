list1 = []
s1 = -3374
s2 = -69783

for j in range(1001):
    a = s1
    b = s2 + 1 * j
    
    for i in range(1001):
        list1.append([a, b])
        a += 1
    
def loop_cycle(coor):
    a, b = 0, 0
    c1, c2 = coor[0], coor[1]
    for _ in range(100):
        c = (a * a) - (b * b)
        d = 2 * a * b
        
        c /= 100000
        d /= 100000

        a = int(c) + c1
        b = int(d) + c2

        if abs(a) > 1000000 or abs(b) > 1000000:
            return a, b
    return a, b
        
engrave = 0   
for k in list1:
    x, y = loop_cycle(k)       
    if (abs(x) <= 1000000 and abs(y) <= 1000000):
        engrave += 1
print(engrave)

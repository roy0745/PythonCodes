l1 = [1,4,15]
l2 = [2,5,6]

l3 = []

for i in l2:
    for j in l1:
        l3 += [[i,j]]

for sub in l3:
    print(sub)
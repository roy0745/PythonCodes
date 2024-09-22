l1= [1,5,8,92]
l2= [2,4,9]

h = 0
sh = 0

for i in l1 + l2:
    if i > h:
        sh = h
        h = i
    elif i > sh:
        sh = i
print(sh)
print(h)
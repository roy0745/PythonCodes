
l1 = [1,4]
l2 = [8,9]

h= 0
sc= 0

for n in l1 + l2:
    if n > h:
        sh = h
        h = n
            
    elif n > sh:
        sh = n

print(sh)

            

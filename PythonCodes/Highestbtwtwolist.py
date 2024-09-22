l1 = [1,4,1]
l2 = [4,6,5]

highest = 0

for num in l1 + l2:
    if num > highest:
        highest = num
    
print(highest)


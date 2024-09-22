a = "arunish"
b = "arup"

c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)

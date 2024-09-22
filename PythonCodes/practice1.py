y = {'a':7, 'b':8}
z = {'a':8, 'b':9, 'c':11}

x = {}
v = {}

for key in y:
    if key in z:
        x[key] = y[key] + z[key]

for key in z:
    if key not in y:
        v[key]= z[key]

print(x)
print(v)

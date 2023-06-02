d = dict()
d2 = dict()
for a in range(2):
    d[a] = (a+1),(a+2)

print("Original:" )
print(d)

d.update({len(d):(3,3)})

for item in d:
    d[item] = (item+1), item+2

print(d)


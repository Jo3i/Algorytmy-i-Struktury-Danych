t = [[5,2,3],[22,5,6]]
print("Tablica dla porównania",t)
for i in t:
    najm = min(i)
    z = i.index(najm)
    i[0], i[z] = i[z], i[0]
print("Tablica po zmianach",t)
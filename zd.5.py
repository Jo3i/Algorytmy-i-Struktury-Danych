tablica = [[5,2,3],[22,5,6]]
print(tablica)
for i in tablica:
    najm = min(i)
    z = i.index(najm)
    i[0], i[z] = i[z], i[0]
print(tablica)
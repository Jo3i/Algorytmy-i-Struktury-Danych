def z_najw(lista):
    x = len(lista)
    if x == 1:
        return lista[0]
    else:
        LP = lista[:x//2]
        PP = lista[x//2:]
        Max_L = z_najw(LP)
        Max_P = z_najw(PP)
        return Max_L if Max_L > Max_P else Max_P

A=[4,22,456,233,43,-22]

print(z_najw(A))
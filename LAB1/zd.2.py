n = int(input("Podaj liczbę elementów ciągu: "))
if n>0:
    i = 0
    ile_u = 0
    for i in range(n):
        ai = int(input(f"Podaj a{i}: "))
        if ai<0:
            ile_u += 1
        else:
            i += 1
    print("Ilość liczb ujemnych ciągu ",ile_u )
else:
    n = int(input("Podaj liczbę większą od 0: "))


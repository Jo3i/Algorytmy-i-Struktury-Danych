n =  int(input("Podaj liczbę elementów ciągu: "))
i = 0
if n>0:
    ile_u = 0
    for i in range(n):
        ai = int(input(f"Podaj a{i}: "))
        if ai<0:
            ile_u += 1
            print("Ilość liczb ujemnych ciągu ",ile_u )
        else:
            i += 1


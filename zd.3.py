liczba=int(input("Podaj liczbę, którą chcesz sprawdzić czy znajduję się ona w tablicy: "))
tablica=[-3,4,5,23,-55,435,-666,2137,420]
if liczba in tablica:
    print("Podana liczba znajduje się w tablicy")
else:
    print("Ta liczba nie znajduje się w tablicy")
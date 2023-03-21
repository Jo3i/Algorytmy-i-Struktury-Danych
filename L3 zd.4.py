#zadanie 2 zadania rekurencyjne.pdf
def wynik(i):
    if i<3:
        return 1
    else:
        if i % 2 == 0:
            return wynik(i-3)+wynik(i-1)+1
        else:
            return wynik(i-1)%7
print(wynik(4),"=",wynik(4-3),"+",wynik(4-1),"+",1)


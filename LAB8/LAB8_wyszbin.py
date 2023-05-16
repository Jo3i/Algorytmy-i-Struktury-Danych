# 1. uzytkownik podaje liczbę n elementów, n>0
# 2. elementy losujemy z przedziału (x,y), x i y podaje użytkownik
# 3. wyswietl listę wylosowaną i posortowaną
# 4. uzytkownik podaje szukaną x
# 5. program ma wyświetliśc info o znalezieniu liczby i na jakiej jest pozycji, nie znalazł?, wuświetlić komunikat
import random

def quicksort(l, r, L): #sortowanie szybkie
    if l >= r:
        return

    v = L[r]
    p = l

    for j in range(l, r):
        if L[j] < v:
            L[p], L[j] = L[j], L[p]
            p += 1

    L[p], L[r] = L[r], L[p]

    quicksort(l, p - 1, L)
    quicksort(p + 1, r, L)
    return L

def binarySearch(L,lewy,prawy,szukany):
    lewy=0
    prawy=n-1
    srodek=(lewy+prawy)//2
    while lewy<=prawy:
        srodek = (lewy + prawy) // 2
        if L[srodek]==szukany:
            return srodek
        elif L[srodek]>szukany:
            prawy=srodek-1
        else:
            lewy=srodek+1

    return -1


while True:
        n = int(input("Podaj liczbę n - liczbę w liście: "))
        if n > 0:
            print("Dobrze")
            break
        else:
            print("Podano niedozwoloną liczbę <0")
while True:
    x = int(input("Podaj pierwszą liczbę przedziału listy: "))
    y = int(input("Podaj drugą liczbę przedziału listy: "))
    if x<=y:
        break
    else:
        print("Proszę ponownie podać przedziały: ")

L=[random.randint(x,y) for i in range(n)]
print(f"Wygenerowana lista: {L}")

quicksort(0,n-1,L)
print(f"Posortowana lista: {L}")
# potrzeba usunąć duplikaty, mogą wystąpić w małym przedziale x, y

z = int(input("Sprawdź czy liczba występuje w liście: "))

print(f"Szukana liczba znajduję się na indeksie: {binarySearch(L,0,n,z)}")
# przerobić to na funkcje, zrobić jego schemat blokowy, i zabezpieczyć przed duplikatami
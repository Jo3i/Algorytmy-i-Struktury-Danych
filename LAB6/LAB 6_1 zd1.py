class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def SprStacku(a):
    s = Stack() #pusty stos
    balans = True #pomocniczy bool
    i = 0 #pomocniczy index
    while i < len(a) & balans: #wykonanie pętli jeżeli index jest mniejszy od rozmiaru stosu
        znak = a[i] #wpisanie w tablice do if'a
        if znak == "(":
            s.push(znak) #dodanie znaku do stosu jeżeli znak == "("
        else:
            if s.isEmpty(): #stos jest pusty to
                balans = False #balanse jest 0 jeżeli stos jest pusty
            else:
                s.pop() #Jeżeli jest COŚ, ale nie "(" to usuwa topową wartość stacku
        i = i + 1 #przejście do następnego znaku
    if balans & s.isEmpty(): #jeżeli po sprawdzeniu wszystkiego stos jest pusty to
        return True, print("Wszystkie nawiasy są poprawnie otwarte i zamknięte")
    else:
        return False, print("Gdzieś jest błąd znaków nawiasów")
SprStacku(')(')
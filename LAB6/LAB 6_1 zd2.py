class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def denqueue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def flawiusz(n):
    # Wyznaczenie l
    l = n - (1 << (n.bit_length() - 1))

    # Wyznaczenie miejsca bezpiecznego z wzoru (3)
    wynik = 2*l + 1
    return wynik
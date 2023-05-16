class Node: # lista jednokierunkowa obiektówa
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)
print(temp.getData())
print(temp.getNext())

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current!=None:
            count=count+1
            current=current.getNext()

        return count

    def search(self,item): #szukanie w liście
        current = self.head
        found = False
        while current!= None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item): #usuwanie wartości w liście
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None: #jeśli usuwamy pierwszy element
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def merge(self,list1,list2):
        L=[]


mylist = UnorderedList()
mylist.add(3213)
mylist.add(32)
mylist.add(33)
mylist.add(356)
mylist.add(2345)

print(mylist.size())
print(mylist.search(32))
print(mylist.search(100))
print(mylist)

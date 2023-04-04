def fib(n):
    t=[]
    for i in range(n):
        if i==0:
            t.append(i)
        elif i==1:
            t.append(i)
        else:
            t.append(t[i-1] + t[i-2])
        print(t)
fib(7)

#inaczej

n = int(input("Podaj długosc ciągu fibonacciego: "))
t=[]
for i in range(n):
    if i==0:
        t.append(i)
    elif i==1:
        t.append(i)
    else:
        t.append(t[i-1] + t[i-2])
print(t)

n = int(input("Podaj długosc ciągu: "))
S=[]
for i in range(n):
    if i==0 or i==1:
        S.append(1)
    else:
        S.append((2*S[i-1])-S[i-2])
print(S)
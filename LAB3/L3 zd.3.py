def nwd(a,b): #iteracyjne NWD euklidesem
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a
print(nwd(4,14))

def nwd2(c,d): #rekurencyjne NWD euklidesem
    if d!=0:
        return nwd2(d,c%d)
    return c
print(nwd2(4,14))

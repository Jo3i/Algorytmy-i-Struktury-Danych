def nwd1(a,b): #iteracyjne NWD
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
print(nwd1(4,14))

def nwd2(c,d): #rekurencyjne NWD
    if c!=d:
        if c>d:
            return nwd2(c-d,d) # c = c-d
        else:
            return nwd2(c,d-c) # d = d-c
    return c
print(nwd2(4,14))

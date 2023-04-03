def SUM(A):
    x = len(A)
    if x == 1:
        return A[0]
    else:
        A1 = A[:x // 2]
        A2 = A[x // 2:]
        s1 = SUM(A1)
        s2 = SUM(A2)
        return s1 + s2


A = [23,46,23,11]
print(SUM(A))
def dec_to_bin(n):
    if n == 0:
        return "0"
    l = ""
    while n > 0:
        l = str(n % 2) + l
        n //= 2
    return l
print(dec_to_bin(1))

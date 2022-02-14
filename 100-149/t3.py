def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

mt = [(7, 14), (8, 4), (3, 6)]
for i in mt:
    print(gcd(i[0], i[1]), end=' ')
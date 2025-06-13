def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)


print(mystery(4))


""" 3+2=5
    2+1=3
    1+0=1
    1"""

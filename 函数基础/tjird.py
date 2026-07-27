def math(n):
    if n==1:
        return 1
    else:
        return n*math(n-1)
print(math(3))
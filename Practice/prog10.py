def sumofnatural(n):
    if n==1:
        return n
    else:
        return n+sumofnatural(n-1)
print(sumofnatural(5))
def min(n):
    if len(n)==1:
       return n[0]
    else:
        m=min(n[::-1])
        return n[m]<=n[m-1]
print("min elment in a list:",min(4))

'''def power(a,n):
    if n==0:
        return 1
    else:
        return n*n
print(power(2,4))'''
    


'''def pal(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return pal(s[1:-1])
print(pal("raman"))'''


'''def sum_digit(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_digit(n//10)
num=int(input("Enter number:"))
print("Sum of digits:",sum_digit(num))'''

'''def count_digit(n):
    if n==0:
         return 0
    else:
        return 1+count_digit(n//10)
num=int(input("Enter number:"))
print("Number of digits:",count_digit(num))'''
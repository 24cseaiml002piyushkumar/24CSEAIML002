'''def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''

'''def print_fibo(n,a=0,b=1):
    if n==0:
        return
    print(a,end=" ")
    print_fibo(n-1,b,a+b)
print_fibo(6)'''

def fibonacci(n): 
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=6
for i in range(n):
    print(fibonacci(i),end=" ")
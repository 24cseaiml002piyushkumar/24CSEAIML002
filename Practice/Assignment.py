                           #ASSIGNMENT-3-----
#1
n=int(input("Enter a number:"))
for i in range(2,n):
  d=0
  for j in range(1,i+1):
    if i%j==0:
      d+=1
  if d==2:
    d=0
    n=i+2
for i in range(1,n+1):
    if n%j==0:
        d=d+1
    if d==2:
        print("(%d,%d)"%(i,n))


#2 
x=int(input("Enter a number:"))
factorial=1
if x<0:
  print("It is a negative number")
elif x==0:
  print("The factorial of",x,"is:",factorial)
else:
  for i in range(1,x+1):
    factorial=factorial*i
  print("The factorial of",x,"is:",factorial)

#3
x=int(input("Enter a year:"))
if(x%4==0)and(x%100!=0)or(x%400==0):
  print(x,"is a leap year")
else:
  print(x,"is not a leap year") 


#4 WAP to check the string is symmetrical or palindrome.
x=int(input("enter a string:"))
z=(str(str(x)[::-1]))
if x==z:
  print("it is a palindrome")
else:
  print("it is not a palindrome")

#5 WAP to print even length words in a string.
x=int(input("Enter a String:"))
y="" 
for c in x:
  if c!=" ":
    y=y+c
  else:
    if len(y)%2==0:
      print(y)
    y=""
if len(y)%2==0:
  print(y)

#6 WAP to remove all duplicate from a given string.
x=int(input("Enter a string:"))
result="" 
for char in x:
  if char not in result:
    result=result+char
print(result)

                                        # ASSIGNMENT-4----
#1 WAP to print the second largest and second smallest element in a list of 10 integers without using sort function.
arr=[]
x=int(input("enter the no of elements:"))
for i in range(x):
  m=int(input("Enter the element:"))
  arr.append(m)
for j in range(len(arr)-1):
  for k in range(len(arr)-j-1):
    if arr[k]>arr[k+1]:
      arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("Second largest element is:",second_largest)
print("Second smallest element is:",second_smallest)
 
#2 WAP to create two list first list containing 5 integer and second list containing 5 strings.print both the list one element from each list combined at a time.
list1=[1,2,3,4,5]
list2=["A","B","C","D","E"]
s=[]
for i in range(len(list1)):
  s.append(str(list1[i]))
  s.append(list2[i])
print(s)

#3 WAP to create an integers list of 20 element increase the odd valuede element by 5.
s=[]
x=int(input("enter the no. of elements:"))
for i in range(x):
  n=int(input("Enter the element:"))
  s.append(n)
for i in range(x):
  if s[i]%2!=0:
    s[i]=s[i]+5
print(s)

#4 WAP to create a function that prints the first 15 terms of the fibonacci series without using recursion.
def fibonacci(n):
  a=0
  b=1
  print(a,b,end=" ")
  #print(b)
  for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
n=int(input("Enter the number of terms you want to print:"))
print("The Fibonacci series of first",n,"terms are:")
fibonacci(n)

#5 WAP to create a function that takes list as argument and return the even values of the list.Print the new list with even values.
def even_len(n):
  s=[]
  for i in n:
    if i%2==0:
      s.append(i)
  return s
x=int(input("enter the list elements:"))
n=[int(i) for i in x.split(" ,")]
s=even_len(n)
print(s)

#6 WAP to calculate factorial of a number using recursion.
def factorial(n):
  if n==0:
    result=1
  else:
    result=n*factorial(n-1)
  return result
n=int(input("Enter the number:"))
if(n<0):
  print("It is a Negative number:")
else:
  print("Factorial of",n,"is:",factorial(n))

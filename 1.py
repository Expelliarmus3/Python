#Prog 1
# message= input("Enter your msg:")
# print(message)

#Prog 2
# n1=int(input("Enter 1:"))
# n2=int(input("Enter 2:"))
# n3=int(input("Enter 3:"))
# sum= n1+n2+n3
# print(sum)

#Prog 3
# length=int(input("Length:"))
# Width=int(input("Width:"))
# area=length*Width
# print(area)

#Prog 4
# n1=int(input("1:"))
# n2=int(input("2:"))
# print(n1,n2)
# n1=n1^n2
# n2=n1^n2
# n1=n1^n2
# print(n1,n2)

#Prog 5
# n1= int(input("Enter"))
# if n1%2==0:
#     print("Even")
# else:
#     print("Odd")

#Prog 6
# n1=int(input())
# n2=int(input())
# n3=int(input())
# max=n1
# if n2>max:
#     max=n2
# if n3>max:
#     max=n3
# print(max)

#Prog 7
#ax2+bx+c
import math
a=int(input())
b=int(input())
c=int(input())
d= b**2-4*a*c
if(d==0):
    r=b/(2*a)
    print(r)
elif(d>0):
    r1= (-b+math.sqrt(d))/(2*a)
    r2= (-b-math.sqrt(d))/(2*a)
    print(r1,r2)
else:
    print("Imaginary roots")


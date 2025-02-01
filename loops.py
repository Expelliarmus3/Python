#Sum
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

#Multiplication Table
# for j in range(1,11):
#     print('2 x',j,'=',(2*j))

#Right Triangle
# for a in range(5):
#     for b in range(a):
#         print('*',end=" ")
#     print()

#Pyramid
# n=int(input())
# for a in range(0,n):
#     for b in range(n-a):
#         print(' ',end=" ")
#     for b in range(2*a-1):
#         print('*',end=" ")
#     print()

# def mystery(container):
#     result=[]
#     for i in range(len(container)):
#         if i%2 != 0:
#             result.append(container[i]*4)
#         else:
#             result.append(container[i]*(-1))
#     return result

n=22
k=0
a=[]
b=0
while(n!=0):
    k=k+(n%10)
    a.append(n%10)
    n=n//10
a.sort()
for i in a:
    b=b+i
if(b!=k):
    print("PYTHON IS FUN")
else:
    print("PYTHON IS BORING")

'''Develop a Python program that determines the mode of a list of n numbers, assume only one mode exists in the provided test cases. 
The program should ask for a single line of input containing n, then n space-separated numbers, and output the mode.

'''
# n=input().split()
# print(n)
# min=0
# for i in range(1,len(n)):
#     if(n[i]==n[min]):
#         print(n[min])
#         break
#     else:
#         min+=1
# #         continue
# n=input().split()
# min=0
# for i in range(1,len(n)):
#     if(n[i]!=n[min]):
#         min+=1
#         continue

#     elif(n[i]==n[min]):
#         break
# if(n[min]!=0):
#     print(n[min])

n = input().split()
min_count = 0  # Variable to keep track of the maximum frequency
mode = n[0]   # Initialize the mode with the first element

for i in range(len(n)):
    count = n.count(n[i])  # Count occurrences of n[i]
    if count > min_count:
        min_count = count
        mode = n[i]

print(mode)
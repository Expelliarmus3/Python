#LISTS
# shopping=["Bread","Coffee","Sugar"]
# print(shopping)
# for i in shopping:
#     print(i)
# print()
# for r in range(0,len(shopping)):
#     print(shopping[r])
# print()
# shopping.append("Curd")
# shopping.insert(0,"Egg")
# for i in shopping:
#     print(i)

# L = [1,22,35,0,-5,15,69,88,25,99,4,-988,67,58,25,41,59,102,15]
# print(L.count(15))
# L.sort()
# print(L)
# L.reverse()
# print(L)

# #SLICING
# print(L[1:20:2])
# print(L[len(L):0])

#FIZZBUZZ
import random
num= int(input("enter range"))
for i in range(1,num+1):
    if(i%5==0 and i%3==0):
        print("Fizz-Buzz")
    elif(i%3==0):
        print("Buzz")
    elif(i%5==0):
        print("Fizz")
    else:
        print(i)

#PERMUTATIONS
def choose():
    words=['rainbow','water','computer','engine','programming','player','ice','dark','science','reverse']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(player1,player2,pp1,pp2):
    print(player1,'your score is:',pp1)
    print(player2,'your score is:',pp2)
    print("Thanks for playing")
def play():
     player1=input("Enter ur name:")
     player2=input("Enter ur name:")
     pp1=0
     pp2=0
     turn=0
     while(1):
         picked_word=choose()
         q=jumble(picked_word)
         print(q)
         #player 1
         if turn%2==0:
             print(player1,"Your turn")
             ans=input("Whats on my mind? ")
             if ans==picked_word:
                 pp1=pp1+1
                 print("Your score is : ",pp1)
             else:
                 print("better luck next time!",picked_word)
             c=input("Press 1 to continue and 0 to quit: ")
             if c==0:
                 thank(player1,player2,pp1,pp2)
                 break
         #player 2
         else:
             print(player2,"Your turn")
             ans=input("Whats on my mind? ")
             if ans==picked_word:
                 pp2=pp2+1
                 print("Your score is : ",pp2)
             else:
                 print("better luck next time!",picked_word)
             c=input("Press 1 to continue and 0 to quit: ")
             if c==0:
                 thank(player1,player2,pp1,pp2)
                 break
         turn=turn+1

play()


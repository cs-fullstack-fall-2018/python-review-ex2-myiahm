import random
randomNumber = random.randint(1,10)
# print (randomNumber)
while True:
 # print(userInput)
    userInput = input('Enter Number: ')
    if int(userInput) == randomNumber:
        print("Correct!!!")
        break
    else:
        print("Sorry Charlie!!")

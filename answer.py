import random
randomNumber = random.randint(1,10)
# print (randomNumber)
while True:
 # print(userInput)
    userInput = input('enter num')
    if int(userInput) == randomNumber:
        print("Right")
        break
    else:
        print("wrong")

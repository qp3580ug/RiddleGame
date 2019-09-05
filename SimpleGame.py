import random

riddleList = ["What loses its head in the morning and gets it back at night?", "What can you catch but not throw?", "During what month do people sleep the least?", "What is the center of gravity?", "What starts with an e but only has a single letter in it?"]
riddleAnswers = ["pillow", "cold", "february", "v", "envelope"]
continueRiddles = True

print("Hello. My name is The Riddle Sphinx.\nI am going to ask you a riddle.\nAnswer correctly and you will be rewarded.\nThese will be one word answers.")

while continueRiddles == True:
    randomNumber = random.randint(0, 4)
    listNumber = randomNumber
    riddleToAnswer = riddleList[listNumber]
    answerToRiddle = riddleAnswers[listNumber]
    print(riddleToAnswer)
    answerInputed = str(input())
    while answerInputed != answerToRiddle:
        answerInputed = input("Try Again: ")
    else:
        print("You are correct!!")
        shallWeContinue = input("Would you like to continue? yes or no? ")
        if shallWeContinue == "yes":
            continueRiddles = True
        elif shallWeContinue == "no":
            continueRiddles = False
else:
    print("Til We Meet Again...")
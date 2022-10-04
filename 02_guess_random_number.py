"""
You need to keep the import of random for generating random number.
At line 13 you can modify the range in between the random number is generated
"""

import random

print("Welcome to Random Number Guess")
print("Number goes to 1 from 25")

run = True

randomNum = random.randint(1,25)
guessNum = 0
x = 0

while(run):
  
  guessNum = int(input("Digit a number: "))
  
  if guessNum == randomNum:
    print("Good!!")
    print("You have guessed the number in ",x," times")
    run = False
    break
    
  elif guessNum > randomNum:
    print("Too High!")
    
  elif guessNum < randomNum:
    print("Too Low!")
  x+=1

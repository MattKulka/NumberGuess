import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess a number 1-10"))
    if user == number:
        print("congrats!")
        print(f"you guessed the number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}")

import random

n = random.randint(1, 100)
a = -1
guesses = 0  

print(" Welcome to the Number Guessing Game!")


while a != n:
    a = int(input("Enter a number: "))
    guesses += 1 
    
    if a > n:
        print("❌ Enter a smaller number")
    elif a < n:
        print("❌ Enter a bigger number")

if guesses == 1:
    print(f" Congrats! You guessed the number {n} in your VERY FIRST attempt!")
else:
    print(f" Well done! You guessed the number {n}\b in {guesses}\n attempts.")
    
if guesses <= 10:
    print("you done very fast")
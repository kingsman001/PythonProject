import sys
import io

print("welcome to Python"*3)

guess = input("Please input your number to ! : ")
num = int(guess)
'''for i in range(num):
    if num == 1: break
    else:
        value = num*(num-1)
        num = num-1

print(value)
'''

'''guess the number 8'''
while num!=8:

        if num<8:
            print("Too small, buddy. Have another try.")
            guess = input("Try again.")
            num = int(guess)
        else:
            print("Too big, buddy. Have another try.")
            guess = input("Try again.")
            num = int(guess)

print("Bingo! You got it!")
print("You are so smart!")
print("Game over")

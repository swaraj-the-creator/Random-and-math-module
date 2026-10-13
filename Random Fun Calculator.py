import random
import math
lunu = random.randint(1,20)
print("Your lucky number is ",lunu)
print("\nNow I'll chose a fun activity for you!")
choi = ["Drawing","Singing","Playing soccer(football)"]
fuac = random.choices(choi)
print("Your fun activity ",fuac)
playing = True
number = str(random.randint(0,50))
print("\nI will generate a number from 0 to 50 , and you have to guess the number,one digit at a time.")
while playing:
    guess = input("Give me your best guess! ")
    if number == guess:
        print("You won the game!")
        print("The number was",number)
        break
    else:
        print("Your guess isn't quite right,try again.\n")
print('\nThe floor and ceiling value of 23.56 are: '+str(math.ceil(23.56)) +str(math.floor(23.56)))
x = 10
y= -15
print('The value of x after copying the sign from y is: ' + str(math.copysign(x,y)))
print('Absolute value of -97 and 58 are: ' +str(math.fabs(-97))+str(math.fabs(86)))
print('The GCD of 20 and 15: '+str(math.gcd(20,15)))
print("\nEXECUTION COMPLETE")

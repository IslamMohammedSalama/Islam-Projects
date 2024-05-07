import math 
import random 
import os
os.system('clear')

while True :

    try:

        lower = int(input('enter a frist limit : '))

        break

    except ValueError:

         print('enter a frist limit ! ')

while True :

    try :

        upper = int(input('enter a second limit : '))

        if upper > lower :

            break 

        else :

            raise ValueError

    except ValueError :
        print('enter a second limit ! ')


x = random.randint(lower,upper)
count = 0 
number = round(math.log(upper - lower +1 ,2))

print(f'The number of attempts is {number}')

while count < number :

    count += 1

    while True :

        
        try:

            guess = int(input('enter a guess : '))
            break
        
        except ValueError:

            print('enter a real guess ! ')

    if x == guess :

        print('Congrats ! ')

        break

    elif x > guess :

        print('your guessed is too small ! ')

    elif x < guess :

        print('your guessed is too high ! ')

    print(f'The number of attempts is {number - count}')

if x != guess :

    print(f'the number is {x} ! ')
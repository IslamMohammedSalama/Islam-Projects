import time
from os import system

Loop = True

while Loop :
    system('clear')
    while True :
        try :

            age = int(input('enter your age : ').strip())

            break 

        except ValueError :

            print('please enter a age agine ')

        finally :

            print("*"*50)

            print('you live for : ')

            time.sleep(1)

            print(f"age is : {age} .")

            time.sleep(1)
            
            month = age * 12

            time.sleep(1)

            print(f'month is : {month} .')

            day = month * 30

            time.sleep(1)

            print(f'day is : {day}.')

            hour = day * 24

            time.sleep(1)

            print(f'hour is : {hour}.')

            minute = hour * 60

            time.sleep(1)

            print(f'minute is : {minute}.')

            second = minute * 60

            time.sleep(1)

            print(f'second is : {second}.')

            millisecond = second * 1000

            time.sleep(1)

            print(f'millisecond is : {millisecond}.')

            microsecond = millisecond * 1000

            time.sleep(1)

            print(f'microsecond is : {microsecond}.')

            nanosecond = microsecond * 1000

            time.sleep(1)

            print(f'nanosecond is : {nanosecond}.')

            picosecond = nanosecond * 1000

            time.sleep(1)

            print(f'picosecond is : {picosecond}.')

            femtosecond = picosecond * 1000
            
            time.sleep(1)

            print(f'femtosecond is : {femtosecond}.')
            
            time.sleep(1)

            attosecond = femtosecond * 1000

            time.sleep(1)

            print(f'attosecond is : {attosecond}.')

            time.sleep(1)

            zeptosecond = attosecond * 1000

            time.sleep(1)

            print(f'zeptosecond is : {zeptosecond}.')
            
            yoctosecond = zeptosecond * 1000

            time.sleep(1)

            print(f'yoctosecond is : {yoctosecond}.')

            time.sleep(1)

            print("*"*50)

        break
    while True :

        try :

            time.sleep(1)

            repaet = str(input('do you repeat that (y and n) :').lower())

            if repaet == "y" or repaet == 'yes' :
                Loop = True
                break
            elif repaet == "n" or repaet == 'no' :
                Loop = False
                break
            else :
                raise ValueError
            
        except ValueError :

            print('only  (y or n) ')
            pass
print("program exit")
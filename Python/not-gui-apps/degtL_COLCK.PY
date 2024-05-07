from os import system as sys
from time import sleep

while True:

    try:

        hours = int(input('enter a hours :'))

        break

        if hours > 23:
            raise ZeroDivisionError

        elif hours < 0:

            raise ZeroDivisionError

    except ValueError:

        print('please enter a hours ')

    except ZeroDivisionError:

        print('please enter a hours begger than zero  and letter than 24')

while True:

    try:

        mun = int(input('enter a munints :'))

        break

        if mun < 0:

            raise ZeroDivisionError

        elif mun > 59:

            raise ZeroDivisionError

    except ValueError:

        print('please enter a munints ')

    except ZeroDivisionError:

        print('please enter munints begger than zero  and letter than 60')

while True:

    try:

        sec = int(input('enter a second :'))

        break

        if sec < 0:

            raise ZeroDivisionError

        elif sec > 59:

            raise ZeroDivisionError

    except ValueError:

        print('please enter a second ')

    except ZeroDivisionError:

        print('please enter second begger than zero  and letter than 60')
        

while True :

    sys('clear')

    print(str(hours ,' : ', mun ,' : ', sec ))

    sleep(1)

    sec += 1

    if sec > 59 :

        sec = 0
        mun += 1
    if mun > 59 :

        mun = 0
        hours += 1
    if hours > 11 :

        hours = 1
        mun = 0

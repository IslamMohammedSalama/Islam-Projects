from numba import *
njit(fastmath= True  ,  cache=True , parallel = True)

import random 
import string 

Loop = True
password = []

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
while Loop:
            
    # len_of_password = input("enter the lan of password : ")
    while True :

        try :
            len_of_password = input("enter the lan of password : ")


            len_of_password = int(len_of_password)
            
            
            if len_of_password < 8 :

                len_of_password = input("enter the lan of password agine : ")

            else :

                break

        except ValueError:

            print("enter a right number")

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    p = round(len_of_password * (30/100))
    p2 = round(len_of_password * (20/100))
    
    for index1 in prange(p) :

        password.append(s2[index1])
        password.append(s1[index1])
        password = random.shuffle(password)

    for index1 in prange(p2) :

        password.append(s4[index1])
        password.append(s3[index1])
        password = random.shuffle(password)

    password = random.shuffle(password)

    password = "".join(password[0:])

    print("password is :" ,password)

    print("-"*50)
    print("X"*50)
    print("-"*50)
    while True :
        
        try :

            reapet = input("Do you reapet that (y,yes,n,no)? ").lower()

            if reapet == "y" or reapet == "yes" :
                
                break
            
            elif reapet == "n" or reapet == "no" :

                Loop = False
                break

            else :
            
                raise ValueError
            
        except ValueError :
            
            print("invalit input . input only (y,yes,n,no) ")   
                    
print("progrm exit")



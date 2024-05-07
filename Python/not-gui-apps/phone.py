from numba import njit
@njit(fastmath= True  ,  cache=True , parallel = True)

def main():
    pass

import phonenumbers

from phonenumbers import carrier , geocoder , timezone
print("x"*35)
Loop = True
while Loop == True :
    try :

      enterd_number = input("enter a phonenumber : ")
      phone_num = phonenumbers.parse(enterd_number , None)
    
    except Exception as e:

      print(f'error: {e}')

    print(phone_num)
    
    print(geocoder.description_for_number(phone_num,"en"))
    
    print(carrier.name_for_number(phone_num,"en"))
    
    print("timezone is :",timezone.time_zones_for_number(phone_num))
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

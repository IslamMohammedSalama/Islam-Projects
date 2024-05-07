# import the meduols
from numba import *
njit(fastmath= True  ,  cache=True , parallel = True )
import math

# variable

Loop = True
frist_numder = ""
type_of_opration = ""
type0 = ""
second_number = ""
resalt = ""
reapet = ""

while Loop :

#--CHECK THE FIRST NUMBER IS VALID

  while True:
     
     try:
       
       frist_numder=float(input("enter frist numder : "))
       
       break
     
    #  if not entrad a frist number

     except ValueError as err:
       
       print(err)
       
# check the type_of_opration type

  while True :

    try :

      type_of_opration = input ("enter opration type  from :(+,-,*,/,**,^,sqrt, sin, cos, tan, log, ln) : ")
      
      if type_of_opration in ("sqrt", "sin", "cos", "tan", "log", "ln") :
         
        while True :

          try :

            type0 = input("enter type of opration (frist number or second number ) : ").lower()

            if type0 == "frist number" or type0 == "1" :
                
                type0 = frist_numder
                break
            
            elif type0 == "second number" or type0 == "2" :
              
              type0 = second_number
              break
            else :
              
              raise ValueError
            
          except ValueError :
            
            print("invalit input . input only (frist numder or second number) ")  
            
            break
      
      # if not entred a type_of_opration 

      if type_of_opration in ("+","-","*","/","**","^","sqrt", "sin", "cos", "tan", "log", "ln") :
         
         break

      else :
         
         raise ValueError
      
    except ValueError :
       
       print("invlit type_of_opration . input only +,-,*,/,,**,sqrt, sin, cos, tan, log, ln")
       
      #  check the second numder 

  while True:

    try:
      second_number = float(input ("enter second numder : "))

      if second_number == 0 and type_of_opration == "/" :

        raise ZeroDivisionError
      
      break 

    # if not enterd a second numder

    except ValueError as err2:
      
      print(err2)
      
    except ZeroDivisionError as err3 :
      
      print("do not input 0")
      

# if condehions

  if type_of_opration == "+" :
      
      resalt = frist_numder + second_number

  elif type_of_opration == "-" :
         
      resalt = frist_numder - second_number

  elif type_of_opration == "*" :
        
      resalt = frist_numder * second_number

  elif type_of_opration == "/" :
      
      resalt = frist_numder / second_number

  elif type_of_opration == "^":
    
    resalt = frist_numder ** second_number

  elif type_of_opration == "**":
    
    resalt = math.pow(frist_numder, second_number)

  elif type_of_opration == "sqrt":
    
    resalt = math.sqrt(float(type0))

  elif type_of_opration == "sin":
    
    resalt = math.sin(float(type0))

  elif type_of_opration == "cos":
    
    resalt = math.cos(float(type0))
  elif type_of_opration == "tan":
    
    resalt = math.tan(float(type0))

  elif type_of_opration == "log":
    
    resalt = math.log(float(type0))

  elif type_of_opration == "ln":
    
    resalt = math.log1p(float(type0))

  else :   
      resalt = None

  if resalt != None :
     
     print("resalt is : " , resalt , ".")

  else :
     
     print("invlit type_of_opration .")

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
                
print("program exit")
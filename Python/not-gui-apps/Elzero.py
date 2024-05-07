import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([3,5,2])
# arr3 = arr1 @ arr2
# set1 = {1,3,5}
# set2 = {3,4,5}
# set3 = set1 | set2
# x = 6^3 # not exponet
# y = 6 & 4
# print(2^2)
# 2**2
# x = 1_000_000 # 1000000
# y = 1e6 # 1000000
# z = 10**6 # 1000000
# print(x,y,z,sep="\n")
# print(x==y==z)
# print(x,y,z,sep="\n")
# print(x==y==z)
# --------------------------------------------------
from numpy import array as arr 
# # \
# # \b
# # \r
# # \n
# # \'
# # \"
# # \t
# # \xhh
# print("hello python")
# print("hello \bpython")
# print("hello \
# python")
# print("hello python \\")
# print("hello python \"ssss\"")
# print("hello \npython")
# print("hello 12345 \rpython")
# print("hello \tpython")
# print("\xhh")

# print('''hello
# my
# frind
# ''')
# --------------------------------------------------
# step 1
# Name=" Osama"
# Age= 38
# Country= "Egypt"
# print(f"Hello, My Name Is {Name} And Iam {Age} Years Old and I Live in {Country}.")
# # step 2
# print(type(Name))
# print(type(Age))
# print(type(Country))
# var = 'hello python'

# print(var[0::3])

# a = "#######lkh########"

# print(a.strip('#') ,'\n',
# a.lstrip('#'),'\n',
# a.rstrip('#')
# )

# a ,d,f,g = "1",'10','100','1000'
# print(a.zfill(3),'\n',
# d.zfill(3),'\n',
# f.zfill(3),'\n',
# g.zfill(3))


# a = "i love code"

# print(a.split())
# a = "ilovecode"

# print(a.split("-"))
# a = "i-love-code"

# print(a.split("-",2))
# a = "i-love-code"

# print(a.rsplit("-",3))

# a = "islam"
# print(a.center(1 , "I"))


# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
# --------------------------------------------------------
#! step 1

# var1 = "'Osama'"

# var2 = '"38""'

# var3 = 'Egypt'

# print(f'"Hello {var1} , How You Doing \ """ Your Age Is "{var2}"" + And Your Country Is: {var3}"')

# "Hello 'Osama' , How You Doing \ """ Your Age Is ""38"""" And Your Country Is: "38"""

# ?step 2

# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

# print(f'"Hello {var1}, How You Doing \\\n """ Your Age Is "{var2}"" +\n And Your Country Is: {var3}')


# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

#todo step 3

# name = 'Elzero'


# print(name[1])
# print(name[2])
# print(name[5])

# print(name[1:4])
# print(name[::2])
# print(name[-2::-2])

# *step 4

# name = "#@#@Elzero#@#@"


# print(name.strip('#@'))


#@ step 5

# num = "9"
# print(num.zfill(4))
# num = "15"
# print(num.zfill(4))
# num = "130"
# print(num.zfill(4))
# num = "950"
# print(num.zfill(4))
# num = "1500"
# print(num.zfill(4))



# # Needed Output
# # 0009
# # 0015
# # 0130
# # 0950
# # 1500
# //step 6

# name_one = "Osama"
# name_two = "Osama_Elzero"

# print(name_one.rjust(20,"@"))
# print(name_two.rjust(20,"@"))


# todo step 7

# name_one = "OSamA"
# name_two = "osaMA"

# print(name_one.swapcase())
# print(name_two.swapcase())


# todo step 8

# msg = "I Love Python And Although Love Elzero Web School"

# print(msg.count("Love"))


# todo step 9

# name_two = "Elzero"

# print(name_two.index("z"))


# todo step 10,11

# msg = "I <3 Python And Although <3 Elzero Web School"

# print(msg.replace('<3','love',1))
# print(msg.replace('<3','love'))


# todo step 12

# name = "Osama"
# age = 38
# country = "Egypt"

# # My Name Is Osama, And My Age Is 38, And My Country Is Egypt
# print('My Name Is %s, And My Age Is %d, And My Country Is %s'%(name,age,country))

# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

# ----------------------------------------------------------

# print(type(1+5j))
# print(complex(297619))

# -----------------------------------------------

# step 1

# print(int(10))
# print(float(10))
# print(complex(10))


# # todo step 2
# print((1+2j).imag)
# print((1+2j).real)


# # todo step 3

# num = 10

# print(f"{num:.10f}")


# todo step 4

# num = 159.650

# print(int(num))
# print(type(int(num)))


# todo step 5

# print(100 - 115 ,\
# 50 * 30 ,\
# 21 % 4 ,\
# 110 / 11 ,\
# 97 // 20 )

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

# --------------------------------------------------------------------

# step  
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[0])
# print(friends[-5])
# print(friends[1])
# print(friends[-4])


# todo step 2

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[::2])

# print(friends[::3])

# todo step 3


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[1:4])
# print(friends[3:5])

# friends[-2:] = ['Elzero','Elzero']

# print(friends)


# todo step 4


# friends = ["Osama", "Ahmed", "Sayed", "Ali"]

# friends.insert(0 , "Nasser")

# print(friends)

# friends.append('Salem')

# print(friends)


# todo step 5

# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# # Needed Output
# # ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]



# friends[0:2] = []
# friends.pop()

# print(friends)


# todo step 6

# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]


# friends.extend(employees)
# friends.extend(school)

# print(friends)


# todo step 7

# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# friends.sort(reverse= True)

# print(friends)

# friends.sort(reverse= False)

# print(friends)


# todo step 8

# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# print(len(friends))


# todo step 9

# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# print(technologies[4][0])
# print(technologies[4][2])

# ------------------------------------------------------------

# step 1 

# var1 = "osama"

# print(var1)
# print(type(var1))


# todo step 2

# friends = ("Osama", "Ahmed", "Sayed")

# k = list(friends)
# k[0] = "Elzero"

# d = tuple(k 
#           )
# print(d)
# print(friends)

# print(type(friends))

# print(len(friends),"Elements")


# todo step 3

# var = (1,2,3)
# var1 = ('A','B','c')

# var3 = tuple(var + var1)

# print(var3)
# print(len(var3) ,"Elements")


# todo step 4

t = 1,2,3,4

# a,b,c,d = t

# print(a)
# print(b)
# print(d)

# ----------------------------------------------------------------
# todo step 1
# my_list = [1, 2, 3, 3, 4, 5, 1]

# unique_list = list(set(my_list))
# print(unique_list)

# print(type(unique_list))
# print(unique_list[:4])


# todo step 2

# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(nums|letters)

# set = letters.union(nums)
# print(set)

# nums.update(letters)

# print(nums)


# todo step 3

# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set)
# letters.clear()
# print(letters)
# letters.update("A","B")
# print(letters)


# todo step 4

# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_two.issuperset(set_one))
# print(set_one.issubset(set_two))

# todo step 5

# dir = {
#     "html":"Progress Is 90%",
#     "css":"Progress Is 80%",
#     "python":"Progress Is 30%"
# }
# print("html",dir["html"])
# print("css",dir["css"])
# print("python",dir["python"])
# dir["ai"]= "Progress Is 20%"
# print("ai",dir["ai"])


# ---------------------------------------------


# todo step 1
# print(bool(1))#true
# print(bool("5"))#true
# print(bool('k'))#true
# print(bool(True))#true
# print(bool({}))#False
# print(bool([]))#False
# print(bool(''))#False
# print(bool(False))#False


# todo step 2

# html = 80
# css = 60
# javascript = 70

# print(html and css and javascript > 50)


# todo step 3

# num_one = 10
# num_two = 20
# num = 20

# print(num > num_one or num > num_two)
# print(num > num_one and num > num_two)


# todo step 4

# num_one = 10
# num_two = 20

# r = num_two + num_one

# print(r)

# print(r**3)
# print(r**3%26000)
# print(r**3%26000/5)
# print(type(str(r**3%26000/5)))

# ---------------------------------------------------------


# todo step 1
# input1 = input('enter ').strip().capitalize()

# print(f"Hello {input1}, Happy To See You Here.")


# todo step 2

# a = int(input("enter''"))

# if a < 16 :
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#     print(f"Hello Your Age Is {a}, All Articles Is Suitable For You")


# todo step 3

# a1= input("jjjjjj")
# a5= input("aaaaaa")
# print(f"Hello {a1} {a5[0]}.")


# todo step 4

# f = input("jk")


# print(f'Your Name Is {f[:f.index("@")]}')
# print(f'Email Service Provider Is {f[f.index("@")+1:f.index(".")]}')
# print(f'Top Level Domain Is {f[f.index(".")+1:]}')
# ------------------------------------------------------

# step 1 

# Inputs

# num1 = int(input('Number one of the following values are required').strip())
# num2 = int(input('Number two of the following values are required').strip())

# operation = input('Operation').strip()

# if operation == '*':

#     resalt = num1 * num2 

# elif operation == '+':

#     resalt = num1 + num2

# elif operation == '-':

#     resalt = num1 - num2

# elif operation == '/':

#     resalt = num1 / num2

# else:
#     print('Invalid operation')

# print(f'{num1} {operation} {num2} = {resalt}')



# todo step 2

# age = 17

# print("App Is Suitable For You") if age > 16 else print("App Is not Suitable For You")



# todo step 4

# country = input("Input Your Country")
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countries:
#     print(f"Your Country Eligible For Discount And The Price After Discount Is $70")
# else:
#     print(f"Your Country Not Eligible For Discount And The Price Is $100")

# ---------------------------------------------------------



# todo step 1

# num = int(input('enter'.strip()))

# if num == 0:

#     print("Number 0 Is Not Larger Than 0")

# else :

#     sum = 0

#     while num > 1 :

#         num -= 1
#         if num == 6 :
#             continue 
#         print(num)
#         sum += 1
#         print("8 Numbers Printed Successfully.")
#         break

# step 2

# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# c = 0 

# s = 0

# while c < len(friends):

#     if friends[c].istitle():

#         print(friends[c])

#     else :

#         s += 1
    
#     c += 1
# print("Friends Printed And Ignored Names Count Is 2"
# )


# todo step 3

# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:

#     print(skills.pop(0))


# todo step 4

# list = []
# var = 4

# while 0 < var:

#     name = input("name :").strip()

#     if name.isupper() :

#         print("Invalid Name")
#         continue

#     elif name.islower() :

#         name.capitalize()
#         print("Friend {} Added => 1st Letter Become Capital".format(name))
#         list.append(name)
#         print(f"Names Left in List Is {var - len(list)}")
        
#     elif name.istitle() :


#         list.append(name)
#         print(f"Friend {name} Added")
#         print(f"Names Left in List Is {var - len(list)}")
#     var -= 1

# ------------------------------------------------------------------------

# todo step 1
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# num = 0 

# for i in my_nums :

#     if i%5 == 0 :

#         num += 1
#         print(f"{num} => {i}")
# else :

#     print("All Numbers Printed")


# todo step 2

# for num in range(1,21) :

#     if num in [6,8,12] :

#         continue

#     print(f'{num}'.zfill(2))
# else :

#     print("All Numbers Printed")


# todo step 3

# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }

# rank = {
#     'A' : 100 ,
#     'B' : 80,
#     'C' : 40,
# }
# sum = 0 

# for key , value in my_ranks.items() :

#     print(f"My Rank in {key} Is {value} And This Equal {rank[value]} Points")
#     sum += rank[value]

# else :

#     print(f"My Total Score Is {sum}")


# todo step 4

# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }

# ranks = {

#     'A' : 100,
#     'B' : 80,
#     'C' : 40,
#     'D' : 20
# }

# sum = 0 

# for nume , data in students.items() :

#     print('-'*30)
#     print(f'-- Student Name => {nume}')
#     print('-'*30)

#     for subject,rank in data.items():

#         print(f'- {subject} => {ranks[rank]} Points')
#         sum += ranks[rank]
    
#     print(f"Total Points For {nume} Is {sum}")

# ----------------------------------------------------------------------


# todo step 1

# def calculate( num1, num2,options='none') :

#     options = options.lower()
    
#     if options == 'none' :

#         return num1 + num2
    
#     elif options == 'add'.lower() or options == 'a'.lower():

#         return num1 + num2
    
#     elif options =='subtract'.lower() or options == 's'.lower() :

#         return num1 - num2
    
#     elif options =='multiply'.lower() or options == 'm'.lower() :

#         return num1 * num2

#      else :


#         return 'it is not valid'

# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30

# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10

# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200


# todo step 2

# def addition(*args):

#     sum = 0

#     for i in args :

#         if i  == 10 :

#             continue

#         elif i == 5 :

#             sum -= i

#         else :

#             sum += i

#     return sum



# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160


# todo step 3


# def show_skills(nume ,*args):

#     if len(args) > 0 :
#         print(f"Hello {nume} Your Skills Is : ")

#         for i in args :

#             print(f' - {i}')

#     else :

#         print(f"Hello {nume} You Have No Skills To Show ")

# show_skills("Osama", "HTML", "CSS", "JS", "Python")
# show_skills("Ahmed")


# todo step 4

# def say_hello(nume='unknown', age='unknown',contry='unknown'):
    
#     return f"Hello {nume} Your Age Is {age} And You Live In {contry}"

# print(say_hello('osama'.capitalize() , 38 , 'eygpt'.capitalize()))
# print(say_hello())

# -----------------------------------------------------------------------------------------------------


# todo step 1

# def get_score(**score):

#     '''
    
#     i am hangriy with the score of the current player and \n the score of the previous player and \n the score of the current player and the score of the previous player 
    
#     '''

#     for key,value in score.items() :

#         print(f"{key} => {value}")


# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)


# todo step 2


# def get_people_scores(name='' , **score):

    
#     if len(score) > 0 :


    
#         if bool(name):

#             print(f"Hello {name} This Is Your Score Table:")    

#         for key,value in score.items() :

#             print(f"{key} => {value}")
    
#     else :

#         print(f"hello {name} You Have No Scores To Show")

# # Test 1
# get_people_scores("Osama", Math=90, Science=80, Language=70)

# # Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# # Test 2
# get_people_scores("Mahmoud", Logic=70, Problems=60)

# # Output
# "Hello Mahmoud This Is Your Score Table:"
# "Logic => 70"
# "Problems => 60"

# # Test 3
# get_people_scores(Logic=70, Problems=60)

# # Output
# "Logic => 70"
# "Problems => 60"

# # Test 4
# get_people_scores("Ahmed")

# # Output
# "Hello Ahmed You Have No Scores To Show"


# todo step 3

# scores_list = {
#                 "Math ":" 90",
#                 "Science ":" 80",
#                 "Language ":" 70"
# }


# def get_the_scores(name='',**scores) :

#     if len(scores) > 0 :

#         if bool(name):

#             print(f"Hello {name} This Is Your Score Table:")

#         for key,value in scores.items() :

#                 print(f"{key} => {value}")
            
#         else :

#             print(f"hello {name} You Have No Scores To Show")   

# # Test 1
# get_the_scores("Osama", **scores_list)

# # Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# # Test 2
# get_the_scores("Osama")

# # Output
# "Hello Osama You Have No Scores To Show"

# # Test 3
# get_the_scores(**scores_list)

# # Output
# "Math => 90"
# "Science => 80"
# "Language => 70"

# ----------------------------------------------------------------------------------------------------------------------------------------
# l = 5
# print(f'{f'{f'{f'{f'{f'{l}'}'}'}'}'}')

# ----------------------------------------------------------------------------------------------------------------------------------------
from PIL import Image

# m = Image.open('/home/shared/Islam-projects/Python/gui_apps/phon/icons8-phone-50.png')
# m.show()

def say_hello(name, message):
    print(f"Hello {name} {message}")


say_hello("Osama", "This is a message")
from numba import njit 
njit(fastmath= True  ,  cache=True , parallel = True)







def sum_list(*args):
    resalt = 0
    for x in args :
        resalt += x
        print(resalt)
        print(*args)
        print(args)
    return resalt

print(sum_list(1,2,3,44,5,6,7,8,9))








def sum_list(a,d,*args,option=True):
    resalt = 0
    if option : 
        for x in args :
            resalt += x
        return a + d +resalt
    else :
        return resalt
print(sum_list(1,2,3,4,5,6,7,8,9))





def make_Professor(**kwargs):
    resalt = ""

    for x in kwargs.values() :
        resalt += x
    return resalt













print(make_Professor(
    a = "It's "
    ,
    b = "Professor "
    ,
    c = "Islam "
    ,
    d = "Mohamed "
    ,
    e = "Salama "
    ,
    r = "!"
))









def heman(**kwarg) :
    
    for key , value in kwarg.items():
        print(f"{key} : {value}")
heman( name = "islam " , jop = "chef" , age = "55")








def printw( x , y , *arg , option=True ,**kwarg ) : 

    print(x)
    print(y)
    print(arg)
    print(option)
    print(kwarg)


printw(12,55 ,"111", name = "islam " ,jop = "progamer")








def sum_list(*args):
    resalt = 0
    for x in args :
        resalt += x
        print(resalt)
        print(*args)
        print(args)
    return resalt
li=[1,2,3]
ld=[4,5,6]
lc=[7,8,9]

print(sum_list(*li,*ld,*lc))
print(sum_list(1,2,3,4,5,6,7,8,9))






a ,*b , c =[1,2,3,45,65,6,8,5,5,8,2,58,5,85,52,5]
print(a)
print(b)
print(c)
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
l4 = [*l1 ,*l2 ,*l3]

print(l1)
print(l2)
print(l3)
print(l4)
print(*l1)
print(*l2)
print(*l3)
print(*l4)







d1  ={"a" : 1
    ,
    "b" : 2
    }
d2  ={"u" : 7
    ,
    "n" : 2
    }
d3 = {**d1 , **d2}
print(d1)
print(d2)
print(d3)
print(*d1)
print(*d2)
print(*d3)








lft = [*"flhhhh" , "fsjhdlhfakj"]
lft57 = [*"flhhhh" , *"fsjhdlhfakj"]
lft7 = ["flhhhh" , *"fsjhdlhfakj"]

print(lft)
print(lft7)
print(lft57)
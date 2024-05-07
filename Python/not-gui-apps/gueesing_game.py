# VAREBOLS
secrt_word = "gueesing game"
guees = ""
guees_counnt = 0
guees_limt= 3
out_of_guees = False
# LOOPS
while guees != secrt_word and not out_of_guees == True:
    # IF CONDESHNS
    if guees_counnt < guees_limt :
       
       guees = input("enter your guees : ")
       guees_counnt += 1

    else :
        out_of_guees = True
else :
    # IF CONDESHNS
    if out_of_guees == True :
        print("you lost")
    else :
        print("you won ")
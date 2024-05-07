# ---------- medols-----------

import tkinter as tk
from tkinter import messagebox
import cv2
import os
import random

# --------- end of medols 
# ---------- functions ------------


def ok():

    passsword = ent.get()
    
    if passsword == 'ISLAM':
        os.system('brave')
        quit()

    if passsword != 'ISLAM':

        global error
        error = tk.Label(root, text=' Wrong Password ',foreground='red', bg='black',font='arial  15')
        error.place(x= 95 , y= 160 )
        ent.delete(0,tk.END)
        s = cv2.VideoCapture(0)
        r,i = s.read()
        cv2.imwrite(f'/home/shared/locks/lock{random.randint(0,1000)}.png' , i)
        del(s)
    

def clear():

    ent.delete(0,tk.END)
    error.place(x=1000 , y= 1000)

# ----------- end of functions --------- 

# ---------varebls -------------

root = ''
frame = ''
bok = ''
bc = ''
cam = ''
read = ''
title = ''
label = ''
label2 = ''
error = ''
ent = ''
passsoed = ''

# ------------ end of varebls ----------

# ----------work--------

root = tk.Tk()
root.title('screen lock')
root.geometry('350x300')
root.resizable(False,False)
root.attributes('-alpha',0.5)
root.config(bg='black')

title = tk.Label(root , text=' Screen Lock ' ,foreground='white', bg='red',font='arial  35')
title.pack(fill=tk.X)

label2 = tk.Label(root , text=' Enter a Password : ', font='arial  17' , bg='black', foreground='white')
label2.place(x=70 ,y= 75)

ent = tk.Entry(root , justify= tk.CENTER,font='arial  20',bd=2,relief=tk.RIDGE ,width=20)
ent.place(x=35 ,y=120)

bok = tk.Button(root,text='OK',width=2,height=2,bd=0,relief=tk.GROOVE,cursor='hand2',foreground='white',bg='black',command=ok)
bok.place(x=200,y=200)

bc= tk.Button(root,text='clear',width=2,height=2,bd=0,relief=tk.GROOVE,cursor='hand2',foreground='white',bg='black',command=clear)
bc.place(y=200,x=70)

root.mainloop()

# -------—--end of work---------------
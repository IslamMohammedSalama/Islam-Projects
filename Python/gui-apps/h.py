from tkinter import *
# from math import *
# from numpy import *

root = Tk()
root.title('calculator by islam')
root.geometry('700x550')

en = Entry(root ,font="arial  50 bold" 
            ,foreground='black',bg='white'
            ,justify=RIGHT,width=50)
en.pack(side='top')

frame= Frame(root,bg='black')
frame.pack()

btns=[['7','8','9','/'],
      ['6','5','4','*'],
      ['3','2','1','+'],
      ['.','0','C','-']]

def button_click(value):
    current_expression = en.get()
    en.delete(0, END)
    en.insert(END, current_expression + str(value))

for row in range(len(btns)):
    for col in range(len(btns[row])):
        btn = Button(frame, text=f'{btns[row][col]}', width=4, height=1, font="arial  50 bold", bd=0, bg='white', command=lambda value=btns[row][col]: button_click(value))
        btn.grid(row=row, column=col)
def calculate():
    expression = en.get()
    result = eval(expression)  # Using eval() to evaluate the expression
    en.delete(0, END)
    en.insert(END, result)

eq = Button(frame, text='=',
             width=4, height=1, font="arial  50 bold",
               bg='white', bd=0, command=calculate)
eq.grid(row=4, column=0, sticky="nsew")
root.mainloop()
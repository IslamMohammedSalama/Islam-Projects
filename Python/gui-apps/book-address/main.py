from tkinter import *
import sqlite3 , asyncio , threading 

db =  sqlite3.connect('/home/shared/Islam-projects/Python/gui_apps/book-address/main.db')
cr = db.cursor()
cr.execute('SELECT * FROM pepoles')
all = cr.fetchall()

contactlist = []



class main(Tk) : 

    def __init__(self):
        super().__init__()

        self.Name = StringVar()
        self.Number = StringVar()
        self.geometry('500x400')
        self.title('address book')
        self.resizable(False , False)
        self.config(background='#00ff00')

        self.frame = Frame(self , background='#000000')
        self.frame.place(x=175 , y= 115)

        self.scroll = Scrollbar(self.frame,
                                orient=VERTICAL ,
                                width=20 ,
                                background='#ffffff' ,
                                activebackground='#7b7b7b' ,
                                bd=0 )
        
        self.select = Listbox(self.frame ,
                            width= 25 , 
                            height= 10 ,
                            background='#ffffff' , 
                            font= 'arial  15 bold' ,
                            yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.select.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select.pack(side=LEFT,  fill=BOTH, expand=1)
        self.Select_set()

        Label(self, text = 'Name : ', font='arial 20 bold', bg = '#00ff00').place(x= 30, y=20)
        Entry(self, textvariable = self.Name , font=('impact' , 20 , 'bold')).place(x= 120, y=20)
        Label(self, text = 'Phone No.', font='arial 20 bold',bg = '#00ff00').place(x= 30, y=70)
        Entry(self, textvariable = self.Number , font=('impact' , 20 , 'bold')).place(x= 160, y=70)

        Button(self,text=" ADD", font='arial 20 bold',bd= 0,bg='SlateGray4',relief=GROOVE, command = self.AddContact).place(x= 50, y=150)
        Button(self,text="EDIT", font='arial 20 bold',bd= 0,bg='SlateGray4',relief=GROOVE,command = self.EDIT).place(x= 50, y=200)
        Button(self,text="DELETE", font='arial 20 bold',bd= 0,bg='SlateGray4',relief=GROOVE,command = self.DELETE).place(x= 50, y=250)
        Button(self,text="VIEW", font='arial 20 bold',bd= 0,bg='SlateGray4',relief=GROOVE, command = self.VIEW).place(x= 50, y=300)
        Button(self,text="EXIT", font='arial 20 bold',bd= 0,bg='tomato', relief=GROOVE , command = self.EXIT).place(x= 300, y=350)
        Button(self,text="RESET", font='arial 20 bold',bd= 0,bg='SlateGray4',relief=GROOVE, command = self.RESET).place(x= 50, y=350)

        self.mainloop()

    def Selected(self):
        return int(self.select.curselection()[0])
        

    def AddContact(self):
        contactlist.append([self.Name.get(), self.Number.get()])
        self.Select_set()
        # cr.execute(f'insert into pepoles values("{self.Name.get()}" , "{self.Number.get()}")')


    def EDIT(self):
        contactlist[self.Selected()] = [self.Name.get(), self.Number.get()]
        self.Select_set()
        # cr.execute(f'update pepoles set name = ')


    def DELETE(self):
        del contactlist[self.Selected()]
        self.Select_set()
    
    def VIEW(self):
        NAME, PHONE = contactlist[self.Selected()]
        self.Name.set(NAME)
        self.Number.set(PHONE)

    def EXIT(self):
        self.destroy()

    def RESET(self):
        self.Name.set('')
        self.Number.set('')
        cr.execute('delete from pepoles')


    def Select_set(self) :
        contactlist.sort()
        self.select.delete(0,END)
        for name,phone in contactlist :
            self.select.insert (END, name)
    

if __name__ == '__main__':

    main()
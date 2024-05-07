'''This Project Is The 
Same gui_phone.py But I 
Use In The Project OOP .'''
from customtkinter import set_appearance_mode,set_default_color_theme,CTk
import phonenumbers as ph
from tkinter import messagebox 
from tkinter import *
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
from tkintermapview import TkinterMapView
from threading import Thread
import asyncio
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder
from tkinter.ttk import Style
# set_appearance_mode('system')
# set_default_color_theme('blue')
class Project(CTk):
    def __init__(self , title , geomety):
        super().__init__()
        self.title(title)
        self.geometry(geomety)
        self.resizable(False,False)
        self.config(background='black')

        self.config(background='#00e5ff')
        self.number_label = Label(self , text= "entar a number : "
                                ,font="arial  20 bold"
                                ,foreground='#000000',background='#00e5ff')
        self.number_label.place(x=40,y=10)

        self.number_entry = Entry(self , width=25
                        ,font="arial 20 bold")
        self.number_entry.place(x=290,y=10)
        self.resalts_label = Label(self,text='resalts : ',font='arial  20 bold',foreground= '#000000',background='#00e5ff')
        self.resalts_label.place(x=390,y=60)

        self.frame = Frame(self)
        self.frame.place(x=20,y=100)

        self.scroll = Scrollbar(self.frame, orient=VERTICAL, width=20, background='#828282', activebackground='#5a5a5a', bd=0)
        self.scroll2 = Scrollbar(self.frame, orient=HORIZONTAL, width=20, background='#828282', activebackground='#5a5a5a', bd=0)
        self.lst = Listbox(self.frame, width=59, height=7, background='#ffffff', font='arial 20 bold', yscrollcommand=self.scroll.set, xscrollcommand=self.scroll2.set)

        self.scroll.config(command=self.lst.yview)
        self.scroll2.config(command=self.lst.xview)

        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll2.pack(side=BOTTOM, fill=X)
        self.lst.pack()#place(x=20,y=100)

        self.map_label = Label(self,text='Map : ',
                font='arial  20 bold',
                foreground = '#000000',background ='#00e5ff')
        self.map_label.place(x=390,y=345)

        self.map = TkinterMapView(self,width=850,height=400,corner_radius=0)
        self.map.place(x=20,y=390)
        self.map.set_position(0,0)
        self.map.set_zoom(1)

        self.status = Label(self , text='Status : ready',
            font= 'arial  15 bold',
            foreground='#ffffff',background='#2B2B2B',
            anchor='w',height=1
            )
        self.status.place(rely=1,anchor='sw',relwidth=1)

        self.button = Button(self ,text='get \n information' ,
                        command=lambda : Thread(target=asyncio.run(self.run_async())).start(),
                        relief=GROOVE,
                        bd=0,
                        background='#00ff00',foreground='#000000',font='arial 16 bold',
                        border=0,cursor='hand2'
                        )
        self.button.place(x=690,y=10)


    async def run_async(self):

        global fanc
        fanc =  self.after(500 ,lambda: self.loading)
        try:
            Thread(target=self.gui_app).start()
        finally:
            self.after_cancel(fanc)# Use after_cancel correctly, pass the after result, not the function reference
            self.status.config(text='Status: Complete')
            self.after(500)
            self.status.config(text='Status: Ready')

    def loading(self):
        self.status.config(text='Status : loading.')
        self.after(500)
        self.update()
        self.status.config(text='Status : loading..')
        self.after(500)
        self.update()
        self.status.config(text='Status : loading...')
        self.after(500)
        self.update()

    def get_info(self, entered_number : str) -> str:

        try : 
            phone_number = ph.parse(entered_number , None)
            # print(phone_number)
            code = geocoder.description_for_number(phone_number,"en")
            geocode = OpenCageGeocode('04bde3b93a7748599ec5616cbe526d07')
            query = str(code)
            resalt = geocode.geocode(query)
            # print(resalt)
            info = {
                'Entered Number : ': entered_number ,
                'Phone Number : ' : phone_number ,
                'Formated Number : ': ph.format_number(phone_number, ph.PhoneNumberFormat.INTERNATIONAL ),
                'Country Code : ' : ph.region_code_for_number(phone_number ),
                'Valid : ' : ph.is_valid_number(phone_number),
                'Possibol : ' : ph.is_possible_number(phone_number),
                'Phone Type : ':ph.number_type(phone_number),
                'Servers Provider : ': carrier.name_for_number(phone_number,"en"),
                'TimeZone : ' : timezone.time_zones_for_number(phone_number) ,
                'Latgtuite : ' : resalt[0]['geometry']['lat'] ,
                'Lngtuite : ' : resalt[0]['geometry']['lng'] ,
                'geocoder : ' : code
            }
            return info
        except Exception: 
            return {
                'Entered Number : ': None ,
                'Phone Number : ' : None ,
                'Formated Number : ': None,
                'Country Code : ' : None,
                'Valid : ' : None,
                'Possibol : ' : None,
                'Phone Type : ':None,
                'Servers Provider : ': None,
                'TimeZone : ' : None ,
                'Latgtuite : ' : None ,
                'Lngtuite : ' : None ,
                'geocode : ' : None 
                }

    def gui_app(self):
        self.lst.delete(0, END)
        entered_numbers = self.number_entry.get()

        if entered_numbers:
            information = self.get_info(entered_number=entered_numbers)
            # print(information)
            self.lst.insert(END, '-'*50)
            for key , value in information.items():
                self.lst.insert(END , f'{key} {value} . ')
            self.lst.insert(END, '-'*50)

            try:
                self.map.set_position(information['Latgtuite : '],information['Lngtuite : '] )
                self.map.set_marker(information['Latgtuite : '],information['Lngtuite : '], text='Number Location')
                self.map.set_zoom(9)
            except Exception:messagebox.showerror('Error', 'Error setting map location.')
        else:
            messagebox.showerror('Error', 'Enter a valid number.')

if __name__ == '__main__':
    Project("Phone Number Tracer","890x825").mainloop()

# +966505473147 +447975777666
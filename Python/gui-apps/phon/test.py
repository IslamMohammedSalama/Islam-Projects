import phonenumbers as ph
from tkinter import messagebox
from tkinter import *
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
from tkintermapview import TkinterMapView
from threading import Thread
import asyncio
from geopy.geocoders import Nominatim
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder

class Project(Tk):
    def __init__(self):
        super().__init__()
        self.title("Phone Number Converter")

        self.geometry("890x825")
        self.resizable(False,False)
        self.config(background='black')
        self.number_label = Label(self , text= "entar a number : "
                                ,font="arial  20 bold" 
                                ,foreground='white',bg='black')
        self.number_label.place(x=40,y=10)

        self.number_entry = Entry(self , width=25 
                        ,font="arial  20 bold")
        self.number_entry.place(x=290,y=10)
        

        self.geometry("900x825")
        self.resizable(False,False)
        self.config(background='black')
        self.number_label = Label(self , text= "entar a number : "
                                ,font="arial  20 bold"
                                ,foreground='white',bg='black')
        self.number_label.place(x=40,y=10)

        self.number_entry = Entry(self , width=25
                        ,font="arial 20 bold")
        self.number_entry.place(x=290,y=10)
        self.resalts_label = Label(self,text='resalts : ',font='arial  20 bold',foreground = 'white',bg ='black')
        self.resalts_label.place(x=375,y=60)

        self.frame = Frame(self , 
                            background='#000000')
        self.frame.place(x=20,y=100)

        self.scroll = Scrollbar(self.frame,
                                orient=VERTICAL ,
                                width=20 ,
                                background='#ffffff' ,
                                activebackground='#7b7b7b' ,
                                bd=0 )

        self.lst = Listbox(self.frame ,
                            width= 59 , 
                            height= 7 ,
                            background='#ffffff' , 
                            font= 'arial  20' ,
                            yscrollcommand=self.scroll.set)

        self.scroll.config(command=self.lst.yview)
        self.scroll.pack(side=RIGHT,
                        fill=Y)
        self.lst.pack()#place(x=20,y=100)

        self.map_label = Label(self,text='Map : ',
                font='arial  20 bold',
                foreground = 'white',bg ='black')
        self.map_label.place(x=375,y=345)

        self.map = TkinterMapView(self,width=850,height=400,corner_radius=0)
        self.map.place(x=20,y=390)
        self.map.set_position(35.8681298 ,-90.9456751)
        self.map.set_zoom(9)
        self.map.set_marker(35.8681298 , -90.9456751, text='islam')

        self.status = Label(self , text='Status : ready',
            font= 'arial  15 bold',
            foreground='white',bg='#2B2B2B',
            anchor='w',height=1
            )
        self.status.place(rely=1,anchor='sw',relwidth=1)

        self.button = Button(self ,text='get \n information' ,
                        command=lambda : Thread(target=asyncio.run(self.run_async())).start(),
                        relief=GROOVE,
                        bd=0,foreground='black',bg='white',
                        font='arial  16 bold'
                        ,foreground='white',background='black',
                        border=0,cursor='hand2',)
        self.button.place(x=690,y=10)

        self.mainloop()

    async def run_async(self):

        fanc =  self.after(500 , self.loading)
        try:
            self.gui_app()
        finally:
            # Use after_cancel correctly, pass the after result, not the function reference
            self.after_cancel(fanc)
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

    def get_info(self, entered_number):
        
            try :

                phone_num = ph.parse(entered_number , None)
                code = geocoder.description_for_number(phone_num,"en")

                carrie = carrier.name_for_number(phone_num,"en")

                timezon = timezone.time_zones_for_number(phone_num)
                geocode = OpenCageGeocode('04bde3b93a7748599ec5616cbe526d07')
                resalt = geocode.geocode(code)
                lat = resalt[0]['geometry']['lat']
                lng = resalt[0]['geometry']['lng']

                return (phone_num ,
                        code ,
                        carrie ,
                        timezon ,
                        lat
                        ,lng )

            except Exception:

                return None ,None ,None ,None ,None ,None

    def gui_app(self):
        self.lst.delete(0, END)
        entered_numbers = self.number_entry.get()

        if entered_numbers:
            phone_numb, coderr, carrierr, timezonee, lat, lng = self.get_info(entered_numbers)
            self.lst.insert(END, '-'*100)
            self.lst.insert(END, f'Entered number is: {entered_numbers}')
            self.lst.insert(END, f'Phone number is: {phone_numb}')
            self.lst.insert(END, f'Geocoder is: {coderr}')
            self.lst.insert(END, f'Carrier is: {carrierr}')
            self.lst.insert(END, f'Timezone is: {timezonee}')
            self.lst.insert(END, f'Latitude is: {lat}')
            self.lst.insert(END, f'Longitude is: {lng}')
            self.lst.insert(END, '-'*100)

            try:
                self.map.set_position(lat, lng)
                self.map.set_marker(lat, lng, text='Number Location')
                self.map.set_zoom(9)
            except Exception:
                messagebox.showerror('Error', 'Error setting map location.')

        else:
            messagebox.showerror('Error', 'Enter a valid number.')

        self.status.config(text='Status: Complete')



if __name__ == '__main__':
    Project()

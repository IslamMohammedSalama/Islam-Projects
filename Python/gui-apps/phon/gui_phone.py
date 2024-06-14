# https://a.tile.openstreetmap.org/{z}/{x}/{y}.png
# ---------- medols-----------

import phonenumbers as ph
from tkinter import  messagebox
from tkinter import *
from phonenumbers import geocoder , carrier , timezone
from opencage.geocoder import OpenCageGeocode 
from tkintermapview import TkinterMapView 
from threading import Thread
import asyncio

# --------- end of medols 
# ---------- functions ------------

def loading():


    status.config(text='Status : loading.')
    root.after(500)
    root.update()
    status.config(text='Status : loading..')
    root.after(500)
    root.update()
    status.config(text='Status : loading...')
    root.after(500)
    root.update()

def get_info( enterd_number : str) -> str :

        try :

            phone_num = ph.parse(enterd_number , None)
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



def gui_app() :

    lst.delete(0,END)
    enterd_numbers = number_entry.get()


    # return code,carrier,timezon

    if enterd_numbers :

        phone_numb, coderr,carrierr,timezonee , lat , lng= get_info(enterd_number=enterd_numbers)
        lst.insert(END,'-'*100)
        lst.insert(END,f'enterd number is : {enterd_numbers}')
        lst.insert(END,f'phone number is : {phone_numb}')
        lst.insert(END,f'geocoder is : {coderr} ')
        lst.insert(END,f'carrier is : {carrierr}')
        lst.insert(END, f'timezons is :{timezonee}')
        lst.insert(END, f'lat is :{lat}')
        lst.insert(END, f'lng is :{lng}')
        lst.insert(END, '-'*100)

        try :

            map.set_position(lat,lng)
            map.set_marker(lat,lng,text='number location')
            map.set_zoom(10)

        except Exception :

            messagebox.showerror('error','Checking the network cables, modem, and router \n\
                                    Reconnecting to Wi-Fi')

    else :

        messagebox.showerror('error',
                                'enter a valid number .')

    status.config(text='Status : complete')
    root.after(5000)
    root.update()
    status.config(text='Status : ready')
    root.after_cancel(fanc)

async def ruun():

    global fanc
    fanc = lambda : Thread(target=root.after(500,loading)).start()
    lambda : Thread(target=gui_app).start()

# --------- end of functions ---------

# ---------varebls -------------

lst = 0
root =0
number_label =0
number_entry =0
button =0

# ------------ end of varebls ----------

# ----------work--------

root = Tk()
root.title("Phone Number Converter")
root.geometry("900x825")
root.resizable(False,False)
root.config(background='black')

number_label = Label(root , text= "entar a number : "
                        ,font="arial  20 bold" 
                        ,foreground='white',background='black')
number_label.place(x=40,y=10)

number_entry = Entry(root , width=25 
                        ,font="arial  20 bold")
number_entry.place(x=290,y=10)

resalts_label = Label(root,text='resalts : ',
                font='arial  20 bold',
                foreground = 'white',background ='black')
resalts_label.place(x=375,y=60)

frame = Frame(root , background= '#000000')
frame.place(x=20,y=100)

scroll = Scrollbar(frame ,
                                orient=VERTICAL ,
                                width=20 ,
                                background='#ffffff' ,
                                activebackground='#000000' ,
                                bd=0 , 
                                highlightcolor='#000000')
lst = Listbox(frame , width= 59 , height= 7 ,
                font= 'arial  20' )
scroll.config(command=lst.yview)
scroll.pack(side=RIGHT, fill=Y)
lst.pack()

map_label = Label(root,text='Map : ',
                font='arial  20 bold',
                foreground = 'white',background ='black')
map_label.place(x=375,y=345)

map = TkinterMapView(root,width=850,height=400,corner_radius=0)
map.place(x=20,y=390)
map.set_position(0,0)
map.set_zoom(1)

status = Label(root , text='Status : ready',
            font= 'arial  15 bold',
            foreground='white',background='#1B1B1B',
            anchor='w',height=1
            )
status.place(rely=1,anchor='sw',relwidth=1)

button = Button(root ,text='get \n information' ,
                command=lambda : Thread(target=asyncio.run(ruun())).start(),
                relief=GROOVE,
                bd=0,foreground='black',background='white',
                font='arial 16 bold',
                border=0,cursor='hand2',)
button.place(x=690,y=10)

root.mainloop()

# ------------end of work -------------------

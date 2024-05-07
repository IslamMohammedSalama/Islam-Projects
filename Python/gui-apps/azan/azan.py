import requests as req 
from tkinter import *
from tkinter import ttk , messagebox
from threading import Thread
from json import load
'''
1 - University of Islamic Sciences, Karachi
2 - Islamic Society of North America
3 - Muslim World League
4 - Umm Al-Qura University, Makkah
5 - Egyptian General Authority of Survey
7 - Institute of Geophysics, University of Tehran
8 - Gulf Region
9 - Kuwait
10 - Qatar
11 - Majlis Ugama Islam Singapura, Singapore
12 - Union Organization islamic de France
13 - Diyanet İşleri Başkanlığı, Turkey
14 - Spiritual Administration of Muslims of Russia
15 - Moonsighting Committee Worldwide (also requires shafaq parameter)
16 - Dubai (unofficial)
'''
user = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

list1=[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16]
list2=[
        '1 - University of Islamic Sciences, Karachi',
        '2 - Islamic Society of North America',
        '3 - Muslim World League',
        '4 - Umm Al-Qura University, Makkah',
        '5 - Egyptian General Authority of Survey',
        '6 - Institute of Geophysics, University of Tehran',
        '7 - Gulf Region',
        '8 - Kuwait',
        '9 - Qatar',
        '10 - Majlis Ugama Islam Singapura, Singapore',
        '11 - Union Organization islamic de France',
        '12 - Diyanet İşleri Başkanlığı, Turkey',
        '13 - Spiritual Administration of Muslims of Russia',
        '14 - Moonsighting Committee Worldwide (also requires shafaq parameter)',
        '15 - Dubai (unofficial)'
        ]


with open('gui_apps/azan/countries+cities.json') as alls :

    dicti2 = load(alls)

all1 = []

for i in range(len(dicti2 ) ) :

    all1.append(dicti2[i]["name"])

all2 = []

def get_city(j=None) :
    '''
    Its take two pranetrs to get the citys in way country
    '''
    con = country_entry.get()  # Get the selected country from the combobox
    
    index = all1.index(con)
    l = dicti2[index]["cities"]
    for i in range(len(l)):
        all2.append(l[i]["name"])

    city_entry.set('enter a city :')
    city_entry.config(values=all2) 
 
    

dicti= {}

for i in range(len(list1)) :

    dicti[list2[i]]= list1[i]




def geting_time(city, country,method):

    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}'
    try:
        response = req.get(url,headers=user)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else :

            return None
        
    except Exception as e:

        return f'unexpected error occurred {e}'
    
def gui_app():

    status.config(text='Status : loading...')
    lst.delete(0,END)
    city = city_entry.get()
    country = country_entry.get()
    mothold = dicti[combo.get()]

    if city and country and mothold:

        get_time = geting_time(city , country,mothold)
        for key , value in get_time.items() :

            lst.insert(END, f"{key}: {value}")
            lst.insert(END)
    else :

        messagebox.showerror('Error', 'Please enter city and country')

    status.config(text='Status : ready')
    
root = Tk()
root.title('Prayer Times')
root.resizable(False,False)
root.geometry('450x650')
root.config(bg='#000000',bd=0)

staly = ttk.Style()
staly.configure('MyCustomStyle.TCombobox', background='#ff0000', foreground='#ffffff' , font=('arial ',20,'bold'))

title = Label(root , text= 'Welcome To Azan Time !',foreground='white',
              bg='#00DCFF',font='arial  22 bold')
title.pack(fill=X)

city_label = Label(root , text= 'City : ',
                       font="arial  20 bold" ,
                       foreground='white',background='black')
city_label.place(x=15,y=100)

city_entry = ttk.Combobox(root , width= 20 ,font='arial  20 bold',state='readonly' )
city_entry.place(x=140,y=100)
city_entry.set('get contry frist .')

country_label = Label(root , text= 'country : ', font="arial  20 bold" , foreground='white',bg='black')
country_label.place(x=20,y=50)

country_entry = ttk.Combobox(root ,background='#c13030',values=all1, state='readonly', width= 18 ,font='arial  20 bold')
country_entry.place(x=165,y=50)
country_entry.set('enter a country')
country_entry.bind("<<ComboboxSelected>>" , get_city)

combo = ttk.Combobox(root , values=list2 , width= 25 ,style='MyCustomStyle.TCombobox', font='arial  20 bold',cursor='hand2' , state='readonly' , foreground='black', background='white')
combo.set('enter a calculation way : ')
combo.place(x=20 , y = 150)

status = Label(root , text='Status : ready',
              font= 'arial  15 bold',
              foreground='white',bg='#332f2f',
              anchor='w',height=1
              )
status.place(rely=1,anchor='sw',relwidth=1)

button = Button(root ,text='get information' ,
                command=lambda : Thread(target=gui_app).start(),
                relief=GROOVE,
                bd=0,foreground='black',bg='white',
                font='arial  16 bold'
                ,foreground='white',background='black',
                border=0,cursor='hand2')
button.place(x=150,y=200)
lst = Listbox(root , width= 25 , height= 11 ,font= 'arial  20 bold')
lst.place(x=40,y=250)
root.mainloop()

# city = input('city :')
# country = input('country :')
# mithold = input('mold :')
# if city and country :

#     time = get_time(city,country,8)
#     # print(time)
#     for i , n in time.items():

#         print(i,' : ',n)

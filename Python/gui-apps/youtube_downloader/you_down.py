from pytube import YouTube
from tkinter import  ttk , messagebox ,filedialog 
from tkinter import *
from threading import Thread
from time import sleep as sle
from re import search

lst = []
yt=''
formula = ['video and sound','only video','only sound']


def clear():

    entry.delete(0,END)
    entry1.delete(0,END)

def bowse():

    entry1.delete(0,END)
    dirc = filedialog.askdirectory(title= 'save video files')
    entry1.insert(0,dirc)




def download():
    
    # yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
    # yt.streams
    # .filter(progressive=True, file_extension='mp4')
    # .order_by('resolution')
    # .desc()
    # .first()
    # .download()
    get_url = link.get()
    get_Formulas = Formulas.get()
    get_folder = entry1.get()

    try :

        status.config(text='downloading...')

        if get_Formulas == 'video and sound' :

            yt = YouTube(get_url,on_complete_callback=finth).streams.filter(progressive=True, file_extension='mp4', resolution='720p').order_by('resolution').desc().first().download(get_folder)
        
        elif get_Formulas == 'only video' :

            yt = YouTube(get_url,on_complete_callback=finth).streams.filter(only_video=True, file_extension='mp4', resolution='720p').order_by('resolution').desc().first().download(get_folder)
        
        elif get_Formulas == 'only sound' :

            yt = YouTube(get_url,on_complete_callback=finth).streams.filter(only_audio=True, file_extension='mp4', resolution='720').order_by('resolution').desc().first().download(get_folder)
        
    except Exception:
    
        messagebox.showerror('error','Error in downloading')
    
def finth(none=None, download=None):
    
    status.config(text='Stutas : completed')
    sle(2)
    status.config(text='Stutas : ready')



def progress():
    
    progressbar = ttk.Progressbar(root,length=200)
    progressbar.place(x=200,y=300)
    while True:
        for i in range(100):
            progressbar["value"] = i + 1
            root.after(100)
            root.update()


root = Tk()
root.title('Youtube Downloader - Download You Videos ')
root.geometry('750x600')
root.resizable(False,False)
root.config(bg='black')

link = StringVar()

logo = PhotoImage(file= '/home/shared/Islam-projects/Python/gui_apps/youtube_downloader/download (2).png')
imege = Label( root, image= logo , bd=0)
imege.place(x= 225 , y= 75)


label = Label(root,
               text='Welcome To Youtube Downloader',
                 foreground= 'white',
                 bg= 'red',
                   font= 'arial  25 bold')
label.pack(fill=X)

label_1 = Label(root,
                 text='enter a url : ',
                   foreground= 'white',
                   bg= 'black',
                     font= 'arial  20 bold')
label_1.place(x= 30 , y= 250 )

entry = Entry(root,
               foreground= 'black',
               bg= 'white',
                 font= 'arial  20 bold',
                   bd=0 , 
                   width=26,
                   textvariable= link )
entry.place(x=190 , y=250)
# entry.bind("<FocusOut>", lambda a=None : Thread(target=get_qulety).start)
label_2 = Label(root,
                 text='folder dirctory : ',
                   foreground= 'white',
                   bg= 'black',
                     font= 'arial  20 bold')
label_2.place(x= 30 , y= 300 )

entry1 = Entry(root,
                foreground= 'black',
                bg= 'white',
                font= 'arial  20 bold',
                bd=0 ,
                width=22)
entry1.place(x=250 , y=300)

Formulas = ttk.Combobox(root , 
                        values= formula , 
                          font='arial  15' ,
                            state='readonly',
                            cursor='hand2',
                            width=26,
                            )

Formulas.set('enter a formula : ')
Formulas.place(x= 80, y=350)

status = Label(root , text='Status : ready',
              font= 'arial  15 bold',
              anchor='w',height=2
              )
status.place(rely=1,anchor='sw',relwidth=1)

button1 = Button(root,
                  text='clear',
                    foreground= 'black',
                    bg= 'white',
                      font= 'arial  20 bold' ,
                        command=clear,cursor='hand2' ,
                          relief= GROOVE,bd= 0 )
button1.place(x=100 , y=450)

button2 = Button(root,
                  text='browse',
                    foreground= 'black',bg= 'white',
                      font= 'arial  15 bold' ,
                        command=bowse,cursor='hand2' ,
                          relief= GROOVE,bd= 0 )
button2.place(x= 600, y=300)

button3 = Button(root,
                  text='download',
                    foreground= 'black',bg= 'white',
                      font= 'arial  15 bold' ,
                        command=lambda : Thread(target=download).start(),cursor='hand2' ,
                          relief= GROOVE,bd= 0 )
button3.place(x= 275, y=450)

root.mainloop()
# helo.dowonload if 
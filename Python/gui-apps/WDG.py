# importing the modules to work................................................................................
from tkinter import *
from pytube import *
from tkinter import messagebox
from tkinter import ttk
import re
# screen diminions and the title and color.......................................................
screan=Tk()
screan.title('Youtube Video Downlaoder')
screan.geometry('500x100')
screan.configure(bg='lightblue')
# icon.............................................................................................

# taking the URL from the user.......................................................................
AskingForUrl=Label(screan,
text='Enter the URL please:',
foreground='blue',bg='lightblue'
,font=('arial ',12))
AskingForUrl.pack()
# URL.........................................................................................................
urlj=StringVar()
URLj=Entry(screan,
font=('arial ',12),
textvariable=urlj
,width=50)    
URLj.pack()
# funcions...................................................................................
def get_var(myvar):
   return myvar.get()         
# checking the qualities of the video and toplevel...........................................
num=0
def CheckQuality():
#loading
    messagebox._show('Checking the qualities','Loading please wait.....')
# checking if the video is avaliable...........................................................................    
    try:yt=YouTube(URLj.get().strip())  
# returning an error if the video not avaliable.................................................................    
    except:messagebox.showerror('Error',
       'Can\'t find the video please try again.')   
    else:
# toplevl settings..............................................................................................      
      TopWindow=Toplevel()
      TopWindow.geometry('350x420')
      TopWindow.configure(bg='lightblue')
# icon.............................................................................................
# space....................................................................................................... 
      space=Label(TopWindow,text='                     ',bg='lightblue',foreground='blue')
#organizer function....................................................................................................
      def organizer(list=[],VarVariable=None,number=0):
          global num
          num += number 
          index=0
          TheMonster=0
          if not len(list)<3  :
             for r in range(0+num,3+num):
                 for c in range(round(len(list)/3)):
                     if TheMonster == index *2:
                        Checkbutton(TopWindow,text=list[index]
                        ,bg='lightblue',foreground='blue',
                        activebackground='lightblue',activeforeground='blue',
                        variable=VarVariable,onvalue=index).grid(row=r,column=c)
                        if index < len(list)-1:
                           index += 1   
                        TheMonster += 2         
          else: 
              for i in range(len(list)):
                  Checkbutton(TopWindow,text=list[i]
                  ,bg='lightblue',foreground='blue',
                  activebackground='lightblue',activeforeground='blue',
                  variable=VarVariable,onvalue=index).grid(row=num,column=i+1)
          num += len(list)
          return num
# title and varibals...............................................................................................      
      File_type=Label(TopWindow,
      text='Choose file type and the quality:',
      foreground='blue',bg='lightblue',
      font=('arial ',10))
      File_type.grid(row=0,column=1)
      var1=IntVar()
      space.grid(row=0,column=0)
# video radiobutton.............................................................................................      
      video=Radiobutton(TopWindow
      ,text='Video with audio',
      foreground='blue',bg='lightblue',
      variable=var1,value=1,
      font=('arial ',10))
      video.grid(row=1,column=1)
# video qualities..................................................................................................
      only_video=re.findall('(?<=res=")\d*p',
       str(yt.streams.filter(progressive=True)))
      var_video=IntVar()
      organizer(list=only_video,VarVariable=var_video,number=2)
# video without audio radiobutton.................................................................................................
      VidoeWithoutAudio=Radiobutton(TopWindow
      ,text='Video without audio',
      foreground='blue',bg='lightblue',
      variable=var1,value=111,
      font=('arial ',10))
      VidoeWithoutAudio.grid(row=organizer(),column=1)
# video without audio qualities.............................................................................................................
      only_videoWV=re.findall('(?<=res=")\d*p',
       str(yt.streams.filter(progressive=False,only_video=True)))
      only_videoWVSet=sorted(list(set(only_videoWV)))
      var_videoWV=IntVar()
      organizer(list=only_videoWVSet,VarVariable=var_videoWV,number=1)
# audio radiobutton........................................................................................................
      audio=Radiobutton(TopWindow,
      text='Audio',
      foreground='blue',bg='lightblue',
      variable=var1,value=11,
      font=('arial ',10))
      audio.grid(row=organizer(),column=1)
# audio qualities...........................................................................................................
      only_vaudio=re.findall('(?<=abr=")\d*kbps',
       str(yt.streams.filter(only_audio=True)))
      var_audio=IntVar()
      organizer(list=only_vaudio,VarVariable=var_audio,number=1)
# path.......................................................................................................................
      AskingForPath=Label(TopWindow,text='Enter the path (optional):',
      bg='lightblue',foreground='blue',
      font=('arial ',10))
      AskingForPath.grid(row=organizer(number=1),column=1,columnspan=3)
      path=Entry(TopWindow,width=50)
      path.grid(row=organizer(number=1),column=0,columnspan=3,padx=10)
# space........................................................................................................... 
      space.grid(row=organizer(number=1),column=1,columnspan=3)
# download function..................................................................................           
      def DownloadTheVideo():
# downloading the video.......................................................................................
          if get_var(var1)==1:
            for i in range(len(only_video)):
               if get_var(var_video)==i:
                  yt.streams.filter(progressive=True)[i].download(output_path=path.get())  
                  messagebox.showinfo('Congratulations',
                  'Your video is downloaded.')           
# downloading the audio....................................................................................................
          elif get_var(var1)==11:
             for x in range(len(only_vaudio)):
                 if get_var(var_audio)==x:
                    yt.streams.filter(only_audio=True)[x].download(output_path=path.get())  
                    messagebox.showinfo('Congratulations',
                    'Your audio is downloaded.') 
# downloading video without audio................................................................................
          elif get_var(var1)==111:
             for x in range(len(only_videoWV)):
                 if only_videoWVSet[get_var(var_videoWV)]==only_videoWV[x]:
                    yt.streams.filter(progressive=False,only_video=True)[x].download(output_path=path.get())  
                    messagebox.showinfo('Congratulations',
                    'Your video without audio is downloaded.') 
                    break            
          else:messagebox.showerror('Error','You did\'t select any file type!!')                                                                                
# the bottuns...............................................................................................................
      btnD=Button(TopWindow,
      text='Download',bg='blue',
      width=20,foreground='lightyellow'
      ,command=DownloadTheVideo
      ,activebackground='blue'
      ,activeforeground='yellow')
      btnD.grid(row=organizer(number=1),column=0,columnspan=3)
# check quality..................................................................................
btnQ=Button(screan,text='Check available qualities',
bg='blue',width=40,font=('arial ',11),
foreground='lightyellow'
,command=CheckQuality
,activebackground='blue'
,activeforeground='yellow')
btnQ.pack()
# making the screen working when the program is running........................................
screan.mainloop()
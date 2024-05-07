# ---------- medols-----------

import tkinter as tk
from tkinter import ttk , messagebox
from libretranslatepy import LibreTranslateAPI

# --------- end of medols 
# ---------- functions ------------

def translate():

    output_text.delete('1.0',tk.END)

    try :

        translated_text = lt.translate(input_text.get('1.0', tk.END),lan_code[input_lang.get()],lan_code[output_lang.get()])
        output_text.insert(tk.END,translated_text)
    
    except KeyError as e :

        messagebox.showerror("Error", e)
    

def clear():

    output_text.delete('1.0',tk.END)
    input_text.delete('1.0',tk.END)
    input_lang.set('enter a language : ')
    output_lang.set('enter a language : ')
    

# ----------- end of functions --------- 

# ---------varebls -------------


lt = LibreTranslateAPI("https://translate.argosopentech.com/")
languages = lt.languages()
lan_name = [lang['name'] for lang in languages]
lan_code = {lang['name'] : lang['code'] for lang in languages}

# ------------ end of varebls ----------

# ----------------------work------------------------------

root = tk.Tk()
root.geometry("1000x600" )
root.resizable(False,False)
root.title(" translitone ")
root.config(bg= 'black')

Label_1 = tk.Label(root , text= 'motargem islam ' , font='arial  40' , foreground= 'white',bg= 'black')
Label_1.place(x=300, y=20)

# input text

Label_2 = tk.Label(root, text= ' enter a text : ', font='arial  20' , foreground= 'white',bg= 'black')
Label_2.place(x= 60 , y= 120)

input_text = tk.Text(root , width=22, height= 9 , font='arial  20' , foreground= 'white',bg= 'black')
input_text.place(x= 60, y= 225)

input_lang = ttk.Combobox(root , values=lan_name , font='arial  20',state= 'readonly',cursor='hand2')
input_lang.set('enter a language : ')
input_lang.place(x= 60, y= 170)

# output text

Label_3 = tk.Label(root, text= ' output text : ' , font='arial  20' , foreground= 'white',bg= 'black')
Label_3.place(x= 600 , y= 120)

output_text = tk.Text(root , width=22, height= 9 , font='arial  20'  , state='disabled', foreground= 'white',bg= 'black')
output_text.place(x= 600, y= 225)

output_lang = ttk.Combobox(root , values=lan_name , font='arial  20' , state='readonly',cursor='hand2')
output_lang.set('enter a language : ')
output_lang.place(x= 600, y= 170)

# buttons

Button_1 = tk.Button(root, text= 'translate', font='arial  20' , width=7, padx= 10 , command=translate, foreground= 'white',bg= 'black',relief=tk.GROOVE,cursor='hand2')
Button_1.place(x= 450, y= 300)

Button_2 = tk.Button(root, text= 'clear', font='arial  20' , width= 7 , padx=10 , command=clear, foreground= 'white',bg= 'black',relief=tk.GROOVE,cursor='hand2')
Button_2.place(x= 450, y= 400)


root.mainloop()

# ------------end of work -------------------


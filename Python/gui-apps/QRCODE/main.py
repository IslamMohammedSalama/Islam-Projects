import os
from tkinter import *
from PIL import Image, ImageTk
import qrcode

class main(Tk):
    def __init__(self, geometry, title):
        super().__init__()
        self.geometry(geometry)
        self.title(title)
        self.config(background='#00ff00')

        Label(self, text='Welcome To The Application',
                bg='#ff1111', fg='#000000',
                font=('arial', 22, 'bold')).pack(side=TOP, fill=X)

        Label(self, text='Title : ',
                bg='#00ff00', fg='#000000',
                font=('arial', 20, 'bold')).place(x=50, y=50)

        self.en1 = Entry(self, font=('arial', 20, 'bold'))
        self.en1.place(x=200, y=50)

        Label(self, text='Text : ',
                bg='#00ff00', fg='#000000',
                font=('arial', 20, 'bold')).place(x=50, y=100)

        self.en2 = Entry(self, font=('arial', 20, 'bold'))
        self.en2.place(x=200, y=100)

        Button(self, text='Submit',
                bg='#11ff11', font=('arial', 20, 'bold'),
                command=lambda: self.app()).place(x=200, y=150)
        self.label = Label(self , bg = '#00ff00') # Keep a reference to the image to prevent garbage collection
        self.label.place(x=150, y=200)

    def app(self):
        e1 = self.en1.get()
        e2 = self.en2.get()
        qr = qrcode.make(e2)
        os.makedirs('/home/shared/qrcodes', exist_ok=True)
        qr.save(os.path.join('/home/shared/qrcodes', f'{e1.lower()}.png'))

        image = Image.open(f'/home/shared/qrcodes/{e1.lower()}.png')
        image = image.resize((200, 200))  # Resize the image if needed
        photo = ImageTk.PhotoImage(image)

        label = Label(self, image=photo)
        # label.image = photo  # Keep a reference to the image to prevent garbage collection
        # label.place(x=100, y=200)
        self.label.config(image=photo)
        self.label.image= photo
        self.label.place(x=150, y=200)

if __name__ == '__main__':
    main('500x500', 'QRCode Generator').mainloop()

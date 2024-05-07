import cv2
from tkinter import *
from PIL import Image, ImageTk
import random
# import os

# Initialize global variables
is_recording = False
out = None
frame = None
def show_and_hide_label(text_input):
    l = Label(root,text=text_input,bg='#000',fg='#00fffb',font=('arial',15,'bold'))
    l.pack()
    root.after(500,lambda : l.place_forget())

# Function to take a photo
def take_photo():
    global frame
    if frame is not None:
        # Generate a unique filename
        filename = f"/home/islam/Pictures/photo_{random.randint(1000, 9999)}.png"
        cv2.imwrite(filename, frame)
        show_and_hide_label("Saved Photo .")
        # You can add a label to show the "Saved" message if you want

# Function to stop recording
def stop_recording():
    global is_recording, out
    if is_recording:
        is_recording = False
        out.release()
        show_and_hide_label("Saved Video .")

# Function to start recording
def start_recording():
    global is_recording, out, frame
    if frame is not None:
        is_recording = True
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
        show_and_hide_label("Startded Recording")

# Initialize the main window
root = Tk()
root.config(background='#000000')
root.attributes('-zoomed', True)
root.resizable(False, False)
root.title('Camera')

# Create a label to display the video frames
label = Label(root, width=1580, height=710, bg='#ffffff')
label.pack()

# Load an image for the photo button
imagel = Image.open('/home/shared/Islam-Projects/Python/gui-apps/camera/pngegg.png')  # Update this path to the image you want to use
image = imagel.resize((100, 60))  # Resize the image if needed
photo = ImageTk.PhotoImage(image)

# Create buttons for taking a photo and starting/stopping recording
Button(root, image=photo, command=take_photo, bg='#000000').pack()
Button(root,text="Start Recording",font=("arial",15,"bold"), command=start_recording, bg='#ff0000').pack(side=LEFT)
Button(root,text="Stop Recording",font=("arial",15,"bold"), command=stop_recording, bg='#ffffff').pack(side=RIGHT)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Function to update the video frame on the GUI
def update_frame():
    global frame, is_recording, out
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (1570, 700))
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        if is_recording:
            out.write(frame)  # Write the frame to the video file if recording
    root.after(1, update_frame)

# Start updating the video frame
update_frame()

# Start the GUI main loop
root.mainloop()

# Release resources
cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()

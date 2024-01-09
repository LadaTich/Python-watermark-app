from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


window = Tk()
window.config(width=700, height=500)
window.title("Watermark app")
window.iconbitmap("icon.ico")

logo = PhotoImage(file="logo.png")
logo_label = Label(image=logo)
logo_label.grid(row=0, column=0, columnspan=1)

def image_open():
    global file_path
    file_path = filedialog.askopenfilename()

open_file_button = Button(text="Open image", command=image_open)
open_file_button.grid(row=2, column=0)

try:
    img = Image.open(file_path)
except:
    img = Image.open("upload_image.png")

img.thumbnail((400, 200))

original = ImageTk.PhotoImage(img)

image_label = Label(image=original)
image_label.grid(row=1, column=0, columnspan=1)
window.mainloop()


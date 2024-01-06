from tkinter import *
from tkinter import filedialog
from PIL import Image


window = Tk()
window.config(width=700, height=500)
window.title("Watermark app")
window.iconbitmap("icon.ico")

logo = PhotoImage(file="logo.png")
logo_label = Label(image=logo, )
logo_label.grid(row=0, column=1)

file_path = filedialog.askopenfilename()

# with open(f"{file_path}") as original:

original = Image.open(f"{file_path}")



window.mainloop()


from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from tkinter.filedialog import asksaveasfile 

from PIL import Image, ImageTk, ImageDraw, ImageFont
from PIL import *

window = Tk()
window.config(width=700, height=500, padx=20, pady=20)
window.title("Watermark app")
window.iconbitmap("icon.ico")

logo = PhotoImage(file="logo.png")
logo_label = Label(image=logo)
logo_label.grid(row=0, column=0, columnspan=3)



def image_open():
    global FILE_PATH
    FILE_PATH = filedialog.askopenfilename()

    try:
        img = Image.open(FILE_PATH)
        img.thumbnail((400, 200))
        img.save("thumbnail.png")
    
        thumbnail = ImageTk.PhotoImage(file="thumbnail.png")
        image_label.config(image=thumbnail)
        image_label.image = thumbnail
    except UnidentifiedImageError:
        messagebox.showwarning("Watermark app", "Unsupported file type!")
        image_open()
    except AttributeError:
        None


def watermark_add():
    try:
        img = Image.open(FILE_PATH).convert("RGBA")
        txt = Image.new('RGBA', img.size, (255,255,255,0))

        font = ImageFont.truetype("arial.ttf", 50)
        d = ImageDraw.Draw(txt)

        position = ((img.size[0] / 2), (img.size[1] / 2))

        window.withdraw()
        
        global wm_text
        try:
            wm_text = simpledialog.askstring(title="Watermark", prompt="Enter watermark text:")
            d.text((position), wm_text, anchor="mm", font=font, fill=(0, 0, 0, 30))

            combined = Image.alpha_composite(img, txt) 

            window.deiconify()

            combined.thumbnail((400, 200))
            combined.save("thumbnail.png")

            thumbnail = ImageTk.PhotoImage(file="thumbnail.png")
            image_label.config(image=thumbnail)
            image_label.image = thumbnail
        except TypeError:
            window.deiconify()
        
    except NameError:
        messagebox.showwarning("Watermark app", "You must select a file first!")
    
    
def save():
    try:
        img = Image.open(FILE_PATH).convert("RGBA")
        txt = Image.new('RGBA', img.size, (255,255,255,0))
        
        font = ImageFont.truetype("arial.ttf", 100)
        d = ImageDraw.Draw(txt)

        position = ((img.size[0] / 2), (img.size[1] / 2))

        
        try:
            d.text((position), wm_text, anchor="mm", font=font, fill=(0, 0, 0, 30))
            combined = Image.alpha_composite(img, txt)

            save_file = filedialog.asksaveasfilename(title="Save Image As", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if save_file:
                    combined.save(save_file)
                    messagebox.showinfo("Watermark app", "File saved.")
        except NameError:
                messagebox.showinfo("Watermark app", "You didn't add your watermark!")

                save_file = filedialog.asksaveasfilename(title="Save Image As", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
                if save_file:
                    img.save(save_file)
                    messagebox.showinfo("Watermark app", "File saved.")
        except TypeError:
            messagebox.showinfo("Watermark app", "You didn't add your watermark!")

            save_file = filedialog.asksaveasfilename(title="Save Image As", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if save_file:
                img.save(save_file)
                messagebox.showinfo("Watermark app", "File saved.")

    except NameError:
        messagebox.showwarning("Watermark app", "You must select a file first!")


image_label = Label()
image_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    

open_file_button = Button(text="Open file", command=image_open, padx=5, pady=5)
open_file_button.grid(row=2, column=0, padx=5, pady=5)

watermark_button = Button(text="Add watermark", command=watermark_add, padx=5, pady=5)
watermark_button.grid(row=2, column=1, padx=5, pady=5)

save_button = Button(text="Save image", command=save, padx=5, pady=5)
save_button.grid(row=2, column=2, padx=5, pady=5)

mainloop()


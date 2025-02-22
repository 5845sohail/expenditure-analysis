import qrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox




# defing funtion
def createQR(*args):
    data = text_entry.get()
    
    if data:
        image = qrcode.make(data)
        resized_image = image.resize((210,210))
        tkimage = ImageTk.PhotoImage(resized_image)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0,anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
        
    else:
        messagebox.showwarning("Error", "Enter some Data First")

def saveQR(*args):
    data = text_entry.get()
    
    if data:
        image = qrcode.make(data)
        resized_image = image.resize((280,250))
        
        path = filedialog.asksaveasfilename(defaultextension=".png")
        
        if path:
            resized_image.save(path)
            messagebox.showinfo("Success", "QR Code is Saved.")
    else:
        messagebox.showwarning("Error", " Enter some Data First")
        



# creaing GUI

root = tk.Tk()
root.title("QR code generator")
root.geometry("300x380") #wxh
root.config(bg="white")
root.resizable(0,0)


# creatiing a frame
frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=280, height=250)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=260, width=280, height=100)

filepath =Image.open("qrCodeCover.png")
cover_img = ImageTk.PhotoImage(filepath)

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0, 0,anchor=tk.NW, image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>",saveQR)
qr_canvas.pack(fill=tk.BOTH)


#text entry
text_entry = ttk.Entry(frame2, width=26, font=("Sitka small" ,11), justify=tk.CENTER)
placeholder_text = "Enter your text here..."
text_entry.insert(0, placeholder_text)
text_entry.bind("<Return>",createQR)
text_entry.place(x=5,y=5)

# creating buttons
btn1 = ttk.Button(frame2,text="Create",width=5,command=createQR)
btn1.place(x=2,y=50)

btn2 = ttk.Button(frame2,text="Save",width=5,command=saveQR)
btn2.place(x=95,y=50)

btn3 = ttk.Button(frame2,text="Exit",width=5,command=root.quit)
btn3.place(x=185,y=50)

root.mainloop()
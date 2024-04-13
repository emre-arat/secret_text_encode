import tkinter
from cryptography.fernet import Fernet
from PIL import ImageTk,Image
from Cryptodome.Cipher import AES
from tkinter import messagebox


import base64

window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(300,600)

png = Image.open("secret.png")
aaa = png.resize((200,200))
img = ImageTk.PhotoImage(aaa)
panel = tkinter.Label(window,image=img)
panel.pack()




label1 = tkinter.Label(text="Enter your title.",font=("Arial",15,"normal"))
label1.pack()
box1 = tkinter.Entry(width=30)
box1.pack()
label2 = tkinter.Label(text="Enter a secret text.",font=("Arial",15,"normal"))
label2.pack()
text_box = tkinter.Text(width=30,height=10)
text_box.pack()
label3 = tkinter.Label(text="Enter a secret key.",font=("Arial",15,"normal"))
label3.pack()
box2 = tkinter.Entry(width=30)
box2.pack()
def save_text(title,data):
    with open("secret.txt","a",encoding='utf-8') as ttt:
        ttt.write(title + " :" + "\n" + str(data) + "\n")
def decripy_func():
    text = text_box.get("1.0", tkinter.END)
    key = box2.get()
    if key == "emrearat":
        result = base64.b64decode(text)
        result_text = tkinter.Label(text=result)
        result_text.pack()
    else:
        tkinter.messagebox.showinfo("ERROR", "Enter key!!")

def encript_func():

    title = box1.get()
    text = text_box.get("1.0",tkinter.END)
    key = box2.get()

    if title == "" or text == "" or key =="":
        tkinter.messagebox.showinfo("ERROR", "Enter all data")
    elif key == "emrearat":
        enc_text = base64.b64encode(text.encode("utf-8"))
        save_text(title, enc_text)
    else:
        tkinter.messagebox.showinfo("ERROR", "Enter all data")

result = ""
dec_button = tkinter.Button(text="decript",command=decripy_func)
enc_button = tkinter.Button(text="encript",command=encript_func)


dec_button.pack()
enc_button.pack()
window.mainloop()

from tkinker import*
from tkinker import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
Image = ImageTk.PhotoImage(upload)
label = Label(root, image = image, bg = "light blue")
label.place(x=180, y=20)

label1 = Label(root,
               text="hey user! welcome to the denomination counter application")
bg="light blue"
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msgbox = messagebox.showinfo(
        "alert", "do you want to calculate the denomination count?")
    if msgbox == "ok":
        topwin()
        button1 = Button(root,
                         text="lets get started")
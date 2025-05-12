from tkinker import *
from tkinker.filedialog import askopenfilename, askscsveasfilename

window = Tk()
window.title("codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window,columnconfigure(1, minsize=800, weight=1)

def open_file():
    """open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with oprn(filepath, "r")as input_file:
        text = input.file.read()

    txt_edit.insert(END, text)
    input_file.close()
    window.title(f"codingal's text editor - {filepath}")

def save_file():
    filepath = askopenfilename(
        defaultextension=".txt",
        filetypes=[("text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit = Text(window)
    fr_button = Frame(window, relief=RAISED, bg=2)
    btn_open = Button(fr_button, text="Open", command=open_file)
    btn_save = button(fr_button, text="save as...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5 pady=5)
    btn_save.grid()

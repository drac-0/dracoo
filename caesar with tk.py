import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="yellow")
window.geometry("400x500")
window.title("CAESAR DECRYPT")

#VARBBB
kalimat = tk.StringVar()
shift = tk.IntVar()
leftright = tk.StringVar()

#membuat layer untuk meletakkan tombol
frame = ttk.Frame(window)
frame.pack(
    padx=10,
    pady=10,
    fill='x',
    expand=True
)

#input label and entry text
labeltext = tk.Label(frame,text="Masukkan text yang ingin di-decrypt")
labeltext.pack(
    padx=10,
    pady=10,
)

inputtext = tk.Entry(frame,textvariable=kalimat)
inputtext.pack(
    padx=10,
    pady=10,
    fill='x',
    expand = True
)

#input label and entry shift
labeltext = tk.Label(frame,text="Masukkan jumlah pergeseran")
labeltext.pack(
    padx=10,
    pady=10,
)

inputtext = tk.Entry(frame,textvariable=shift)
inputtext.pack(
    padx=10,
    pady=10,
    fill='x',
    expand = True
)

#left and wrong
ops1 = tk.Radiobutton(frame,text='left', variable=leftright, value=1)
ops1.pack(padx=10,pady=10,fill='x',expand=True)

ops2 = tk.Radiobutton(frame,text='right', variable=leftright, value=0)
ops2.pack(padx=10,pady=10,fill='x',expand=True)

#output entry NIGGA
hasil_label = tk.Label(frame, text="", background="white", anchor="center")
hasil_label.pack(padx=10, pady=10, fill='x', expand=True)

#logic func :DDD
def caesar_decrypt():
    kalimatinput = kalimat.get()
    shiftinput = shift.get()
    result = []
    acleftright = int(leftright.get())
    if acleftright == 1 :
        for char in kalimatinput:
            if char.isupper():
                b = (ord(char) - shiftinput - 65) % 26 + 65
                result.append(chr(b))
            elif char.islower():
                b = (ord(char) - shiftinput - 97) % 26 + 97
                result.append(chr(b))
            else:
                result.append(char)
        decrypted_text = ''.join(result)

    else :
        for char in kalimatinput:
            if char.isupper():
                b = (ord(char) + shiftinput - 65) % 26 + 65
                result.append(chr(b))
            elif char.islower():
                b = (ord(char) + shiftinput - 97) % 26 + 97
                result.append(chr(b))
            else:
                result.append(char)
        decrypted_text = ''.join(result)

    
    return ''.join(result)

#output section
def show():
    hasil_label.config(text=caesar_decrypt())


#line button keluar
decryptbut = tk.Button(frame,text="DECRPYT", command=show)
decryptbut.pack(padx=10,pady=10,fill='x',expand=True)

tombolquit = tk.Button(frame,text="KMS",command=window.destroy)
tombolquit.pack(padx=10,pady=10,fill='x',expand=True)

window.mainloop()
import tkinter as tk
from tkinter  import ttk

window = tk.Tk()
window.config(bg="white")
window.geometry('400x500')
window.title("personal outcome note")


#varbgina
kalimat = tk.StringVar()
nominal = tk.IntVar()
date = tk.StringVar()

frame = ttk.Frame(window)
frame.pack(
    padx = 10,
    pady = 10,
    fill = 'x',
    expand = True
)
with open("D:\\code\\actual.py\\nominal.txt", 'r') as f:
    a = str(f.read())
    main = tk.Label(frame, text = a)
    main.pack(
        padx=20,
        pady=20
    )
    


#input pengeluaran
labeltext1 = tk.Label(frame, text = "masukkan jumlah pengeluaran")
labeltext1.pack(
    padx = 10,
    pady = 10
)

inputtext1 = tk.Entry(frame, textvariable=nominal)
inputtext1.pack(
    padx = 10,
    pady = 10,
    fill = 'x',
    expand = True 
)

labeltext2 = tk.Label(frame, text = "masukkan alasan pengeluaran")
labeltext2.pack(
    padx = 10,
    pady = 10
)

inputtext2 = tk.Entry(frame, textvariable=kalimat)
inputtext2.pack(
    padx = 10,
    pady = 10,
    fill = 'x',
    expand = True 
)

labeltext3 = tk.Label(frame, text = "masukkan tanggal")
labeltext3.pack(
    padx = 10,
    pady = 10
)

inputtext3 = tk.Entry(frame, textvariable=date)
inputtext3.pack(
    padx = 10,
    pady = 10,
    fill = 'x',
    expand = True 
)

def getdata() :
    inputa=nominal.get()
    inputb=kalimat.get() 
    inputc=date.get()
    with open("(path)", "r") as f:
        duit = f.read()
        sisa = int(duit) - inputa

    with open("(path)", 'a') as f :
        f.write(f"\n{duit} - {inputa} = {sisa} \n{inputb}, tanggal {inputc}")

    with open("(path)", 'w') as f :
        f.write(str(sisa))
    
    main.config(text=str(sisa))

update = tk.Button(frame,text='update',command=getdata)
update.pack(
    padx=10,
    pady=10,
    fill='x',
    expand = True
)

window.mainloop()
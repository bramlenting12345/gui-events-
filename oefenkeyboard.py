from cProfile import label
import tkinter as tk
import time 

tijd = 30

hoofd_vak = tk.Tk()
hoofd_vak.geometry("300x300")

def timers(tijd):
    while tijd > 0:
        time.sleep(1)
        tijd = tijd - 1
        label_tijd.update()
        label_tijd.configure(text=tijd)
        
        


start = tk.Button(hoofd_vak,text="strat",padx=2,pady=3,bg="red",command=lambda:timers(tijd))
label_tijd = tk.Label(hoofd_vak,text=tijd,bg="silver")
label_tijd.pack()
start.pack()


hoofd_vak.mainloop()
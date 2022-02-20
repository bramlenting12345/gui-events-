
import tkinter as tk 
from random import randint
import time 
from tkinter import messagebox

# ==========================================={-list aanmaak-}==========================================

kleuren = []
timer = [20]
punten = [0]
tijd = 30
# ============================================{-hoofdscherm aanmaak-}======================================

hoofd_scherm = tk.Tk()
hoofd_scherm.geometry("400x400")
hoofd_scherm.configure(bg="gray")

# ==========================================={-aanmaak labels-}=================================================

label_a = tk.Label(
    hoofd_scherm,
    text="druk op a",
    bg= "white",
    fg='black',
    padx=30,
    pady=20
)
label_w = tk.Label(
    hoofd_scherm,
    text="druk op w",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)

label_s = tk.Label(
    hoofd_scherm,
    text="druk op s",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)
label_d = tk.Label(
    hoofd_scherm,
    text="druk op d",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)
label_onclick = tk.Label(
    hoofd_scherm,
    text="Oneclick",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)
label_dubbel_click = tk.Label(
    hoofd_scherm,
    text="Dubbelclick",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)
label_drie_dubbel_click = tk.Label(
    hoofd_scherm,
    text="Drie dubbel click",
    bg= "white",
    fg= "black",
    padx=30,
    pady=20
)
    
    
# ========================================{-def actie label a-}===============================================

def actie_label_a():
    knop_start.destroy()
    boven_balk.configure(text=("punten",punten))
    kleuren.append('#%06X' % randint(0, 0xFFFFFF))
    label_a.configure(bg=kleuren[0])
    
    hoofd_scherm.bind("a",actie_label_w)
    label_a.pack()
    label_a.place(x=randint(50,300),y=randint(50,300))
    
    
# ============================================{-def actie label a-}================================================
#      
def actie_label_w(event):
    hoofd_scherm.unbind("a")
    label_drie_dubbel_click.place_forget()
    label_a.place_forget()

    punten[0] = punten[0] + 1
    boven_balk.configure(text=("punten",punten))

    kleuren[0]='#%06X' % randint(0, 0xFFFFFF)
    label_w.configure(bg=kleuren[0]) 
    
    hoofd_scherm.bind("w",actie_label_s)
    label_w.pack() 
    label_w.place(x=randint(50,300),y=randint(50,300))

# ================================================={-def actie label w-}==============================================

def actie_label_s(event):
    hoofd_scherm.unbind("w")
    label_w.place_forget()

    punten[0] = punten[0] + 1
    boven_balk.configure(text=("punten",punten))

    kleuren[0]='#%06X' % randint(0, 0xFFFFFF)
    label_s.configure(bg=kleuren[0])
    
    hoofd_scherm.bind("s",actie_label_d)
    label_s.pack() 
    label_s.place(x=randint(50,300),y=randint(50,300))

# ==================================================={-def sctie label s-}===================================
def actie_label_d(event):
    hoofd_scherm.unbind("s")
    label_s.place_forget()

    punten[0] = punten[0] + 1
    boven_balk.configure(text=("punten",punten))

    kleuren[0]='#%06X' % randint(0, 0xFFFFFF)
    label_d.configure(bg=kleuren[0])
    
    hoofd_scherm.bind("d",actie_label_onclick)
    label_d.pack() 
    label_d.place(x=randint(50,300),y=randint(50,300))

# ========================================={-def actie label d-}======================================================

def actie_label_onclick(event):
    hoofd_scherm.unbind("d")
    label_d.place_forget()

    punten[0] = punten[0] + 1
    boven_balk.configure(text=("punten",punten))

    kleuren[0] ='#%06X' % randint(0, 0xFFFFFF)
    hoofd_scherm.bind("<Button-1>",actie_label_dubbel_click)
    label_onclick.configure(bg=kleuren[0])
    

    label_onclick.pack() 
    label_onclick.place(x=randint(50,300),y=randint(50,300))

# ========================================{-actie label dubbel click-}=======================
def actie_label_dubbel_click(event):
    hoofd_scherm.unbind("<Button-1>")
    label_onclick.place_forget()

    punten[0] = punten[0] + 2
    boven_balk.configure(text=("punten",punten))

    kleuren[0]='#%06X' % randint(0, 0xFFFFFF)
    hoofd_scherm.bind("<Double-Button-1> ",actie_label_drie_dubbel_click)  # =====
    label_dubbel_click.configure(bg=kleuren[0])
    

    label_dubbel_click.pack() 
    label_dubbel_click.place(x=randint(50,300),y=randint(50,300)) 

#=============================================================================================

def actie_label_drie_dubbel_click(event):
    hoofd_scherm.unbind("<Double-Button-1>")
    label_dubbel_click.place_forget()

    punten[0] = punten[0] + 2
    boven_balk.configure(text=("punten",punten))

    kleuren[0]='#%06X' % randint(0, 0xFFFFFF)
    hoofd_scherm.bind("<Triple-Button>",actie_label_w)  
    label_drie_dubbel_click.configure(bg=kleuren[0])
    

    label_drie_dubbel_click.pack() 
    label_drie_dubbel_click.place(x=randint(0,300),y=randint(0,300)) 

# ========================================={-hoofd programma-}=================================================print
knop_start = tk.Button(hoofd_scherm,text="druk op start om te beginnen",padx=20,pady=10,command=actie_label_a)
knop_start.place(x=95, 
                y=190,
                    )

boven_balk=tk.Label(hoofd_scherm,bg="black",padx=200, pady=8,text=("punten",punten),fg="white")
boven_balk.pack()

label_tijd = tk.Label(hoofd_scherm,text=(tijd,"timer"),fg="black")
label_tijd.pack()

while tijd > 0:
    time.sleep(1)
    tijd = tijd - 1
    label_tijd.update()
    label_tijd.configure(text=(tijd,"timer"))
    label_tijd.pack()
    if tijd < 5:
        label_tijd.configure(bg="orange")

    if tijd == 0:
        berichten = messagebox.askyesno("de tijs is om ", "uw heeft " + str(punten[0])+ " punten" + " wilt u nog een keer : ?")
        if berichten == True:
            tijd = 30
            label_tijd.configure(bg="white")
            actie_label_a()
        else:
            exit()    
            
        

hoofd_scherm.mainloop()


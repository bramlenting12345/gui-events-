from cgitb import text
from logging import root
import tkinter as tk

# Kopieer het programma Clicker v1 in deze repository en update deze met de volgende specificaties:

# Als je met je muis over het label gaat wordt de achtergrond van het scherm geel worden ongeacht wat hij was (groen, grijs of rood).
# Als je met je muis van het label af gaat moet de kleur weer als daarvoor worden (groen, grijs of rood)

opteller = [0]
ORGINAL_COLLOR = "grey"
last_click = None

# ...............................................................................

def optellen_up(opteller):
    global last_click
    opteller[0] = opteller[0] + 1
    teller.configure(text=opteller[0])
    last_click = "up"

    opteller_up = opteller[0]
    if opteller_up > 0:
        clicker.configure(bg="green")

    if opteller_up < 0:
        clicker.configure(bg="red")
    
# ...................................................................................

def afteller_down(opteller):
    global last_click
    opteller[0] = opteller[0] - 1
    teller.configure(text=opteller[0])
    opteller_up = opteller[0]
    last_click = "down"
    
    if opteller_up > 0:
        clicker.configure(bg="green")

    if opteller_up < 0:
        clicker.configure(bg="red")

# ........................................................................................
    
def verranderen_geel(event):
    clicker["background"] = "yellow"

# .........................................................................................

def verranderen_vorrige_kleur(event):
    kleur_switch = opteller[0]
    if kleur_switch > 0:
        clicker["background"] = "green"

    if kleur_switch < 0 :
        clicker["background"] = "red"    

# .............................................................................................

def vervoudig_label(event):
    global last_click
    if last_click == "up":
        teller.configure(text=opteller[0] * 3)

    if last_click == "down":
        teller.configure(text=opteller[0] / 3)

# ...............................................................................................

clicker=tk.Tk() 
clicker.title("place() methode") 
clicker.geometry("300x300")
clicker.configure(bg="grey")

# ................................................................................................

button_up=tk.Button(clicker, text="UP",padx=80,pady=2,command=lambda:optellen_up(opteller))
button_up.place(x=60, 
                y=40,)

button_down=tk.Button(clicker, text="down",padx=80,pady=2,command=lambda:afteller_down(opteller))
button_down.place(x=50, 
                  y=220,)                

# ...................................................................................................

teller = tk.Label(clicker,bg="white",text=opteller,padx=85,pady=2)
teller.place(relx = 0.5,
             rely = 0.5,
             anchor = 'center')

# .....................................................................................................

teller.bind("<Double-Button-1 >",vervoudig_label)

# ......................................................................................................

teller.bind("<Enter>",verranderen_geel)
teller.bind("<Leave>",verranderen_vorrige_kleur)

# ......................................................................................................

clicker.mainloop()




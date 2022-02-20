from cgitb import text
from logging import root
import tkinter as tk
import keyword
# Als je op de + of het pijltje omhoog van je toetsenbord drukt word de zelfde functionaliet afgevuurd als op de up button.
# Als je op de – of het pijltje omlaag van je toetsenbord drukt word de zelfde functionaliet afgevuurd als op de down button.
# Als je op de spatie balk klikt word dezelfde functionaliteit afgevuurd als of je dubbel klikt op het label


opteller = [0]
ORGINAL_COLLOR = "grey"
last_click = None

# .................................{-def optellen up-}......................................................................

def optellen_up():
    global opteller
    global last_click
    opteller[0] = opteller[0] + 1
    teller.configure(text=opteller[0])
    last_click = "up"

    opteller_up = opteller[0]
    if opteller_up > 0:
        clicker.configure(bg="green")

    if opteller_up < 0:
        clicker.configure(bg="red")
    
# .................................{-def aftellen down-}..................................................................

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

# .....................................{-def verranderen geel-}............................................................
    
def verranderen_geel(event):
    clicker["background"] = "yellow"

# ......................................{-def verranderen vorrige kleur-}..................................................

def verranderen_vorrige_kleur(event):
    kleur_switch = opteller[0]
    if kleur_switch > 0:
        clicker["background"] = "green"

    if kleur_switch < 0 :
        clicker["background"] = "red"    

# ........................................{-def vervoudig label-}...........................................................

def vervoudig_label(event):
    global last_click
    if last_click == "up":
        teller.configure(text=opteller[0] * 3)

    if last_click == "down":
        teller.configure(text=opteller[0] / 3)

# .........................................{-def keyboard omhoog-}..........................................................

def keyboard_omhoog(event):
    global opteller
    global last_click
    opteller[0] = opteller[0] + 1
    teller.configure(text=opteller[0])
    last_click = "up"

    opteller_up = opteller[0]
    if opteller_up > 0:
        clicker.configure(bg="green")

    if opteller_up < 0:
        clicker.configure(bg="red")

# .........................................{-keyboard omlaag-}-------------------------------------------------------------


def keyboard_omlaag(event):
    global last_click
    opteller[0] = opteller[0] - 1
    teller.configure(text=opteller[0])
    opteller_up = opteller[0]
    last_click = "down"
    
    if opteller_up > 0:
        clicker.configure(bg="green")

    if opteller_up < 0:
        clicker.configure(bg="red") 

# ..........................................{-cliker aanmaak scherm tk-}.....................................................

clicker=tk.Tk() 
clicker.title("place() methode") 
clicker.geometry("300x300")
clicker.configure(bg="grey")

# ............................................{-aanmaak button up met tk-}....................................................

button_up=tk.Button(clicker, text="UP",padx=80,pady=2,command=lambda:optellen_up())
button_up.place(x=60, 
                y=40,)

button_down=tk.Button(clicker, text="down",padx=80,pady=2,command=lambda:afteller_down(opteller))
button_down.place(x=50, 
                  y=220,)                

# ..............................................{-aanmaak teller met tk-}.....................................................

teller = tk.Label(clicker,bg="white",text=opteller,padx=85,pady=2)
teller.place(relx = 0.5,
             rely = 0.5,
             anchor = 'center')
            
# ...............................................{-dubbel click commando-}......................................................

teller.bind("<Double-Button-1 >",vervoudig_label)

# ................................................{-Enter en leave command muis-}......................................................

teller.bind("<Enter>",verranderen_geel)
teller.bind("<Leave>",verranderen_vorrige_kleur)

# .................................................{-keyboad avents up button -}.....................................................

clicker.bind("+",keyboard_omhoog)
clicker.bind("-",keyboard_omlaag)

clicker.mainloop()




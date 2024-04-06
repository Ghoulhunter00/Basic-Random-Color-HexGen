"""Author: Nathan Uhl
A random color generator based off of the seeded RNG model.
Generator outputs colors that can be used to provide color palates for guis
Can output up to 5 at a time without needing to be cleared."""

import random
import tkinter as Tk
import string

def color_hex():
    x = list(string.hexdigits)
    random.shuffle(x)
    y = ''.join(x[:6])
    return y
def Color_Generation():
    Val = color_hex()
    output.insert(Tk.END, Val, "\n")
def Clear():
    output.delete("1.0", Tk.END)

MainWin = Tk.Tk()
MainWin.title("Color Generator")
MainWin.config(bg= '#7F00FF', relief='raised')
button = Tk.Button(MainWin, text = "Generate", command=Color_Generation,fg='#FFFFFF',bg='#000000',relief= 'sunken', height=1, width=7)
button.pack(side=Tk.TOP)
button2 = Tk.Button(MainWin, text= "Clear", command=Clear, fg='#FFFFFF',bg='#000000',relief= 'sunken', height=1, width= 6)
button2.pack(side=Tk.TOP)
output = Tk.Text(MainWin, bg='#D4AF37', fg="Black", height= 1, width= 6)
output.pack()

MainWin.mainloop()
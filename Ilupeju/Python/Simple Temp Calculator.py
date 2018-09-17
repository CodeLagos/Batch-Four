# PROJECT NAME - SIMPLE TEMPERATURE CONVERTER.
# NAME - AKINTOLA STEPHEN IYANU
# EMAIL - sakintola351@gmail.com
# PHONE NUMBER - 09092226607
# CENTER -  ILUPEJU
# CLASS - AFTERNOON CLASS.

from tkinter import *

def convert_fahr():
    words = fbtext.get()
    ftemp = float(words)
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % ( tocel( ftemp) ) )
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % ( tokel(tocel ( ftemp) ) ) )
    return

def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % ( tofahr( ctemp) ) )
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % ( tokel( ctemp) ) )

def convert_kel():
    words = kbtext.get()
    ktemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % ( tofahr( ktoc (ktemp ) ) ) )
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % ( ktoc( ktemp) ) )

def tocel(fahr):
    return (fahr-32) * 5.0 / 9.0

def tofahr(cel):
    return cel * 9.0 / 5.0 + 32

def ktoc(kel):
    return kel - 273.15

def tokel(cel):
    return cel + 273.15

app = Tk()
app.title('CONVERTER')
app.geometry('400x200')

fahrlabel = Label(app, text = 'FAHRENHEIT', font = ('calibri') )
fahrlabel.grid(row = 0, column = 0, padx = 25, pady = 10)

cellabel = Label(app, text = 'CELCIUS', font= ('calibri') )
cellabel.grid(row = 1, column = 0, padx = 5, pady = 10)

kellabel = Label(app, text = 'KELVIN', font = ('calibri') )
kellabel.grid(row = 2, column = 0, padx = 5, pady = 10)

# Entry point for the fahrenheit
fbtext = DoubleVar()
fbtext.set('')
fahrbox = Entry(app, textvariable = fbtext)
fahrbox.grid(row = 0, column = 1, padx = 5, pady = 5)

# Entry point for the Celcius
cbtext = DoubleVar()
cbtext.set('')
celbox = Entry(app, textvariable = cbtext)
celbox.grid(row = 1, column = 1, padx = 5, pady = 5)

# Entry point for the Kelvin
kbtext = DoubleVar()
kbtext.set('')
kelbox = Entry(app, textvariable = kbtext)
kelbox.grid(row = 2, column = 1, padx = 5, pady = 5)

#Fahrenheit Button
fgobutton = Button(app, text = 'CONVERT', command = convert_fahr, bg='black', fg='white')
fgobutton.grid(row = 0, column = 2, padx = 5, pady = 5)

#Celcius Button
cgobutton = Button(app, text = 'CONVERT', command = convert_cel, bg='black', fg='white')
cgobutton.grid(row = 1, column = 2, padx = 5, pady = 5)

# Kelvin Button
kgobutton = Button(app, text = 'CONVERT', command = convert_kel, bg='black', fg='white')
kgobutton.grid(row = 2, column = 2, padx = 5, pady = 5)

#Exit Button
exitbutton = Button(app, text = 'EXIT', bg='red', fg='white', command = quit)
exitbutton.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan = 3)

app.mainloop()

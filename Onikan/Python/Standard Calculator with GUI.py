#calculator using tkinter
#Afolabi    Jeremiah
#afolabijeremayia@gmail.com

from tkinter import*

root = Tk()

root.geometry("800x400")

root.title("Standard alculator ")

text_Input = StringVar()
operator =""

self = Frame(root, width = 20,height = 10, relief=FLAT)
self.pack(expand=YES)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""

txtDisplay = Entry(self,font=('verdana', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="sky blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2,column=2)
Addition=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2,column=3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn4=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3,column=2)
Subtraction=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3,column=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4,column=0)
btn2=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4,column=1)
btn3=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4,column=2)
Multiply=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4,column=3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5,column=0)
btnClear=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="C", bg="powder blue", command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="=", bg="powder blue", command=btnEqualsInput).grid(row=5,column=2)
Division=Button(self,padx=16,pady=16,bd=8, fg="black", font=('verdana',20,'bold'),text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5,column=3)


root.mainloop()

#Name: Michael Felix H.
#E-mail: mfhlive@gmail.com
#Purpose of the program: To create a simple payroll calculator that is capable of computing monthly salary of the employees
#Facilitator's Name: Mr. Dotun Onasanya

import datetime
import random
from tkinter import*


root=Tk() #Frame
root.geometry("1600x8000") #Frame Size on the computer screen
root.title("Simple Payroll Calculator") #Name on the title bar
date=datetime.datetime.now() #Current date and time



    
def AddPay():
    x=random.randint(1238,80257) #Automatically generate the random numbers within the specified ranges 
    randomRef=(IDNO.get()),'_',date.strftime('%b-%y'), '_',(str(x)) #Adding Staff ID No, month and year of payment and random number for easy tracking of each payment.
    rand.set(randomRef) #Set the ref into the table


    if (GS.get()==""):
        MGS=0
    else:
        MGS=float(GS.get())


    if (OT.get()==""):
        MOT=0
    else:
        MOT=float(OT.get())


    
    if (YEB.get()==""):
        AYEB=0
    else:
        AYEB=float(YEB.get())



    if (LA.get()==""):
        ALA=0
    else:
        ALA=float(LA.get())

    
    if (OP.get()==""):
        MOP=0
    else:
        MOP=float(OP.get())



    if (MP.get()==""):
        MMP=0
    else:
        MMP=float(MP.get())

        
    if (SP.get()==""):
        MSP=0
    else:
        MSP=float(SP.get())

    if (LD.get()==""):
        MLD=0
    else:
        MLD=float(LD.get())



    if (CD.get()==""):
        MCD=0
    else:
        MCD=float(CD.get())

        
    if (OD.get()==""):
        MOD=0
    else:
        MOD=float(OD.get())
        
    #TOTAL PAYMENTS FOR THE MONTH
    T_Pay = "N", str('%.2f' % (MGS+MOT+AYEB+ALA+MOP))
    TPay= (MGS+MOT+AYEB+ALA+MOP)

    #MINIMUM PAYE @ 1%. 
    #DISCLAIMER: THE 1% COMPUTATION IS INTENDED FOR THIS PROJECT ONLY AND SHOULD NOT BE USED AS A BASIS FOR YOUR PAYE COMPUTATION. KINDLY CONTACT YOUR TAX CONSULTANT.
    Paye = (TPay * 0.01)

    #MONTHLY PENSION @ 8% OF GROSS SALARY
    Pension = (MGS * 0.08)

    #TOTAL DEDUCTIONS FOR THE MONTH
    T_Ded = "N", str('%.2f' %(Paye+Pension+MLD+MOD+MCD))
    TDed=(Paye+Pension+MLD+MOD+MCD)

    #NET PAYMENT 
    NPay = "N", str('%.2f' % (TPay-TDed))

    #INPUTING THE CALCULATED VARIABLES INTO THEIR VARIOUS TABLE
    TP.set(T_Pay)
    MP.set(Paye)
    SP.set(Pension)
    TD.set(T_Ded)
    NP.set(NPay)
    
def Exit():
    root.destroy()

def Clear():
    Names.set("") 
    rand.set("")
    IDNO.set("")
    Position.set("")
    GS.set("")
    OT.set("")
    YEB.set("")
    LA.set("")
    OP.set("")
    TP.set("")
    MP.set("")
    SP.set("")
    LD.set("")
    OD.set("")
    CD.set("")
    TD.set("")
    NP.set("")
    

    
#VARIABLES
Names = StringVar()
rand = StringVar()
IDNO=StringVar()
Position=StringVar()
GS= StringVar()
OT= StringVar()
YEB= StringVar()
LA= StringVar()
OP= StringVar()
TP= StringVar()
MP= StringVar()
SP= StringVar()
LD= StringVar()
OD= StringVar()
CD= StringVar()
TD= StringVar()
NP= StringVar()


A=Frame(root, width=40, relief=RIDGE)
A.pack(side=TOP)

B=Frame(root,width=20,height=8, relief=RIDGE)
B.pack(side=LEFT)


#HEADER AND TIME

lHeadings=Label(A,font=('Dodger',45,'bold'),text="OSHA PRAPRA NIG LTD.",fg="Green",bd=10,justify=CENTER,anchor='w').grid(row=0,column=0)

lInfo=Label(A,font=('arial black', 23,'bold'),text="Payroll Management System",fg="Green",bd=1,anchor='w').grid(row=1,column=0)

lPeriod=Label(A,font=('Tekton Pro Ext', 20, 'italic','bold'),text=('Payslip for', date.strftime('%B, %Y.')),fg="Red",justify=LEFT,anchor='w').grid(row=2,column=0)

lTime=Label(A,font=('Tekton Pro Ext', 11, 'italic','bold'),text=date.strftime('%a. %d %b, %Y. %I:%M:%S%p'),fg="BLACK",justify=LEFT,anchor='w').grid(row=3,column=0)



#PERSONAL DATA

lNames= Label(B, font=('arial',20, 'bold'),text="NAMES",fg="Black",bd=16,anchor="w").grid(row=0, column=0)
tNames=Entry(B, font=('arial',16,'bold'),textvariable=Names,bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=0,column=1)

lIDNO= Label(B, font=('arial',20, 'bold'),text="ID NO.",fg="Black",bd=16,anchor="w").grid(row=0, column=2)
tIDNO=Entry(B, font=('arial',16,'bold'),textvariable=IDNO,bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=0,column=3)

lPosition= Label(B, font=('arial',20, 'bold'),text="POSITION",fg="Black",bd=16,anchor="w").grid(row=0, column=4)
tPosition=Entry(B, font=('arial',16,'bold'),textvariable=Position,bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=0,column=5)




#PAYMENTS
lGS= Label(B, font=('arial', 16, 'bold'),text="Gross Salary",bd=16,anchor="w").grid(row=1, column=0)
tGS=Entry(B, font=('arial',16,'bold'),textvariable=GS,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=1,column=1)


lOT= Label(B, font=('arial', 16, 'bold'),text="Overtime",bd=16,anchor="w").grid(row=2, column=0)
tOT=Entry(B, font=('arial',16,'bold'),textvariable=OT,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=2,column=1)


lYEB= Label(B, font=('arial', 16, 'bold'),text="Bonus",bd=16,anchor="w").grid(row=3, column=0)
tYEB=Entry(B, font=('arial',16,'bold'),textvariable=YEB,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=3,column=1)

lLA= Label(B, font=('arial', 16, 'bold'),text="Leave Allow.",bd=16,anchor="w").grid(row=4, column=0)
tLA=Entry(B, font=('arial',16,'bold'),textvariable=LA,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=4,column=1)

lOP= Label(B, font=('arial', 16, 'bold'),text="Other Payts.",bd=16,anchor="w").grid(row=5, column=0)
tOP=Entry(B, font=('arial',16,'bold'),textvariable=OP,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=5,column=1)



#DEDUCTIONS


lLD= Label(B, font=('arial', 16, 'bold'),text="Loan Ded.",bd=16,anchor="w").grid(row=3, column=2)
tLD=Entry(B, font=('arial',16,'bold'),textvariable=LD,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=3,column=3)

lCD= Label(B, font=('arial', 16, 'bold'),text="Co-Op. Due.",bd=16,anchor="w").grid(row=4, column=2)
tCD=Entry(B, font=('arial',16,'bold'),textvariable=CD,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=4,column=3)

lOD= Label(B, font=('arial', 16, 'bold'),text="Other Ded.",bd=16,anchor="w").grid(row=5, column=2)
tOD=Entry(B, font=('arial',16,'bold'),textvariable=OD,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=5,column=3)


#LAST TAB ORDERS

lReference= Label(B, font=('arial', 16, 'bold'),text="PAY REF.",bd=16,anchor="w").grid(row=1, column=4)
tReference=Entry(B, font=('arial',16,'bold'),textvariable=rand,fg="RED",bd=10,insertwidth=4,bg="Yellow",justify='right').grid(row=1,column=5)

lMP= Label(B, font=('arial', 16, 'bold'),text="PAYE",bd=16,anchor="w").grid(row=1, column=2)
tMP=Entry(B, font=('arial',16,'bold'),textvariable=MP,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=1,column=3)


lSP= Label(B, font=('arial', 16, 'bold'),text="Pension",bd=16,anchor="w").grid(row=2, column=2)
tSP=Entry(B, font=('arial',16,'bold'),textvariable=SP,bd=10,insertwidth=4,bg="Light Green",justify='right').grid(row=2,column=3)

lTP= Label(B, font=('arial', 18, 'bold'),text="TOTAL PAYS",fg="RED",bd=16,anchor="w").grid(row=6, column=0)
tTP=Entry(B, font=('arial',16,'bold'),textvariable=TP,fg="RED",bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=6,column=1)

lTD= Label(B, font=('arial', 16, 'bold'),text="TOTAL DEDS",fg="RED",bd=16,anchor="w").grid(row=6, column=2)
tTD=Entry(B, font=('arial',16,'bold'),textvariable=TD,fg="RED",bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=6,column=3)

lNP= Label(B, font=('arial', 16, 'bold'),text="NET PAY.",fg="RED",bd=16,anchor="w").grid(row=6, column=4)
tNP=Entry(B, font=('arial',16,'bold'),textvariable=NP,fg="RED",bd=10,insertwidth=4,bg="Light Yellow",justify='right').grid(row=6,column=5)


#BOTTONS
AddPaybtn=Button(B,padx=6,pady=5,bd=12,fg="DARK GREEN",font=('arial black',20,'bold'),width=8,text="ADD PAYS",bg="Light Green",command=AddPay).grid(row=7,column=3)

Clearbtn=Button(B,padx=6,pady=5,bd=12,fg="DARK GREEN",font=('arial black',20,'bold'),width=8,text="CLEAR",bg="Light Green",command=Clear).grid(row=7,column=4)

Exitbtn=Button(B,padx=6,pady=5,bd=12,fg="RED",font=('arial black',20,'bold'),width=8,text="EXIT",bg="Light Green",command=Exit).grid(row=7,column=5)


root.mainloop()



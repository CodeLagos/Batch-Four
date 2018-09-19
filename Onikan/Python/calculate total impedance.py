#Name Kotun Abdulfatai .O
#kotun.abdul@gmail.com 09025125590
import math
#A program to calculate the total impedance of a n a.c Cct
r = float (input('the resistance of the resistor is,'))
l = float (input('the value of the inductor is, '))
c = float (input('the value of the capacitor is, '))
f = float (input('the value of the frequency is, '))
v = float (input('the value of the volatage running the circuit,'))

xl= (2*math.pi*f*l)
xc= (1/(2*math.pi*f*c))

z=(math.sqrt(r**2+(xl-xc)**2))
z1=(1/math.sqrt((1/r)**2+(1/xl-1/xc)**2))
cct = str (input('whether series or parallel, ' ))
if cct=='series':
    print ('the total impedance of the cct is', z)
elif cct=='parallel':
    print ('the total impedance of the cct is', z1)
else:
    print ('your spelling of series or parallel is not correct')


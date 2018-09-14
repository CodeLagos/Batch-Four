#Okunola Oluwaseun
#okunola_oluwaseun@yahoo.com
#08131192937
#This Programe is to simulate a race
from turtle import*
from random import randint
from random import shuffle

#To indicate speed and 
speed(30)
penup()
goto(-140, 140)

for step in range(18):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

    

bola = Turtle()
bola.color('purple')
bola.shape('turtle')

bola.penup()
bola.goto(-160, 100)
bola.pendown()




budo = Turtle()
budo.color('blue')
budo.shape('turtle')

budo.penup()
budo.goto(-160, 70)
budo.pendown()




rash = Turtle()
rash.color('green')
rash.shape('turtle')

rash.penup()
rash.goto(-160, 40)
rash.pendown()



tobi = Turtle()
tobi.color('red')
tobi.shape('turtle')

tobi.penup()
tobi.goto(-160, 10)
tobi.pendown()

for turn in range(6):
    bola.right(60)
    budo.right(60)
    rash.right(60)
    tobi.right(60)
    
for turn in range(100):
    bola.forward(randint(1,6))
    budo.forward(randint(1,6))
    rash.forward(randint(1,6))
    tobi.forward(randint(1,6))

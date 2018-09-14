#This program enables my restaurant to calculate revenue
#Name: Mr Babalola Tunde
#Number: 08181620007

orders=int(input("how many orders do you want to make? "))
subtotal =0
for i in range(orders):
    fd1 = 0
    sp1 = 0
    mt1 = 0

    my_order = 0


#first order
    food_order1 = input("Please place your order \n(a) eba N150 \n(b) pounded_yam N200 \n(c) semolina N150 \n(d) fufu N150 \n \n")
    if (food_order1.lower() == "a"):
        fd1 = fd1 + 150
    elif(food_order1.lower() == "b"):
        fd1 = fd1 + 200
    elif(food_order1.lower() == "c"):
        fd1 = fd1 + 150
    elif(food_order1.lower() == "d"):
        fd1 = fd1 + 150
    else:
        print("You Placed no orders")

    qty1a = input("Please choose the quantity \n(a) one \n(b) two \n(c) three \n(d) four \n \n")
    if (qty1a.lower() == "a"):
        fd1 = fd1 * 1
    elif(qty1a.lower() == "b"):
        fd1 = fd1 * 2
    elif(qty1a.lower() == "c"):
        fd1 = fd1 * 3
    elif(qty1a.lower() == "d"):
        fd1 = fd1 * 4
    else:
        print("You Placed no orders")

    soup_order1 = input("Please select your soup \n(a) okra N50 \n(b) egusi N100 \n(c) ewedu N100 \n(d) veg_soup N150 \n \n")
    if (soup_order1.lower() == "a"):
        sp1 = sp1 + 100
    elif(soup_order1.lower() == "b"):
        sp1 = sp1 + 100
    elif(soup_order1.lower() == "c"):
        sp1 = sp1 + 100
    elif(soup_order1.lower() == "d"):
        sp1 = sp1 + 150
    else:
        print("You Placed no orders")

    meat_order1 = input("Please place your order \n(a) beef N250 \n(b) chicken N300 \n(c) fish N250 \n(d) goat N250 \n \n")
    if (meat_order1.lower() == "a"):
        mt1 = mt1 + 250
    elif(meat_order1.lower() == "b"):
        mt1 = mt1 + 300
    elif(meat_order1.lower() == "c"):
        mt1 = mt1 + 250
    elif(meat_order1.lower() == "d"):
        mt1 = mt1 + 250
    else:
        print("You Placed no orders")

    qty1b = input("Please choose the quantity \n(a) one \n(b) two \n(c) three \n(d) four \n \n")
    if (qty1b.lower() == "a"):
        mt1 = mt1 * 1
    elif(qty1b.lower() == "b"):
        mt1 = mt1 * 2
    elif(qty1b.lower() == "c"):
        mt1 = mt1 * 3
    elif(qty1b.lower() == "d"):
        mt1 = mt1 * 4
    else:
        print("You Placed no orders")
    my_order = fd1 + sp1 + mt1
    print("your current order price is #",my_order)
    print("\n")
    
    subtotal = subtotal +  my_order

    
print ("Your subtotal is #", subtotal)
VAT = subtotal * 0.04
print ("Your VAT is #", VAT)
total = subtotal + VAT
print("Your total is #",total)
  


#!/usr/bin/env python3

print ("Welcome to Code Lagos Mobile Store")

#print ("Items In The Store: \n1)Iphone 6:N60,000           2)Iphone 7:N80,000 \n3)Samsung S7:N70,000         4)Samsung S8:N85,000 \n5)Blackberyy Key 1:N85,0000  6)Iphone 5:N40,000    \n7)Iphone SE:N80,000          8)Apple Pad:N120,000 \n9)Samsung Note 1:N85,000    10)Infinix Note 1:N45,0000")
stock = {"iphone6" : 60000, "iphone7" :80000, "samsung S7":70000, "samsung S8":85000, "blackberyy key1":850000, "iphone5":40000    , "iphone se":80000, "apple pad":120000, "samsung note1":85000, "infinix note1":450000}
shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("Enter DONE to stop. Enter HELP for this help. Enter SHOW to see your current list.")

def add_to_list(item):
    shopping_list.append(item)
    print("Added!  {} Items In Your Shopping Basket.".format(len(shopping_list)))

def show_list():
    print("Here's your Shopping Cart:")
    #for item in shopping_list:
     #   print(item)
    tp = 0
    for a in shopping_list:
            for item, price in stock.items():
                if a == item:
                    print(item.title() + ":" + str(price))
                    tp += price
                else:
                    continue
    checkout = input("Would you Like to Check Out: Y | N: ")
    if checkout == "y":
        print("Total price for the items is : " + str(tp))
                    
        print ("Thanks for Shopping With us We Automatically Deducted The Money from your Accounts Without your Knowledge 'Thanks to WCP'")
                
        
def show_stock():
    print("Here's Our Mobile Store:")
    print ("Which of these would you Like to Add to Cart")
    for k, v in stock.items():
        print( k.title() + " : " + str(v))
        


show_help()
show_stock()

while True:
    new_item = input("> ")
    new_item = new_item.lower()
    if new_item == 'done':
        show_list();
       
        break
    elif new_item == 'help':
        show_help()
        continue
    elif new_item == 'show':
        show_list()
        continue
    add_to_list(new_item)
    continue
    

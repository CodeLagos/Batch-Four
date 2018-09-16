
#Name: Victor Raji

#victororaji@gmail.com

print("This program is to enable people receive and transfer money peer-to-peer around the world within minutes without intermediaries.")

#Step 1. Welcome the user
print("Welcome to D'RajPay. The worlds fastest, simplest and cheapest peer_to_peer money transfer application.")

#Step 2. Ask the user to enter their location
print ("SENDERS DETAILS")

senders_country=input("Please enter your country:")
print(senders_country)

#Step 3. Ask the user to enter thier Bank name
bank_name=input("Please enter the name of your Bank:")
print(bank_name)


#Step 4. Ask the user to enter thier bank account number
value=int(input("Please enter your bank account number:"))
print(value)

#Step 5. Ask the user to enter a five digit secret code
code=int(input("Please enter a 5 digit secret number:"))
print("THIS IS THE RECEIVER'S ACCESS CODE:",code)


#Step 6. Ask the user to enter the amount to be transfered
amount=input("Please enter the amount you want to transfer in naira : ")
print("You are transfering N",amount)


#Step 7. Ask the user to enter the receiver's location
print("RECEIVER'S DETAILS")
      
receivers_country=input("Please enter the recevier's country:")
print(receivers_country)

#Step 8. Ask the user to enter the reciever's Bank name
bank_name1=input("Please enter the name of the recevier's Bank:")
print(bank_name1)

#Step 9. Ask the user to enter the recevier's bank account number
receivers_account=int(input("Please enter the recevier's bank account number:"))
print(receivers_account)

a=amount
b=receivers_account
c="You are about to transfer N:"
d="to"
print(c,a,d,b, "Please confirm your transaction details again.")

print("Thank you for choosing D'RajPay... Cheap,Immediate, reliable")

#Step 10. stop

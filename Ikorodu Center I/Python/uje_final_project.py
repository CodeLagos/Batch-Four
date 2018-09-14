# This is a codeLagos project by
# Suleiman Uje
# uje.oshio98@gmail.com
def main():
    print('Welcome to Uje\'s inventory application')
    opt=input('''
What operation would you like to carry out:
(A) Input record
(B) Search records
(C) Display all entries
(D) Modify a record
(E) Delete a record
(F) Display the number of entries
(G) Exit application
''')
    # List all options and corrsponding actions
    # in if statements
    if opt.upper()=='A':
        input_record()
        redo_app()
    elif opt.upper()=='B':
        display_part_record()
        redo_app()
    elif opt.upper()=='C':
        display_all()
        redo_app()
    elif opt.upper()=='D':
        modify_record()
        redo_app()
    elif opt.upper()=='E':
        delete_record()
        redo_app()
    elif opt.upper()=='F':
        display_no_entries()
        redo_app()
    elif opt.upper()=='G':
        print('Thank you for using this application')
def redo_app():
    redo_opt=input('''
Would you like to continue using the application:
(A) Yes
(B) No
''')
    if redo_opt.upper()=='A':
        main()
    elif redo_opt.upper()=='B':
        print('Have a lovely day')
    else:
        print('Invalid selection')
        redo_app()
#This program is to record  the details of
#codelagos participants
def input_record():
    #open the codelagos file with append so that it wont delete old data in file
    class_file=open('codelagos.txt','a')
    again='y'
    while again=='y' or again=='Y':
        first_name=input('First Name: ')
        last_name=input('Last Name: ')
        pho_no=input('Phone Number: ')
        sex=input('Sex: ')
        class_file.write(first_name+'\n')
        class_file.write(last_name+'\n')
        class_file.write(pho_no+'\n')
        class_file.write(sex+'\n')
        again=input('''Do you want to input another participant
Yes=Y
Anything else=No
''')
    class_file.close()
    print('The file has been updated.')
#This program is for determining the number of records in the codelagos file
def display_no_entries():
    count=0
    class_file=open('codelagos.txt','r')
    first_name=class_file.readline()
    # Begin loop to continue reading if first name is not empty
    while first_name!='':
        last_name=class_file.readline()
        pho_no=class_file.readline()
        sex=class_file.readline()
        count+=1
        first_name=class_file.readline()
    class_file.close()
    print('There are',count,'entries in the file')

#This program is to delete a record
def delete_record():
    import os #Required to rename and delete files
    #Create bool variable as flag
    found=False
    #open the codelagos file
    class_file=open('codelagos.txt','r')
    #open the temporary file
    temp_file=open('temp.txt','w')
    search=input('Enter keyword of file to be deleted \
(click Enter to end): ')
    while search!='':
        #read the first records first name field
        first_name=class_file.readline()
        #read the rest of the file
        while first_name!='':
            last_name=class_file.readline()
            pho_no=class_file.readline()
            sex=class_file.readline()
            #strip the \n from the records
            first_name=first_name.rstrip('\n')
            last_name=last_name.rstrip('\n')
            pho_no=pho_no.rstrip('\n')
            sex=sex.rstrip('\n')
            #Write the old records into the temporary file
            if first_name==search or last_name==search or sex==search or pho_no==search:
                #set the found flag to true
                found=True
            else:
                temp_file.write(first_name+'\n')
                temp_file.write(last_name+'\n')
                temp_file.write(pho_no+'\n')
                temp_file.write(sex+'\n')
            #read the next description
            first_name=class_file.readline()
        #close all files
        class_file.close()
        temp_file.close()
        #delete the codelagos file
        os.remove('codelagos.txt')
        #rename the temp file
        os.rename('temp.txt','codelagos.txt')
        if found:
            print('The file has been updated')
        else:
            print('The item was not found in the file')
        found=False
        search=input('Enter keyword of file to be deleted \
(click Enter to end): ')
    if search=='':
        print('Thank you for using this program')
        temp_file.close()
        os.remove('temp.txt')
#This program is to modify data in the records
def modify_record():
    import os #Required to rename and delete files
    #Create bool variable as flag
    found=False
    new_var=input('''
What would you like to change in the entry:
A = First Name
B = Last Name
C = Phone Number
D = Sex
X = Cancel Program
''')
    
    while new_var.upper()=='A' or new_var.upper()=='B' or new_var.upper()=='C' or new_var.upper()=='D' or new_var.upper()=='X':
        if new_var.upper()=='A':
            new_first_name=input('Enter the new first name: ')
            new_last_name=new_pho_no=new_sex=0
        elif new_var.upper()=='B':
            new_last_name=input('Enter the new last name: ')
            new_first_name=new_pho_no=new_sex=0
        elif new_var.upper()=='C':
            new_pho_no=input('Enter the new phone number: ')
            new_first_name=new_last_name=new_sex=0
        elif new_var.upper()=='D':
            new_sex=input('Enter the new sex: ')
            new_first_name=new_last_name=new_pho_no=0
        elif new_var.upper()=='X':
            print('Thank you for using this program.')
            found=0
            break
        else:
            print('Invalid selection.')
        #open the codelagos file
        class_file=open('codelagos.txt','r')
        #open the temporary file
        temp_file=open('temp.txt','a')
        search=input('Enter keyword: ')
        #read the first records first name field
        first_name=class_file.readline()
        #read the rest of the file
        while first_name!='':
            last_name=class_file.readline()
            pho_no=class_file.readline()
            sex=class_file.readline()
            #strip the \n from the records
            first_name=first_name.rstrip('\n')
            last_name=last_name.rstrip('\n')
            pho_no=pho_no.rstrip('\n')
            sex=sex.rstrip('\n')
            #Write the records new or old into the temporary file
            if first_name==search or last_name==search or sex==search or pho_no==search:
                if new_first_name==0:
                    new_first_name=first_name
                if new_last_name==0:
                    new_last_name=last_name
                if new_pho_no==0:
                    new_pho_no=pho_no
                if new_sex==0:
                    new_sex=sex
                #write the modified values into the temp file
                temp_file.write(new_first_name+'\n')
                temp_file.write(new_last_name+'\n')
                temp_file.write(new_pho_no+'\n')
                temp_file.write(new_sex+'\n')
                #set the found flag to true
                found=True
            else:
                temp_file.write(first_name+'\n')
                temp_file.write(last_name+'\n')
                temp_file.write(pho_no+'\n')
                temp_file.write(sex+'\n')
            #read the next description
            first_name=class_file.readline()
        #close all files
        class_file.close()
        temp_file.close()
        #delete the codelagos file
        os.remove('codelagos.txt')
        #rename the temp file
        os.rename('temp.txt','codelagos.txt')
        if found:
            print('The file has been updated')
        else:
            print('The item was not found in the file')
        found=False
        new_var=input('''
What would you like to change in the entry:
A = First Name
B = Last Name
C = Phone Number
D = Sex
X = Cancel Program
''')
#if the search value is found or not display a message
    if found==0:
        print('Good Bye')   
#This program is for displaying all entries in the codelagos file
def display_all():
    # Open the codeLagos file
    class_file=open('codelagos.txt','r')
    first_name=class_file.readline()
    while first_name!='':
        last_name=class_file.readline()
        pho_no=class_file.readline()
        sex=class_file.readline()
        first_name=first_name.rstrip('\n')
        last_name=last_name.rstrip('\n')
        pho_no=pho_no.rstrip('\n')
        sex=sex.rstrip('\n')
        print('First Name:',first_name)
        print('Last Name:',last_name)
        print('Phone Number:',pho_no)
        print('Sex:',sex)
        print()
        first_name=class_file.readline()
    # Close the file
    class_file.close()
def display_part_record():
    # Make bool variable as flag
    found=False
    search=input('Insert a keyword to search for: ')
    # Open the codelagos file
    class_file=open('codelagos.txt','r')
    first_name=class_file.readline()
    # Make loop to go on till first name is empty
    while first_name!='':
        last_name=class_file.readline()
        pho_no=class_file.readline()
        sex=class_file.readline()
        first_name=first_name.rstrip('\n')
        last_name=last_name.rstrip('\n')
        pho_no=pho_no.rstrip('\n')
        sex=sex.rstrip('\n')
        # When the keyword is found
        if last_name==search or first_name==search or pho_no==search or sex==search:
            print('First Name:',first_name)
            print('Last Name:',last_name)
            print('Phone Number:',pho_no)
            print('Sex:',sex)
            print()
            found=True
        first_name=class_file.readline()
    if not found:
        print('The item is not in this file.')
    class_file.close()
    again()
def again():
    main_again=input('''
Would you like to search for another record?
(A) Yes
(B) No
''')
    if main_again.upper()=='A':
        display_part_record()
    elif main_again.upper()=='B':
        print('Thank you for using this program')
    else:
        print('Invalid selection')
        again()    
main()

#Name:Matthew Abayomi Olusesi
#Email:olusesimatthew14@gmail.com
#Simple Text Editor
#Instructor:Rex
#Documentation:This editor is a type of computer program that edits plain text,also used to change configuration files,documentation files and programming language source code
import sys
import os
import shutil

#A Simple text editor
#Written by Matt

def leave():
    sys.exit("You are leaving the Text Editor: Mexor")

def read():
    try:
        filename = input("Enter file name: ")
        target = open(filename, "r")
        readfile = target.read()
        print(readfile)
    except Exception as e:
        print("There was a problem: %s" %(e))

def delete():
    try:
        filename = input("Enter file name: ")
        os.unlink(filename)
    except Exception as e:
        print("There was a problem: %s" %(e))

def write():
    try:
        filename = input("Enter file name: ")
        target = open(filename, "a")
        while True:
            append = input()
            target.write(append)
            target.write("\n")
            if append.lower() == "menu":
                break
    except Exception as e:
        print("There was a problem: %s" %(e))

def cwd():
    try:
        print(os.getcwd())
        change = input("change Y/N: ")
        if change.startswith ("y"):
            path = input("New CWD: ")
            os.chdir(path)
    except Exception as e:
        print("There was a problem: %s" %(e))

def rename():
    try:
        filename = input("Enter current file name: ")
        new = input("Enter new filename: ")
        shutil.move(filename,new)
    except Exception as e:
        print("There was a problem: %s" %(e))
while True:
    print("options:write, read, cwd, exit, delete, rename")
    do = input("So,what do you intend to do: ")
    if do.lower() == "write":
        write()
    elif do.lower() == "read":
        read()
    elif do.lower() == "delete":
        delete()
    elif do.lower() == "exit":
        leave()
    elif do.lower == "cwd":
        cwd()
    elif do.lower == "rename":
        rename()


















        

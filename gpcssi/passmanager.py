import tkinter as tk
from tkinter import messagebox

def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added !!")
    else:
        messagebox.showerror("Error", "Please enter both the fields")

def get():
    username = entryName.get()
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("ERROR !!")
    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")

def getlist():
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!!")
    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            mess += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List !!")

def delete():
    username = entryName.get()
    temp_passwords = []
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(k)
    except:
        print("No passwords found!!")
    with open("passwords.txt", 'w') as f:
        for k in temp_passwords:
            f.write(k)
    messagebox.showinfo("Success", "Password deleted !!")

root = tk.Tk()
root.title("Password Manager")

labelName = tk.Label(root, text="Username")
labelName.pack()

entryName = tk.Entry(root)
entryName.pack()

labelPassword = tk.Label(root, text="Password")
labelPassword.pack()

entryPassword = tk.Entry(root, show="*")
entryPassword.pack()

buttonAdd = tk.Button(root, text="Add", command=add)
buttonAdd.pack()

buttonGet = tk.Button(root, text="Get", command=get)
buttonGet.pack()

buttonGetList = tk.Button(root, text="Get List", command=getlist)
buttonGetList.pack()

buttonDelete = tk.Button(root, text="Delete", command=delete)
buttonDelete.pack()

root.mainloop()
#!/usr/bin/python3

#Encrypt/Decrypt text using the Ceasar Cipher

import string
import tkinter as tk

alpha_u = string.ascii_uppercase
alpha_l = string.ascii_lowercase

def crypt():
    text = entry_var.get()
    key = tk_key.get()

    output = ''

    for letter in text:
        if letter in alpha_u or letter in alpha_l:
            if letter in alpha_u:
                alpha = alpha_u
            elif letter in alpha_l:
                alpha = alpha_l
            shift = alpha.index(letter)+key
            if shift >= len(alpha):
                shift = shift - len(alpha)
            output += alpha[shift]
        else:
            output += letter

    entry_var.set('')
    entry_var.set(output)

top = tk.Tk()
top.title('Ceasar Cipher')
top.resizable(0,0)

frame = tk.Frame(top)
frame.pack()

tk_key = tk.IntVar()
tk_key.set(1)
entry_var = tk.StringVar()

txt = tk.Entry(frame, textvariable=entry_var)
lbl_text = tk.Label(frame, text="Enter your text: ")
button = tk.Button(frame, text="Encrypt/Decrypt", command = crypt)
menu_key = tk.OptionMenu(frame, tk_key, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

lbl_text.grid(row=0, column=0)
txt.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=3, pady=(10,10))
menu_key.grid(row=0,column=2)

top.mainloop()




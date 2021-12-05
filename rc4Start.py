import pyperclip
import sys
import os
from tkinter import *
from tkinter import messagebox
from rc4EncryptDecrypt import encrypt, decrypt

root = Tk()
root.title("RC4 Algorithm")
root.geometry("700x150")
   
def encryptClicked():  
    result = encrypt(keyText.get(), letterText.get())
    messagebox.showinfo("Encrypted text - текст скопирован в буфер обмена", result)
    pyperclip.copy(result)
    
def decryptClicked():
    result = decrypt(keyText.get(), letterText.get())
    messagebox.showinfo("Decrypted text - текст скопирован в буфер обмена", result)
    pyperclip.copy(result)

letterText = StringVar()
keyText = StringVar()
 
letter_label = Label(text="Введите текст:")
key_label = Label(text="Введите ключ:")
 
letter_label.grid(row=0, column=0)
key_label.grid(row=1, column=0)
 
letter_entry = Entry(width="100", textvariable=letterText)
key_entry = Entry(width="100", textvariable=keyText)
 
letter_entry.grid(row=0, column=1)
key_entry.grid(row=1, column=1)

letter_entry.insert(0, "Rivest Cipher 4 also known as ARC4 or ARCFOUR meaning Alleged RC4")
key_entry.insert(0, "QWERTYYUIDIOTIEYETOERITOLRETOEFJGDKKFKGJDFKGHJKDFJGKDFJTKDFJFKGKG")
 
encryptButton = Button(width="50", text="Encrypt", command=encryptClicked)
encryptButton.grid(row=2, column=1)

decryptButton = Button(width="50", text="Decrypt", command=decryptClicked)
decryptButton.grid(row=3, column=1)
 
root.mainloop()
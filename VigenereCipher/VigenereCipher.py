from tkinter import *
from random import *

vigenere_cipher = Tk()
vigenere_cipher.title("Vigenere Cipher")
vigenere_cipher.minsize(500, 500)

firstLabel = Label(vigenere_cipher, text="Vigenere Cipher")
firstLabel.grid(row=0, column=250)

msg_label = Label(vigenere_cipher, text="Enter your Message:")
msg_label.grid(row=20, column=150)

msg = Entry(vigenere_cipher)
msg.grid(row=20, column=250)


def generate_key(message):
    key = []
    for i in message:
        if i.isalpha():
            key.append(randint(0, 26))
        else:
            key.append(i)
    return key


def encrypt():
    message = msg.get()
    key = generate_key(message)
    key_label = Label(vigenere_cipher, text="Key generated is:" + " ".join(str(x) for x in key))
    key_label.grid(column=250)

    cipher_text = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            if char.isupper():
                cipher_text += chr((ord(char) + key[i] - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(char) + key[i] - 97) % 26 + 97)
        else:
            cipher_text += char

    label = Label(vigenere_cipher, text=cipher_text)
    label.grid(column=250)

    decrypt_button = Button(vigenere_cipher, text="Decrypt the Message", command=lambda: decrypt(cipher_text, key))
    decrypt_button.grid(column=250)


def decrypt(cipher_text,key):
    plain_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            if char.isupper():
                plain_text += chr((ord(char) - key[i] - 65) % 26 + 65)
            else:
                plain_text += chr((ord(char) - key[i] - 97) % 26 + 97)
        else:
            plain_text += char
    label = Label(vigenere_cipher, text=plain_text)
    label.grid(column=250)


encrypt_button = Button(vigenere_cipher, text="Encrypt the Message", command=encrypt)
encrypt_button.grid(column=250)

vigenere_cipher.mainloop()
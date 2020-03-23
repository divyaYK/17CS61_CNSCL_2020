from tkinter import *
from random import *

root = Tk()
root.title("Caesar Cipher")
root.minsize(500, 500)

firstLabel = Label(root, text="Caesar Cipher")
firstLabel.grid(row=25, column=250)

msg_label = Label(root, text="Enter your Message:")
msg_label.grid(row=30, column=150)
msg = Entry(root)
msg.grid(row=30, column=250, columnspan=2)

radio = IntVar()
question_label = Label(root, text="Would you like to provide a key or generate a key?")
question_label.grid(column=250)
key_shift = Entry(root)


def print_key():
    key_label = Label(root, text="Enter the shift position:")
    key_label.grid(row =150, column=150)
    # key_shift = Entry(root)
    global key_shift
    key_shift.grid(row=150, column=250, columnspan=2)


provide = Radiobutton(root, text="Provide a Key", variable=radio, value=1, command=print_key)
provide.grid(column=250)


def generate_key():
    keyshift = randint(1, 26)
    # global key
    # key = key_shift
    return keyshift


generate = Radiobutton(root, text="Generate a Key", variable=radio, value=2, command=generate_key)
generate.grid(column=250)
generate.deselect()
provide.deselect()


# radio.set(1)


def encrypt():
    key = ""
    option = radio.get()
    if option == 1:
        key = key_shift.get()
    elif option == 2:
        key = str(generate_key())
    else:
        label = Label(root, text="Please select an option")
        label.grid(column=250)
    # shift = IntVar()
    message = msg.get()
    if message == "" or key == "":
        label = Label(root, text="Please Enter a Message and/or Key!")
        label.grid(column=250)
    else:
        cipher_text = ""
        shift = int(key)
        key_label = Label(root, text="Your Key is " + key)
        key_label.grid(column=250)
        for i in range(len(message)):
            char = message[i]
            if char.isalpha():
                if char.isupper():
                    cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                cipher_text += char
        label = Label(root, text=cipher_text)
        label.grid(column=250)
        decrypt_button = Button(root, text="Decrypt the Message", padx=50, command=lambda: decrypt(shift, cipher_text))
        decrypt_button.grid(column=250)


def decrypt(shift, cipher_text):
    plain_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            if char.isupper():
                plain_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    label = Label(root, text=plain_text)
    label.grid(column=250)


encrypt_button = Button(root, text="Encrypt the Message", padx=50, command=encrypt)
encrypt_button.grid(row=250, column=250)

root.mainloop()

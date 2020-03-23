from tkinter import *
import numpy as np


hill_cipher = Tk()
hill_cipher.title("Hill Cipher")
hill_cipher.minsize(500, 500)

first_label = Label(hill_cipher, text="Hill Cipher")
first_label.grid(row=0, column=250)

msg_label = Label(hill_cipher, text="Enter your message:")
msg_label.grid(row=25, column=150)
msg = Entry(hill_cipher)
msg.grid(row=25, column=250)

key_label = Label(hill_cipher, text="Enter your key:")
key_label.grid(row=50, column=150)
key_entry = Entry(hill_cipher)
key_entry.grid(row=50, column=250)

dict_count_uppercase = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

dict_count_lowercase = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z',
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}


def generate_key_code(key, n):
    key_matrix = np.zeros((n, n), dtype=str)
    key_coded = np.zeros((n, n))
    k = 0
    for i in range(n):
        for j in range(n):
            if k == len(key):
                k = 0
            key_matrix[i, j] = key[k]
            if key[k].isalpha():
                if key[k].isUpper():
                    key_coded[i, j] = dict_count_uppercase.get(key[k])
                else:
                    key_coded[i, j] = dict_count_lowercase.get(key[k])
            else:
                key_coded[i, j] = key[k]
            k += 1
    generated_key_label = Label(hill_cipher, text="key " + str(key_coded))
    generated_key_label.grid(column=250)
    return key_matrix, key_coded


def generate_msg_code(message):
    msg_coded = np.zeros((len(message), 1))
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                msg_coded[i] = dict_count_uppercase.get(message[i])
            else:
                msg_coded[i] = dict_count_lowercase.get(message[i])
        else:
            msg_coded[i] = message[i]

    label = Label(hill_cipher, text="message" + str(msg_coded))
    label.grid(column=250)
    return msg_coded


def encrypt():
    message = msg.get()
    key = key_entry.get()
    msg_coded = generate_msg_code(message)
    key_matrix, key_coded = generate_key_code(key, len(message))
    det = np.linalg.det(key_coded)
    if det == 0 or det % 13 == 0 or det % 2 == 0:
        error_label = Label(hill_cipher, text="Your key is not valid. Try again.")
        error_label.grid(column=250)
    cipher_coded = key_coded.dot(msg_coded) % 26
    cipher_text = ''
    for i in cipher_coded:
        for j in i:
            cipher_text += dict_count_lowercase.get(j)

    cipher_label = Label(hill_cipher, text=cipher_text)
    cipher_label.grid(column=250)

    decrypt_button = Button(hill_cipher, text="Decrypt the Message",
                            command=lambda: decrypt(cipher_text, cipher_coded, key_matrix, key_coded))
    decrypt_button.grid(column=250)


def get_multiplicative_inverse(key_coded):
    det = np.linalg.det(key_coded)
    det = int(det % 26)
    x = 0
    for i in range(26):
        if (i * det) % 26 == 1:
            x = i
            break

    return x


def decrypt(cipher_text, cipher_coded, key_matrix, key_coded):
    key_inverse = np.linalg.inv(key_coded)
    key_inverse = np.linalg.det(key_coded) * get_multiplicative_inverse(key_coded) * key_inverse
    key_inverse = key_inverse.astype(int)
    key_inverse = key_inverse % 26
    plain_coded = np.matmul(key_inverse, cipher_coded) % 26  # key_inverse.dot(cipher_coded) % 26
    # plain_coded = np.remainder(plain_coded, module).flatten()
    plain_coded = plain_coded.astype(int)
    plain_text = ''
    for i in plain_coded:
        for j in i:
            plain_text += dict_count_lowercase.get(j)

    plain_label = Label(hill_cipher, text="Plain text is:   " + plain_text)
    plain_label.grid(column=250)


encrypt_button = Button(hill_cipher, text="Encrypt the message", command=encrypt)
encrypt_button.grid(column=250)

hill_cipher.mainloop()

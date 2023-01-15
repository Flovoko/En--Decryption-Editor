import os
from Crypto.Cipher import AES
import clipboard
from tkinter import Tk, Text, Scrollbar, Menu, filedialog, messagebox, Label, Button, BOTH

key = key = os.urandom(32)
nonce = b'\xd1\x1a!\x10\x8b&\x94\x8c\x8d7>\xa8\xa3\rS1'

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'rb') as file:
        ciphertext = file.read()
    key = input("Please enter the key for decryption: ")
    key = bytes.fromhex(key)
    decryption_suite = AES.new(key, AES.MODE_EAX, nonce)
    plaintext = decryption_suite.decrypt(ciphertext)
    plaintext = plaintext.decode('UTF-8')
    text.insert('1.0', plaintext)

def save_file():
    filepath = filedialog.asksaveasfilename()
    key_label = Label(root, text='Key: ' + key.hex() + ' \nFile: ' + filepath)
    key_label.pack(side="bottom")
    copy_button = Button(root, text="Copy", command=copy_key)
    copy_button.pack(side="bottom")
    with open(filepath, 'wb') as file:
        encryption_suite = AES.new(key, AES.MODE_EAX, nonce)
        ciphertext = encryption_suite.encrypt(text.get('1.0', 'end').encode('UTF-8'))
        file.write(ciphertext)

def copy_key():
    clipboard.copy(key.hex())

root = Tk()

root.title('En-/Decryption Editor')

text = Text(root, bg="#222", fg="white", font="Forte 12", insertbackground='white')
text.pack(fill=BOTH, expand=1)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
menubar.add_cascade(label='File', menu=filemenu)
root.config(menu=menubar)

root.mainloop()
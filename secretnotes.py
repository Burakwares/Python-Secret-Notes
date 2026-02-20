import tkinter
import base64
from tkinter import messagebox

'''FUNCTIONS'''

#ENCRYPTION FUNC
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.b64encode("".join(enc).encode("latin-1")).decode("utf-8")

#DECRYPTION FUNC
def decode(key, enc):
    dec = []
    enc = base64.b64decode(enc.encode("utf-8")).decode("latin-1")
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#BUTTON FUNCS AND FILE PROCESSES
def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0", tkinter.END).strip()
    master_secret = master_secret_entry.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="ERROR!", message="Please fill the all lines.")
    else:
        message_encrypted = encode(master_secret, message)

        try:
            with open("my_secret_notes.txt", "a", encoding="utf-8") as data_file:
                data_file.write(f"\nHeading: {title}\nEncrypted Note: {message_encrypted}\n")
        except FileNotFoundError:
            with open("my_secret_notes.txt", "w", encoding="utf-8") as data_file:
                data_file.write(f"Heading: {title}\nEncrypted Note: {message_encrypted}\n")
        finally:
            title_entry.delete(0, tkinter.END)
            master_secret_entry.delete(0, tkinter.END)
            input_text.delete("1.0", tkinter.END)
            messagebox.showinfo(title="Successfully", message="Your note has been encrypted and saved successfully.")

def decrypt_notes():
    message_encrypted = input_text.get("1.0", tkinter.END).strip()
    master_secret = master_secret_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showwarning(title="ERROR!", message="Please enter decryption text and key.")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            input_text.delete("1.0", tkinter.END)
            input_text.insert("1.0", decrypted_message)
        except Exception:
            messagebox.showerror(title="ERROR!", message="The key could not be decrypted. Text or Key might be wrong.")

'''WINDOW'''
window = tkinter.Tk()
window.title("SecretNotes")
window.geometry("400x600")
window.config(padx=30, pady=40)

'''INTERFACE'''
#HEADING
title_label = tkinter.Label(text="Enter A Note Heading", font=("Verdana", 12, "bold"))
title_label.pack(pady=5)
title_entry = tkinter.Entry(width=30)
title_entry.pack()

#CONTENT
input_label = tkinter.Label(text="Enter Your Secret Note", font=("Verdana", 12, "bold"))
input_label.pack(pady=5)
input_text = tkinter.Text(width=40, height=15)
input_text.pack()

#MASTERKEY
master_secret_label = tkinter.Label(text="Enter Your Key", font=("Verdana", 12, "bold"))
master_secret_label.pack(pady=5)
master_secret_entry = tkinter.Entry(width=30, show="*")
master_secret_entry.pack()

#BUTTONS
save_button = tkinter.Button(text="Save and Encrypt", command=save_and_encrypt_notes)
save_button.pack(pady=10)

decrypt_button = tkinter.Button(text="Decrypt the key", command=decrypt_notes)
decrypt_button.pack(pady=5)

window.mainloop()
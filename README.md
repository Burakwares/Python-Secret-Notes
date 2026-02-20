# Secret Notes 🔐

A simple and intuitive desktop application built with Python and Tkinter. It allows users to write secret notes, encrypt them using a master key, and save them safely to a local file. You can also decrypt your previously saved notes using the correct master key.

## 🚀 Features
* **User-Friendly GUI:** Clean and simple graphical interface built with Python's native `tkinter` library.
* **Encryption & Decryption:** Uses a custom Vigenère-style cipher combined with Base64 encoding to secure your text.
* **Local Storage:** Automatically saves and appends your encrypted notes to a local `my_secret_notes.txt` file.
* **Standalone Capability:** Can be easily compiled into a standalone executable (`.exe`) using PyInstaller.

## 🛠️ Requirements
* **Python 3.x**
* No external libraries are required to run the source code (it uses built-in `tkinter` and `base64`).

## 💻 How to Run

1. Clone this repository to your local machine:
```bash
git clone https://github.com/Burakwares/Python-Secret-Notes.git 
```
2. Navigate to the project directory:
```bash
cd Python-Secret-Notes
```
3. Run the application:
```bash
python secretnotes.py
```
## 📖 Usage
* **To Encrypt and Save a Note:**

-Enter a title for your note.

-Type your secret message in the main text area.

-Enter a secure "Master Key" (password).

-Click the Save & Encrypt button.

* **To Decrypt a Note:**

-Paste the encrypted message into the text area.

-Enter the exact same Master Key used for encryption.

-Click the Decrypt button to reveal the hidden message.

<img width="399" height="625" alt="image" src="https://github.com/user-attachments/assets/f18664fd-39ce-45b7-a491-8589bc977a72" /> <img width="404" height="100" alt="image" src="https://github.com/user-attachments/assets/75536a48-5973-45d7-982d-f8a2e15e5e83" />



## ⚠️ Disclaimer
This project was developed for educational purposes to demonstrate basic cryptography and GUI creation in Python. The custom encryption algorithm is relatively simple and should not be used to store highly sensitive data (like bank accounts or real passwords).

## 📄 License
This project is open-source and available to use, modify, and distribute.

import customtkinter as ctk
import self

app = ctk.CTk()
app.geometry("640x480")
app.title("Caesar Cryptography")
app.iconbitmap("shield.ico")

plain_text1 = ctk.StringVar()

cipher_text1 = ctk.StringVar()

shift = ctk.IntVar()


def Encrypt():
    cipher_text = ""
    plain_text = plain_text1.get()
    for i in plain_text:
        if (i.islower()):
            cipher_text += (chr((ord(i) - 97 + shift.get()) % 26 + 97))
            cipher_text1.set(cipher_text)
        if (i.isupper()):
            cipher_text += (chr((ord(i) - 65 + shift.get()) % 26 + 65))
            cipher_text1.set(cipher_text)


def Decrypt():
    plain_text = ""
    cipher_text = cipher_text1.get()
    for i in cipher_text:
        if (i.islower()):
            plain_text += (chr((ord(i) - 97 - shift.get()) % 26 + 97))
            plain_text1.set(plain_text)
        if (i.isupper()):
            plain_text += (chr((ord(i) - 65 - shift.get()) % 26 + 65))
            plain_text1.set(plain_text)


Label1 = ctk.CTkLabel(app, text="Caesar Cipher", font=("IBM Plex Mono Medium", 42), text_color="#FB5607")
Label1.pack()

Label2 = ctk.CTkLabel(app, text="Plain Text:", font=("IBM Plex Mono Medium", 22), text_color="#FFBE0B")
Label2.place(x=10, y=170)

Entry1 = ctk.CTkEntry(app, height=25, width=220, text_color='#FF006E', textvariable=plain_text1)
Entry1.place(x=165, y=175)

Label2 = ctk.CTkLabel(app, text="Cipher Text:", font=("IBM Plex Mono Medium", 22), text_color="#FFBE0B")
Label2.place(x=10, y=255)

Entry2 = ctk.CTkEntry(app, height=25, width=220, text_color="#FF006E", textvariable=cipher_text1)
Entry2.place(x=179, y=260)

Label3 = ctk.CTkLabel(app, text="Shift:", font=("IBM Plex Mono Medium", 22), text_color="#8338EC")
Label3.place(x=10, y=310)

Entry3 = ctk.CTkEntry(app, height=10, width=160, text_color="#8338EC", textvariable=shift)
Entry3.place(x=95, y=315)

Btn1 = ctk.CTkButton(app, text="Encrypt", fg_color="#FB5607", font=("IBM Plex Mono Medium", 20),
                     command=lambda: print(Encrypt()))
Btn1.place(x=125, y=370)

Btn1 = ctk.CTkButton(app, text="Decrypt", fg_color="#FB5607", font=("IBM Plex Mono Medium", 20),
                     command=lambda: print(Decrypt()))
Btn1.place(x=375, y=370)

app.mainloop()
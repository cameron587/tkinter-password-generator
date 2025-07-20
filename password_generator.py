import tkinter as tk
import string
import random

window = tk.Tk()
window.title("Password Generator")
window.geometry("350x150")

password_display = tk.Entry(window, font=("Arial", 20), justify="center")
password_display.pack(pady=10, ipadx=10, ipady=10)

def generate_password():
    length = 18
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

generate_button = tk.Button(text="Generate Password", font=("Arial", 20), command=generate_password)
generate_button.pack(pady=10, padx=20)

window.mainloop()

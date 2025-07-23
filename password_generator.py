import tkinter as tk
import string
import random

window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")

password_display = tk.Entry(window, font=("Arial", 20), justify="center")
password_display.pack(pady=10, ipadx=10, ipady=10)

length_label = tk.Label(window, text="Password Length: 18", font=("Arial", 12))
length_label.pack()

length_slider = tk.Scale(
    window,
    from_=4,
    to=32,
    orient='horizontal',
    length=300,
    sliderrelief='flat',
    troughcolor='darkgrey'
)
length_slider.set(18)
length_slider.pack()

def update_label(value):
    length_label.config(text=f"Password Length: {value}")

length_slider.config(command=update_label)

def generate_password():
    length = length_slider.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.delete(0, tk.END)
    password_display.insert(0, password)

generate_button = tk.Button(text="Generate Password", font="Arial, 20", command=generate_password)
generate_button.pack(pady=5, padx=20)

def copy_to_clipboard():
    password = password_display.get()
    window.clipboard_clear()
    window.clipboard_append(password)

copy_button = tk.Button(text="Copy", font="Arial, 10", command=copy_to_clipboard)
copy_button.pack(pady=2)

window.mainloop()
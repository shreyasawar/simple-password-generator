import tkinter as tk
import random
import string

def generate_password(length):
    """
    Generates a random password of the specified length.
    
    Args:
        length (int): The desired length of the password.
    
    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display():
    """
    Generates a password and displays it in the GUI.
    """
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_label.config(text=f"Your password is: {password}")

root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
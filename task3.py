import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.complexity_var = tk.IntVar(value=1)
        self.lowercase_var = tk.IntVar(value=1)
        self.uppercase_var = tk.IntVar(value=1)
        self.digits_var = tk.IntVar(value=1)
        self.special_chars_var = tk.IntVar(value=1)

        self.create_widgets()

    def generate_password(self):
        length = self.length_var.get()
        complexity = self.complexity_var.get()
        lowercase = self.lowercase_var.get()
        uppercase = self.uppercase_var.get()
        digits = self.digits_var.get()
        special_chars = self.special_chars_var.get()

        characters = ""

        if lowercase:
            characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if special_chars:
            characters += string.punctuation

        if complexity == 1:
            characters = string.ascii_letters + string.digits
        elif complexity == 2:
            characters = string.ascii_letters

        if not characters:
            self.result_label.config(text="Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.result_label.cget("text").split(": ")[1]
        pyperclip.copy(password)
        self.result_label.config(text="Password copied to clipboard.")

    def create_widgets(self):
        # Length
        length_label = ttk.Label(self.master, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10)
        length_entry = ttk.Entry(self.master, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Complexity
        complexity_label = ttk.Label(self.master, text="Password Complexity:")
        complexity_label.grid(row=1, column=0, padx=10, pady=10)
        complexity_combobox = ttk.Combobox(self.master, values=["High", "Medium", "Low"], state="readonly", textvariable=self.complexity_var)
        complexity_combobox.grid(row=1, column=1, padx=10, pady=10)
        complexity_combobox.current(0)

        # Character Types
        types_frame = ttk.Frame(self.master)
        types_frame.grid(row=2, column=0, columnspan=2, pady=10)

        lowercase_checkbox = ttk.Checkbutton(types_frame, text="Lowercase", variable=self.lowercase_var)
        lowercase_checkbox.grid(row=0, column=0, padx=5)

        uppercase_checkbox = ttk.Checkbutton(types_frame, text="Uppercase", variable=self.uppercase_var)
        uppercase_checkbox.grid(row=0, column=1, padx=5)

        digits_checkbox = ttk.Checkbutton(types_frame, text="Digits", variable=self.digits_var)
        digits_checkbox.grid(row=0, column=2, padx=5)

        special_chars_checkbox = ttk.Checkbutton(types_frame, text="Special Characters", variable=self.special_chars_var)
        special_chars_checkbox.grid(row=0, column=3, padx=5)

        # Generate Button
        generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Copy to Clipboard Button
        copy_button = ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

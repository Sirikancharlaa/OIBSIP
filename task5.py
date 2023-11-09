import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from datetime import datetime

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Advanced Chat App')

        # User authentication
        self.username = ''
        self.authenticate_user()

        # UI setup
        self.create_widgets()

        # Chat data
        self.chat_history = {}

    def authenticate_user(self):
        # For simplicity, just ask for a username
        self.username = simple_dialog('Enter your username')

    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

        # Chat room selection
        self.room_label = ttk.Label(self.root, text='Chat Room:')
        self.room_label.pack(pady=5)

        self.room_combobox = ttk.Combobox(self.root, values=['General', 'Random', 'Python'])
        self.room_combobox.pack(pady=5)

        # Chat history display
        self.chat_display = scrolledtext.ScrolledText(self.root, state='disabled', wrap='word')
        self.chat_display.pack(padx=10, pady=10)

        # Message input
        self.message_entry = ttk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)

        # Send button
        send_button = ttk.Button(self.root, text='Send', command=self.send_message)
        send_button.pack(pady=10)

    def send_message(self):
        room = self.room_combobox.get()
        message = self.message_entry.get()
        timestamp = datetime.now().strftime('%H:%M:%S')

        if room not in self.chat_history:
            self.chat_history[room] = []

        self.chat_history[room].append(f'[{timestamp}] {self.username}: {message}')

        # Update chat display
        self.update_chat_display()

        # Clear message entry
        self.message_entry.delete(0, 'end')

    def update_chat_display(self):
        room = self.room_combobox.get()
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, 'end')

        if room in self.chat_history:
            for message in self.chat_history[room]:
                self.chat_display.insert('end', message + '\n')

        self.chat_display.config(state='disabled')

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.chat_history = eval(file.read())  # Insecure, should use JSON or other safer methods

            self.update_chat_display()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt",
                                                  filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(str(self.chat_history))


def simple_dialog(prompt):
    return tk.simpledialog.askstring("Input", prompt)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

import tkinter as tk

from tkinter import (
    filedialog,
    messagebox
)

from sender import send_messages


class SendPage:

    def __init__(self, root):

        self.root = root

        self.image_path = None

        tk.Label(
            root,
            text="Message"
        ).pack(pady=10)

        self.message_box = tk.Text(
            root,
            width=60,
            height=10
        )

        self.message_box.pack(pady=10)

        tk.Button(
            root,
            text="Choose Image",
            command=self.choose_image
        ).pack(pady=10)

        self.image_label = tk.Label(
            root,
            text="No Image Selected"
        )

        self.image_label.pack(pady=5)

        tk.Button(
            root,
            text="Send To All Contacts",
            command=self.send
        ).pack(pady=20)

    def choose_image(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg")
            ]
        )

        if file_path:

            self.image_path = file_path

            self.image_label.config(
                text=file_path
            )

    def send(self):

        message = self.message_box.get(
            "1.0",
            tk.END
        ).strip()

        if not message:

            messagebox.showerror(
                "Error",
                "Message Required"
            )

            return

        send_messages(
            message,
            self.image_path
        )

        messagebox.showinfo(
            "Done",
            "Messages Sent Successfully"
        )
import tkinter as tk
from tkinter import filedialog, messagebox

import csv

from database import add_contact


class ImportPage:

    def __init__(self, root):

        self.root = root

        tk.Label(
            root,
            text="Import Contacts"
        ).pack(pady=10)

        tk.Button(
            root,
            text="Import from CSV",
            command=self.import_csv
        ).pack(pady=10)

        tk.Label(
            root,
            text="Or paste numbers (one per line)"
        ).pack(pady=10)

        self.text_box = tk.Text(
            root,
            width=40,
            height=15
        )
        self.text_box.pack(pady=10)

        tk.Button(
            root,
            text="Save Pasted Numbers",
            command=self.save_pasted
        ).pack(pady=10)

    def validate(self, phone):
        return phone.startswith("+20")

    def import_csv(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if not file_path:
            return

        with open(file_path, newline="") as file:

            reader = csv.reader(file)

            for row in reader:

                phone = row[0].strip()

                if self.validate(phone):
                    add_contact(phone)

        messagebox.showinfo("Done", "Contacts imported")

    def save_pasted(self):

        data = self.text_box.get("1.0", tk.END).strip().split("\n")

        for phone in data:

            phone = phone.strip()

            if self.validate(phone):
                add_contact(phone)

        messagebox.showinfo("Done", "Numbers saved")
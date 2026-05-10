import tkinter as tk
from tkinter import messagebox

from database import *


class ContactsPage:

    def __init__(self, root):

        self.root = root

        tk.Label(
            root,
            text="Phone Number (+20)"
        ).pack(pady=5)

        self.phone_entry = tk.Entry(
            root,
            width=40
        )
        self.phone_entry.pack(pady=5)

        tk.Button(
            root,
            text="Add Contact",
            command=self.add_contact
        ).pack(pady=5)

        self.contacts_list = tk.Listbox(
            root,
            width=50,
            height=20
        )
        self.contacts_list.pack(pady=10)

        tk.Button(
            root,
            text="Delete Selected",
            command=self.delete_contact
        ).pack(pady=5)

        tk.Button(
            root,
            text="Update Selected",
            command=self.update_contact
        ).pack(pady=5)

        self.load_data()

    def load_data(self):

        self.contacts_list.delete(0, tk.END)

        contacts = get_contacts()

        for contact in contacts:

            self.contacts_list.insert(
                tk.END,
                f"{contact[0]} - {contact[1]}"
            )

    def validate_phone(self, phone):

        return (
            phone.startswith("+20")
            and len(phone) >= 13
        )

    def add_contact(self):

        phone = self.phone_entry.get().strip()

        if not self.validate_phone(phone):

            messagebox.showerror(
                "Error",
                "Phone must start with +20"
            )

            return

        add_contact(phone)

        self.load_data()

        self.phone_entry.delete(0, tk.END)

    def delete_contact(self):

        selected = self.contacts_list.get(tk.ACTIVE)

        if selected:

            contact_id = selected.split(" - ")[0]

            delete_contact(contact_id)

            self.load_data()

    def update_contact(self):

        selected = self.contacts_list.get(tk.ACTIVE)

        new_phone = self.phone_entry.get().strip()

        if not self.validate_phone(new_phone):

            messagebox.showerror(
                "Error",
                "Phone must start with +20"
            )

            return

        if selected:

            contact_id = selected.split(" - ")[0]

            update_contact(
                contact_id,
                new_phone
            )

            self.load_data()
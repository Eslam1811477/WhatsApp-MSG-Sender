import tkinter as tk
from tkinter import ttk

from database import create_tables
from ui.contacts_page import ContactsPage
from ui.send_page import SendPage
from ui.import_page import ImportPage

create_tables()

root = tk.Tk()
root.title("WhatsApp Tool")
root.geometry("700x700")

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True)

tab1 = tk.Frame(tabs)
tab2 = tk.Frame(tabs)
tab3 = tk.Frame(tabs)

tabs.add(tab1, text="Contacts")
tabs.add(tab2, text="Send")
tabs.add(tab3, text="Import")

ContactsPage(tab1)
SendPage(tab2)
ImportPage(tab3)

root.mainloop()
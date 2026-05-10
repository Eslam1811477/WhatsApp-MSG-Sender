import sqlite3

DB_NAME = "whatsapp.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Contacts

def add_contact(phone):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO contacts(phone) VALUES(?)", (phone,))

    conn.commit()
    conn.close()


def get_contacts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()

    conn.close()
    return data


def delete_contact(contact_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))

    conn.commit()
    conn.close()


def update_contact(contact_id, phone):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE contacts SET phone=? WHERE id=?",
        (phone, contact_id)
    )

    conn.commit()
    conn.close()


# Messages

def add_message(message):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(message) VALUES(?)",
        (message,)
    )

    conn.commit()
    conn.close()


def get_messages():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()

    conn.close()
    return data


def delete_message(message_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE id=?",
        (message_id,)
    )

    conn.commit()
    conn.close()


def update_message(message_id, message):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE messages SET message=? WHERE id=?",
        (message, message_id)
    )

    conn.commit()
    conn.close()
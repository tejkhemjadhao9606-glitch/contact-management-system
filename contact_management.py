import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tejas1741",
        database="contact_management"
    )


def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Enter username and password")
        return

    db = db_connect()
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    result = cur.fetchone()
    db.close()

    if result:
        login_win.destroy()
        dashboard()
    else:
        messagebox.showerror("Error", "Invalid username or password")


def contact_form(title, action):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("450x450")

    fields = ["ID", "Name", "Phone", "Email", "Address", "Category"]
    entries = []

    for i, field in enumerate(fields):
        tk.Label(win, text=field).grid(
            row=i, column=0, padx=10, pady=10
        )

        if field == "Category":
            entry = ttk.Combobox(
                win,
                values=["Friend", "Family", "College", "Work", "Other"],
                width=27
            )
        else:
            entry = tk.Entry(win, width=30)

        entry.grid(row=i, column=1)
        entries.append(entry)

    def clear():
        for entry in entries:
            if isinstance(entry, ttk.Combobox):
                entry.set("")
            else:
                entry.delete(0, tk.END)

    def save():
        values = [e.get() for e in entries]

        if action == "add":
            if values[1] == "" or values[2] == "":
                messagebox.showwarning(
                    "Warning", "Name and Phone required"
                )
                return

            if not values[2].isdigit() or len(values[2]) != 10:
                messagebox.showwarning(
                    "Warning", "Enter valid 10 digit phone"
                )
                return

            db = db_connect()
            cur = db.cursor()

            cur.execute("""
                INSERT INTO contacts
                (name, phone, email, address, category)
                VALUES (%s,%s,%s,%s,%s)
            """, tuple(values[1:]))

            db.commit()
            db.close()

            messagebox.showinfo("Success", "Contact added")
            clear()

        else:
            if values[0] == "":
                messagebox.showwarning(
                    "Warning", "Enter Contact ID"
                )
                return

            db = db_connect()
            cur = db.cursor()

            cur.execute("""
                UPDATE contacts
                SET name=%s, phone=%s, email=%s,
                    address=%s, category=%s
                WHERE id=%s
            """, (
                values[1], values[2], values[3],
                values[4], values[5], values[0]
            ))

            db.commit()

            if cur.rowcount:
                messagebox.showinfo("Success", "Contact updated")
            else:
                messagebox.showwarning(
                    "Warning", "Contact not found"
                )

            db.close()

    tk.Button(
        win, text="Save", width=12, command=save
    ).grid(row=7, column=0, pady=20)

    tk.Button(
        win, text="Clear", width=12, command=clear
    ).grid(row=7, column=1, pady=20)


def add_contact():
    contact_form("Add Contact", "add")


def update_contact():
    contact_form("Update Contact", "update")


def view_contacts():
    win = tk.Toplevel(root)
    win.title("View Contacts")
    win.geometry("850x450")

    columns = ("ID", "Name", "Phone", "Email", "Address", "Category")
    table = ttk.Treeview(
        win, columns=columns, show="headings"
    )

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=130)

    table.pack(fill="both", expand=True)

    db = db_connect()
    cur = db.cursor()
    cur.execute("SELECT * FROM contacts")

    for row in cur.fetchall():
        table.insert("", tk.END, values=row)

    db.close()


def search_contact():
    win = tk.Toplevel(root)
    win.title("Search Contact")
    win.geometry("850x450")

    tk.Label(win, text="Enter Contact ID").pack(pady=5)

    search = tk.Entry(win, width=30)
    search.pack(pady=5)

    columns = ("ID", "Name", "Phone", "Email", "Address", "Category")
    table = ttk.Treeview(
        win, columns=columns, show="headings"
    )

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=130)

    table.pack(fill="both", expand=True)

    def find():
        for item in table.get_children():
            table.delete(item)

        if search.get() == "":
            messagebox.showwarning(
                "Warning", "Enter Contact ID"
            )
            return

        db = db_connect()
        cur = db.cursor()

        cur.execute(
            "SELECT * FROM contacts WHERE id=%s",
            (search.get(),)
        )

        result = cur.fetchall()

        for row in result:
            table.insert("", tk.END, values=row)

        db.close()

        if not result:
            messagebox.showinfo(
                "Result", "Contact not found"
            )

    tk.Button(
        win, text="Search", width=15, command=find
    ).pack(pady=10)


def delete_contact():
    win = tk.Toplevel(root)
    win.title("Delete Contact")
    win.geometry("350x250")

    tk.Label(win, text="Contact ID").pack(pady=20)

    entry = tk.Entry(win)
    entry.pack()

    def delete():
        if entry.get() == "":
            messagebox.showwarning(
                "Warning", "Enter Contact ID"
            )
            return

        if not messagebox.askyesno(
            "Confirm", "Delete this contact?"
        ):
            return

        db = db_connect()
        cur = db.cursor()

        cur.execute(
            "DELETE FROM contacts WHERE id=%s",
            (entry.get(),)
        )

        db.commit()

        if cur.rowcount:
            messagebox.showinfo(
                "Success", "Contact deleted"
            )
        else:
            messagebox.showwarning(
                "Warning", "Contact not found"
            )

        db.close()

    tk.Button(
        win, text="Delete", width=15, command=delete
    ).pack(pady=20)


def logout():
    if messagebox.askyesno(
        "Logout", "Do you want to logout?"
    ):
        root.destroy()
        start_login()


def dashboard():
    global root

    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry("600x500")

    tk.Label(
        root,
        text="CONTACT MANAGEMENT SYSTEM",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    buttons = [
        ("Add Contact", add_contact),
        ("View Contacts", view_contacts),
        ("Search Contact", search_contact),
        ("Update Contact", update_contact),
        ("Delete Contact", delete_contact),
        ("Logout", logout)
    ]

    frame = tk.Frame(root)
    frame.pack()

    for i, (text, command) in enumerate(buttons):
        tk.Button(
            frame,
            text=text,
            width=20,
            height=2,
            command=command
        ).grid(
            row=i // 2,
            column=i % 2,
            padx=15,
            pady=15
        )

    root.mainloop()


def start_login():
    global login_win, user_entry, pass_entry

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("450x350")

    tk.Label(
        login_win,
        text="CONTACT MANAGEMENT SYSTEM",
        font=("Arial", 18, "bold")
    ).pack(pady=30)

    frame = tk.Frame(login_win)
    frame.pack()

    tk.Label(
        frame, text="Username"
    ).grid(row=0, column=0, pady=15)

    user_entry = tk.Entry(frame, width=30)
    user_entry.grid(row=0, column=1)

    tk.Label(
        frame, text="Password"
    ).grid(row=1, column=0, pady=15)

    pass_entry = tk.Entry(
        frame, width=30, show="*"
    )
    pass_entry.grid(row=1, column=1)

    tk.Button(
        login_win,
        text="Login",
        width=15,
        command=login
    ).pack(pady=25)

    login_win.mainloop()


start_login()
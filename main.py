import pyodbc
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('200x300')
app.title('CREATE-CONNECT MS DATABASE')

entry_database = customtkinter.CTkEntry(app, placeholder_text='Database Name')
entry_database.place(relx=0.1, rely=0.1)

def create_db ():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-C38T8FU,1541;"
            "DATABASE=master;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        connection.autocommit = True
        connection.execute(f'create database {entry_database.get()}')
        info_label.configure(text='Database Created')
    except pyodbc.Error:
        info_label.configure(text='Error, Database Was Not Created')

def connect_db():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-C38T8FU,1541;"
            f"DATABASE={entry_database.get()};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        info_label.configure(text='Connection Successfull')
    except pyodbc.Error:
        info_label.configure(text='Connection Failed')

create_button = customtkinter.CTkButton(app, text='Create', command=create_db, fg_color='green')
create_button.place(relx=0.1, rely=0.2)
create_button = customtkinter.CTkButton(app, text='Connect', command=connect_db, fg_color='blue')
create_button.place(relx=0.1, rely=0.3)

info_label = customtkinter.CTkLabel(app, text='')
info_label.place(relx=0.1, rely=0.4)

app.mainloop()





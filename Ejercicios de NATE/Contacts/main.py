
import pickle
from Contacts import Contact
from tkinter import *
from tkinter import ttk
from time import sleep


ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts, name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)
    save_contacts(contacts)
    return contact


def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact.name).grid(column=1, row=row, sticky=W)
    ttk.Label(frame_contact_list, text=contact.email).grid(column=2, row=row, sticky=W)
    ttk.Label(frame_contact_list, text=contact.phone).grid(column=3, row=row, sticky=W)


def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(input("Nombre: "), input("Email: "), input("Telefono: "))
    sleep(2)


def remove_contact(contacts):
    index_to_delete = find_contact(contacts)
    contacts.pop(index_to_delete)
    sleep(3)
    print("Se elimino el contacto correctamente.")


def find_contact(contacts):
    answer = "si"
    while answer == "si":
        print("\n\nBuscar contacto\n")
        search_by = input("Desea buscar por email o por nombre? [email / name]: ")
        while search_by != "email" and search_by != "name":
            search_by = input("Desea buscar por email o por nombre? [email / name]: ")

        if search_by == "name":
            search_term = input("Introducir el nombre del contacto o parte de él: ")
            found_contacts = []

            print("He encontrado los siguientes contactos:")
            contact_indexes = []
            contact_counter = 0

            for contact in contacts:
                if contact.name.find(search_term) >= 0:
                    found_contacts.append(contact)
                    print("{} - {}".format(contact_counter, contact.name))
                    contact_indexes.append(contact_counter)
                    contact_counter += 1

            contact_index = 0
            answer = "no"
            if len(contact_indexes) > 1:
                contact_index = ask_until_option_expected(contact_indexes)
            elif len(contact_indexes) == 0:
                print("No se ha encontrado ninguno.")
                answer = input("Deseas hacer otra busqueda? [si,no]: ")
                if answer == "no":
                    return
        elif search_by == "email":
            search_term = input("Introducir el email del contacto o parte de él: ")
            found_contacts = []

            print("He encontrado los siguientes contactos:")
            contact_indexes = []
            contact_counter = 0

            for contact in contacts:
                if contact.email.find(search_term) >= 0:
                    found_contacts.append(contact)
                    print("{} - {}".format(contact_counter, contact.email))
                    contact_indexes.append(contact_counter)
                    contact_counter += 1

            contact_index = 0
            answer = "no"
            if len(contact_indexes) > 1:
                contact_index = ask_until_option_expected(contact_indexes)
            elif len(contact_indexes) == 0:
                print("No se ha encontrado ninguno.")
                answer = input("Deseas hacer otra busqueda? [si,no]: ")
                if answer == "no":
                    return
    contact = found_contact[contact_index]
    contact.print_data()
    sleep(2)



def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="12 12 12 12")
    frame_add_contact.grid()
    frame_contact_list = ttk.Frame(root, padding="12 12 12 12")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Entry(frame_add_contact, width=10, textvariable=name).grid(column=1, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=20, textvariable=email).grid(column=2, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=10, textvariable=phone).grid(column=3, row=2, sticky=W)

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1, sticky=W)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=1, sticky=E)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3, sticky=W)
"""
    for index in contacts:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=index["name"]).grid(column=1, row=row, sticky=W)
        ttk.Label(frame_contact_list, text=index["email"]).grid(column=2, row=row, sticky=W)
        ttk.Label(frame_contact_list, text=index["phone"]).grid(column=3, row=row, sticky=W)

    for child in frame_add_contact.winfo_children():
        child.grid_configure(padx=10, pady=5)

    for child in frame_contact_list.winfo_children():
        child.grid_configure(padx=10, pady=5)

    root.mainloop()
"""

if __name__ == "__main__":
    main()
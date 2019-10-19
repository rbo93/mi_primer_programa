"""
Modificaciones a realizar:

1 - Agregar Remover contacto
2 - Busqueda por email, aparte de la de nombre
3 - Si al buscar no se encuentra contacto, pregunte si desea buscar otro


"""

import pickle

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


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact_id = len(contacts) + 1
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: "),
        "id": contact_id
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
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
                if contact["name"].find(search_term) >= 0:
                    found_contacts.append(contact)
                    print("{} - {}".format(contact_counter, contact["name"]))
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
                if contact["email"].find(search_term) >= 0:
                    found_contacts.append(contact)
                    print("{} - {}".format(contact_counter, contact["email"]))
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

    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n".format(**found_contacts[contact_index]))
    sleep(2)
    return int(contact_index-1)


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
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
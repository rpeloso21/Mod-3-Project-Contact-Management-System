import re
import os

# os.makedirs("Contacts")

def add_contact(contacts):
    while True:
        id_input = input("Please provide the 10 digit phone number for the contact you would like to add with no spaces, dashes, or other markings: ")
        if re.match(r"^\d{10}$", id_input):
            contacts[id_input] = {}
            contacts[id_input]["Phone Number"] = id_input
            break
        else:
            print("That is not a valid format.  Please try again.")

    while True:
        name_input = input("Please provide the name of your contact (first last): ")
        if re.match(r"^[a-zA-Z]+ [a-zA-Z]+$", name_input):
            contacts[id_input]["Name"] = name_input
            break
        else:
            print("That is not a valid name format.  Please try again.")

    while True:
        email_imput = input("Please provide the email for your contact: ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_imput):
            contacts[id_input]["Email"] = email_imput
            break
        else:
            print("That is not a valid email format.  Please try again.")

    print(f"\nContact created successfully! \n")

def edit_contact(contacts):

    while True:
        search_input = input("Please provider the contact ID (eg. phone number) of the contact that you would like to edit: ")
        
        for contact in contacts:
            if contacts[contact]["Phone Number"] == search_input:
                    
                while True:
                    field_input = input("What field would you like to edit? (Name / Phone Number / Email)")
                    
                    for item in contacts[search_input]:
                        if item == field_input:
                            update_input = input("What should this field now say?  ")
                            contacts[search_input][field_input] = update_input
                            
                            print(f"\nContact successfully updated! \n")
                            return

                    print("That is not a valid field.  Please try again.")
                    continue
            

        print("That is not a valid contact ID. Please try again.")
        continue
        

def delete_contact(contacts):
    while True:
        search_input = input("Please provider the contact ID (eg. phone number) of the contact that you would like to delete: ")
        
        for contact in contacts:
            if contacts[contact]["Phone Number"] == search_input:
                contacts.pop(contact)
                print("\nContact deleted successfully!\n")
                return

        continue_input = input("That contact is not in your contacts list.  Would you like to try another? (yes/no):  ")
        if continue_input.upper() != "YES":
            return


def search():
    while True:
        search_input = input("Please provider the contact ID (eg. phone number) of the contact that you would like to search for: ")

        for contact in contacts:
            if contact == search_input:
                print(f"\nContact found! \nContact ID: {contact}  \nName: {contacts[contact]['Name']}  \nPhone Number: {contacts[contact]['Phone Number']}  \nEmail: {contacts[contact]['Email']}\n")
                return
        
        continue_input = input("That contact is not in your contacts list.  Would you like to try another? (yes/no):  ")
        if continue_input.upper() != "YES":
            return


def display_contacts(contacts):
    for contact in contacts:
        print(f"\nContact ID: {contact}  \nName: {contacts[contact]['Name']}  \nPhone Number: {contacts[contact]['Phone Number']}  \nEmail: {contacts[contact]['Email']}\n")
    
def export_contacts():
    while True:
        search_input = input("Please provider the contact ID (eg. phone number) of the contact that you would like to export: ")

        for contact in contacts:
            if contact == search_input:
                entry = (f"\nContact ID: {contact}  \nName: {contacts[contact]['Name']}  \nPhone Number: {contacts[contact]['Phone Number']}  \nEmail: {contacts[contact]['Email']}\n")
                with open("Contacts.txt", 'a') as file:
                    file.write(entry)
                print("\nContact successfully exported.\n")
                return
            
        continue_input = input("That contact is not in your contacts list.  Would you like to try another? (yes/no):  ")
        if continue_input.upper() != "YES":
            return



contacts = {}

print("\nWelcome to the Contact Management System!")

while True:

    print("\nMenu\n1. Add a new contact  \n2. Edit an existing contact  \n3. Delete a contact  \n4. Search for a contact  \n5. Display all contacts  \n6. Export contacts to a text file  \n7. Quit")
    selection = input("Please make a selection: ")

    if selection == "1":
        add_contact(contacts)
    elif selection == "2":
        edit_contact(contacts)
    elif selection == "3":
        delete_contact(contacts)
    elif selection == "4":
        search()
    elif selection == "5":
        display_contacts(contacts)
    elif selection == "6":
        export_contacts()
    elif selection == "7":
        print("\nThank you for using the contact management system!")
        break
    else: 
        print("That is an invalid selection.  Please try again!")   

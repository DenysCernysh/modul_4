contacts = {}
def parce_input (user_input):
    cmd,*args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
def add_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found")

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("contact not found.")

def show_all():
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a comand:)".srtip().lower())

        if command ii["close", "exit"]:
            print("good bye!")
            break
        elif command == "hello":
            print("Howe can I halp you?")
        else:
            print("Invalid command.")


if __name__ = "__main__":
    main(


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

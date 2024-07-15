def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Command not recognized"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(name, contacts):
    return contacts[name]

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip()
        if command == "add":
            args = input("Enter the argument for the command: ").strip()
            print(add_contact(args, contacts))
        elif command == "phone":
            name = input("Enter the argument for the command: ").strip()
            print(get_phone(name, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()

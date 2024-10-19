def parse_input(user_input: str) -> tuple[str, list]:
    try:
        cmd, *args = user_input.split()
    except ValueError:
        # set default data to render the error msg
        cmd = ""
        args = []

    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Command has wrong format."

    name, phone = args

    operation_type = "added"

    if name in contacts:
        operation_type = "updated"

        # verify if contact is exists and waiting the answer if it is necessary
        while True:
            user_input = (
                input("Contact is exists, overwrite it(yes=default,no)? ") or "yes"
            )
            command, *args = parse_input(user_input)

            if command == "no":
                return ""
            elif command == "yes":
                break

    contacts[name] = phone

    return f"Contact {operation_type}."


def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Command has wrong format."

    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact was not found."


def show_contact(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Command has wrong format."

    name = args.pop()

    if name in contacts:
        return f"{name} has phone: {contacts[name]}"
    else:
        return "Contact was not found."


def show_all_contacts(contacts: dict) -> str:
    if len(contacts) > 0:
        # combine all contacts in one string
        data = "\n".join(
            [f"{name} has phone: {phone}" for name, phone in contacts.items()]
        )

        return data
    else:
        return "Contacts were not found."

def help_info(user_input, client):
    if len(user_input) == 1:
        client.print_help(client.json_data["help_messages"]["main"])
    elif len(user_input) == 2:
        command = user_input[1]
        if not client.json_data["help_messages"].get(command):
           print(f"Invalid argument. Command '{command}' is not valid.")
           return
        client.print_help(client.json_data["help_messages"][command])
    else:
        print("Too many arguments.")

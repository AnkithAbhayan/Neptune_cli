from source.command_funcs.cd import cd


def let(user_input, client):
    # full filtering
    parse_this = client.strip_spaces_and_slashes(user_input)

    # changing directories if existent
    if not parse_this:
        print("Please enter an arugment for 'let'.")
        return
    current_path = client.path[0 : len(client.path)]
    error = False
    for i in range(len(parse_this)):
        if cd(["cd", parse_this[i]], client) == "invalid":
            error = True
            parse_this = parse_this[i : len(parse_this)]
            break

    if error == False:
        print(
            "Looks like you're trying to confuse me.\nWhat is it that you want to add?"
        )
        return

    if client.IsAtHomeDir():
        if len(parse_this) < 2:
            subject = parse_this[0]
            print(f"Creating subject '{subject}'..")
            client.create_subject(subject)
            print("Done!")
        else:
            subject = parse_this[0]
            todo = " ".join(parse_this[1 : len(parse_this)])
            if not client.subject_exists(subject):
                print(f"Creating subject '{subject}'..")
                client.create_subject(subject)
            print(f"Adding todo to subject: '{subject}'..")
            client.create_todo(subject=subject, item=todo)
            print("Done!")

    else:
        todo = " ".join(parse_this)
        print(f"Adding todo to subject: '{client.path[1]}'..")
        client.create_todo(subject=client.path[1], item=todo)
        print("Done!")
    client.path = current_path

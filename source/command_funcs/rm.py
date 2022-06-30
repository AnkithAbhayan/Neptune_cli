from source.command_funcs.cd import cd


def rm(user_input, client):
    if len(user_input) == 1:
        print(f"Please enter an arument for '{user_input[0]}'.")
        return
    path_array = client.strip_spaces_and_slashes(user_input)

    current_path = client.path[0 : len(client.path)]
    for i in range(len(path_array) - 1):
        if cd(["cd", path_array[0]], client) == "invalid":
            return
        del path_array[0]
    # client.path = current_path
    # parsing
    path_array = path_array[0].split(",")
    path_array = [item.strip(" ") for item in path_array if item]

    if client.IsAtHomeDir():
        for subject_name in path_array:
            if not client.subject_exists(subject_name):
                print(f"Subject '{subject_name}' Doesn't exist. Skipping..")
                continue
            print(f"Deleting subject '{subject_name}'..")
            client.delete_subject(subject_name)
        print("Done!")

    else:
        for index in path_array:
            if not index.isdigit():
                print(f"Failed to convert '{index}' to int.")
            elif (int(index) >= len(client.json_data["subjects"][client.path[1]])):
                print(f"Index '{index}' out of range.")
            else:
                # deleting the thing
                index = int(index)
                print(f"Deleting index '{index}' from subject '{client.path[1]}'.")
                client.delete_todo(subject=client.path[1], index=index)
                client.json_data["subjects"][client.path[1]].insert(index, "")

        # fixing broken indexes
        for i in range(client.json_data["subjects"][client.path[1]].count("")):
            client.json_data["subjects"][client.path[1]].remove("")
        print("Done!")
    client.path = current_path

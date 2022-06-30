def cd(user_input, client):
    def first_check_of_dot_keys():
        if len(path_array) == 1:
            if path_array[0] == ".":
                return True
            elif path_array[0] == ".." and not client.IsAtHomeDir():
                del client.path[-1]
                return True
        return False

    def check_subjects():
        if len(path_array) == 1:
            if client.subject_exists(path_array[0]) and client.IsAtHomeDir():
                client.path.append(user_input[1])
            else:
                print(f"Unknown path '{'/'.join(path_array)}'")
                return "invalid"

    path_array = client.strip_spaces_and_slashes(user_input)

    if len(path_array) > 1:
        while len(path_array) > 0:
            # recursive loop since input too big
            if cd(["cd", path_array[0]], client) == "invalid":
                return "invalid"

            del path_array[0]

    elif first_check_of_dot_keys():
        return True

    return check_subjects()

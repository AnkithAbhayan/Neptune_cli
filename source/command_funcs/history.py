class parse:
    def parse_start_end_points(string):
        if string.count("-") > 1:
            print("Too many dividers. (-)")
            return None

        try:
            range_list = [int(item) for item in string.split("-") if item]
        except ValueError:
            print(
                "Error converting arguments to integer, enter start and end-points correctly."
            )
            return None

        if len(range_list) > 2:
            print("Too many start and end points. Make sure its just two.")
            return None
        if "-" in string and len(range_list) == 1:
            print("Negative values not allowed at the moment.")
            return None
        elif len(range_list) == 1:
            return range_list
        else:
            return range(range_list[0], range_list[1])


class HistoryCommands:
    def length(user_input, client):
        print(
            f"Displaying the length of command history/total number of commands entered-\n{len(client.json_data['history'])} items."
        )

    def clear(user_input, client):
        client.json_data["history"] = []
        print("Successfully cleared the command history!")

    def delete(user_input, client):
        if len(user_input) == 2:
            print("Argument for the start and end-point is non-existant.")
        else:
            list_of_indexes = parse.parse_start_end_points(user_input[2])
        count = 0
        for i in list_of_indexes:
            if not i >= 0:
                print("Numbers less than 0 can't be parsed.")
                continue
            try:
                del client.json_data["history"][i]
                count += 1
                client.json_data["history"].insert(i, "")
            except:
                if len(list_of_indexes) == 1:
                    print(f"Invalid index [{i}]")
                else:    
                    print(f"Invalid index(es) [{i}-{list_of_indexes[-1]}]")
                break
        for i in range(client.json_data["history"].count("")):
            client.json_data["history"].remove("")
        print(f"Successfully deleted {count} item(s) from the history.")

    def list_out(user_input, client):
        if len(user_input) <= 2:
            full_length = len(client.json_data["history"])
            list_of_indexes = range(full_length - 20, full_length)  # latest 20
        else:
            list_of_indexes = parse.parse_start_end_points(user_input[2])
        if not list_of_indexes:
            return

        for i in list_of_indexes:
            if i < -1:
                continue
            try:
                print(f" {i} {client.json_data['history'][i]}")
            except:
                if len(list_of_indexes) == 1:
                    print(f"Invalid index [{i}]")
                else:    
                    print(f"Invalid index(es) [{i}-{list_of_indexes[-1]}]")
                break


def history(user_input, client):
    if len(user_input) == 1:
        HistoryCommands.list_out(["history", "-l"], client)  # latest 20
    elif len(user_input) > 3:
        print("Too many arguments.")
    else:
        command_index = {
            "--clear": HistoryCommands.clear,
            "-c": HistoryCommands.clear,
            "--delete": HistoryCommands.delete,
            "-d": HistoryCommands.delete,
            "--show": HistoryCommands.list_out,
            "-s": HistoryCommands.list_out,
            "--length": HistoryCommands.length,
            "-l": HistoryCommands.length,
        }
        if func:=command_index.get(user_input[1]):
            func(user_input, client)
        else:
            print("Unknown argument for 'history'.")

        # range_str = [int(item) for item in user_input[1].split("-")]

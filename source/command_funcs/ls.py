def ls(user_input, client):
    def showtree(data):
        print("subjects")
        for key, value in data.items():
            for i in range(2):
                print("   |")
            print(f"   +--[{key}]:")
            if not value:
                print("   |    |")
                print("   |    +---<*Nothing here*>")
            else:
                no_spaces = (len(key) // 2) + 2
                if len(key) % 2 == 0:
                    no_spaces = (len(key) // 2) + 1
                print(f"   |{' '*no_spaces}|")
                for index, item in enumerate(value):
                    print(f"   |{' '*no_spaces}+---[{index+1}] {item}")
            print("   |")
        print("   =")

    def showlist(data):
        for key, value in data.items():
            print(f"{key}:")
            if value == []:
                print("<*Nothing here*>\n")
                continue
            print("\n".join(value) + "\n")

    data = client.json_data["subjects"]
    if len(client.path) != 1:
        data = {client.path[1]: client.json_data["subjects"][client.path[1]]}

    if len(user_input) > 1:
        if user_input[1] == "--tree":
            showtree(data)
            return
        elif user_input[1] != "--list":
            print("invalid argument.")
    showlist(data)

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

    dict1 = {
        "--tree":showtree,
        "-t":showtree,
        "--list":showlist,
        "-l":showlist
    }
    if client.path == ["home"]:
        data = client.json_data["subjects"]
    else:
        data = {client.path[1]: client.json_data["subjects"][client.path[1]]}

    if len(user_input) == 1:
        showlist(data)
    elif len(user_input) == 2:
        if client.json_data["subjects"].get(user_input[1]) in [True, []]: #either exists empty or has smth in it
            data = {user_input[1]: client.json_data["subjects"][user_input[1]]}
        elif not (func:=dict1.get(user_input[1])):
            print("Error: Invalid 1st argument for 'subject name' or 'format'.")
            return
        func = dict1.get(user_input[1], showlist)
        func(data) 
    
    elif len(user_input) == 3:
        subject = user_input[1]
        type1 = user_input[2]
        if not client.json_data["subjects"].get(subject):
            print("Error: Invalid 1st argument [subject name].")
            return
        else:
            data = {subject: client.json_data["subjects"][subject]} #1st argument subject data
            if func:=dict1.get(type1):
                func(data) #2nd argument format taken
            else:
                print("Error: Invalid 2nd argument for 'format'.")
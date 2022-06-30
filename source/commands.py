from source.command_funcs import rm, ls, cd, let, stop, save, history, help_info


def parse(user_input, client):
    command_palette = {
        "let": let.let,
        "cd": cd.cd,
        "ls": ls.ls,
        "del": rm.rm,
        "rm": rm.rm,
        "stop": stop.stop,
        "save": save.save,
        "history": history.history,
        "help": help_info.help_info,
    }
    if not user_input:
        print()
        return
    array = user_input.split()
    if command_palette.get(array[0]):
        command_palette[array[0]](array, client)
    else:
        print("Unknown Command.")
    print()

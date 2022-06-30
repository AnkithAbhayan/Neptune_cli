# 12/4/2021
# Dear future me,
# I can't even begin to express
# how sorry I am.

from source.commands import parse
from source.student import student
import json
import sys
import os

with open("source/data.json", "r") as JsonFile:
    data = json.load(JsonFile)

client = student(json_data=data)
client.check_running_instances()
client.first_time_usage_checker()
print(client.introduction_text)

while True:
    user_input = input(
        f"\033[1;33;40m{client.name}@{os.name} \033[1;36;40m/{'/'.join(client.path)}\033[1;37;40m\n$ "
    )
    client.log_history(user_input)
    parse(user_input, client)

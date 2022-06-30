import json
import sys
import string
import os


class student:
    def __init__(self, json_data):
        self.json_data = json_data
        self.name = self.json_data["name"]
        self.introduction_text = self.json_data["introduction_text"]
        self.path = self.json_data["path"]

    def check_running_instances(self):
        if self.json_data["running"] == False:
            self.json_data["running"] = True
            self.save()
        else:
            print("Either (or both) of the following happened:\nYou didn't close Nepture CLI properly (entering 'stop') the last time.\nOR\nAnother instance of Nepture CLI is running, close all instances and restart.")
            sys.exit()

    def first_time_usage_checker(self):
        def filter(name):
            if not name:
                return "Why did you leave this blank? Enter your name."
            elif name == "0":
                return "You just discovered a secret name that you can't use."
            elif len(name) < 3:
                return "I bet that your real name isn't less than 3 characters long."
            for item in string.punctuation:
                if item in name:
                    return "You can't use special characters like this one, sorry."
            for item in string.whitespace:
                if item in name:
                    return "Please remove all whitespaces in your name."

        if self.json_data["name"] == 0:
            print(
                "Hey! it looks like you're using this command-line interface for the first time.\n"
                "Would you like to enter your name? This piece of data will only be stored locally."
            )
            while True:
                name = input("Enter name: ")
                if output := filter(name):
                    print(output)
                    continue
                else:
                    print("Operation Successful!")
                    break
            self.json_data["name"] = name
            self.save()
            if os.name == 'nt': 
                os.system("cls")
            else:
                os.system("clear")

    def stop(self, running=False):
        self.json_data["path"] = ["home"]
        self.json_data["running"] = running
        with open("source/data.json", "w") as JsonFile:
            json.dump(self.json_data, JsonFile)
        sys.exit()

    def save(self):
        current_path = self.json_data["path"]
        self.json_data["path"] = ["home"]
        with open("source/data.json", "w") as JsonFile:
            json.dump(self.json_data, JsonFile, indent=4)
        with open("source/data.json", "r") as JsonFile:
            self.json_data = json.load(JsonFile)
        self.path = current_path
        self.json_data["path"] = current_path
        self.name = self.json_data["name"]
        self.introduction_text = self.json_data["introduction_text"]

    def IsAtHomeDir(self):
        if len(self.path) == 1:
            return True
        return False

    def log_history(self, user_input):
        if user_input:
            self.json_data["history"].append(user_input)

    def strip_spaces_and_slashes(self, data):
        if type(data) != list:
            data = data.split(" ")
        path_array = [item.strip(" ") for item in data if item]
        path_array = " ".join(path_array[1 : len(path_array)]).split("/")

        return path_array

    def create_subject(self, subject):
        self.json_data["subjects"].update({subject: []})

    def subject_exists(self, subject):
        returned_thing = self.json_data["subjects"].get(subject)
        if returned_thing or returned_thing == []:
            return True
        return False

    def delete_subject(self, subject):
        del self.json_data["subjects"][subject]

    def create_todo(self, subject, item):
        self.json_data["subjects"][subject].append(item)

    def delete_todo(self, subject, index):
        del self.json_data["subjects"][subject][index]

    def print_help(self, array):
        print("\n    "+"\n    ".join(array))

"""
file: train_run.py
by: Isaac McKinney

runs a simulated train yard based off a serious of user inputted commands
"""
from command_list import *


def process_commands(command, train):
    """
        process the inputted command
        pre-condition: command has been passed in as an input and a train has been created
        post-condition: command has been read and processed, train is adjusted accordingly
        :param command: the action the user wishes to have processed
        :param train: the linked list which represents the train
        :return: N/A
    """
    action = command.split()[0]
    if action == "set_speed":
        try:
            speed = command.split()[1]
            set_speed(speed, train)
        except ValueError:
            print("Illegal Command Use or Form")
    elif action == "help":
        help()
    elif action == "add_car":
        try:
            content, place, distance = command.split()[1:]
            add_car(content, place, distance, train)
        except ValueError:
            print("Illegal Command Use or Form")
    elif action == "quit":
        return quit()
    elif action == "train_size":
        print("Number of cars attached to the train is " + str(train_size(train)))
    elif action == "show_train":
        print(show_train(train))
    elif action == "start":
        if train.speed <= 0:
            print("Illegal Command Use or Form")
        else:
            start(train)
    else:
        print("Illegal Command Name: Command doesn't exist in database")
    command = str(input("Enter a command: "))
    process_commands(command, train)


def main():
    """
        initials the train(linked list), prints a welcome message, and compiles the program
        pre-condition: train is made and command is an empty string
        post-condition: train is manipulated appropriately and it is used in the sim.
        string is filled
        :return: N/A
    """
    train = Entire_Train(None, 0, 0)
    print("welcome to the train yard!")
    command = str(input("Enter a command: "))
    process_commands(command, train)


if __name__ == '__main__':
    main()

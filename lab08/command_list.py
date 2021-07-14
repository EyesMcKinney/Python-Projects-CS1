"""
file: command_list.py
By: Isaac McKinney

A series of commands used in a train yard simulation program
"""
from typing import Union
from dataclasses import dataclass


""" 
    a dataclass for an individual train car
    contents: the item/s in the train cars
    destination: the location of drop off for the train car contents
    miles: the distance to that destination
    next: a node which points to the current train car and links it to the next train car. 
    represents the next train car that is attached to the train, if there is one
"""
@dataclass(frozen=False)
class Train_Car:
    contents: str
    destination: str
    miles: int
    next: Union["Train_Car", None] = None


""" 
    a dataclass for the entire training
    head: creates the initial linked list for the train cars to be added too and will represent the back train car
    speed: the mph for which the car travels
    num_cars: the number of cars in the train
"""
@dataclass(frozen=False)
class Entire_Train:
    head: Union["Train_Car", None]
    speed: float
    num_cars: int


def set_speed(speed, train):
    """
        sets the train speed in mph
        pre-condition: command was called, speed > 0 has been inputted by the user, train has been created
        post-condition: train speed as been changed accordingly
        :param speed: the speed being added to the train
        :param train: the train that is having it's speed changed
        :return: the train with changed speed value
    """
    if float(speed) >= 0:
        train.speed = float(speed)
        return train
    else:
        raise ValueError


def add_car(content, place, distance, train):
    """
        adds a train car onto the train in the appropriate and optimal place
        pre-condition: command was called, contents, place, and distance have been inputted
        and train has been passed
        post-condition: a new train car is made with the appropriate arguments and added to the right spot
        :param content: train car contents
        :param place: the place for the contents to be delivered to
        :param distance: the total distance needed to travel to reach the place for drop-off
        :param train: the linked list being manipulated
        :return: the train with a new train car
    """
    car = Train_Car(content, place, distance, None)
    node = train.head
    if node is None:
        train.head = car
    else:
        successor = node
        previous = None
        while successor is not None:
            if int(successor.miles) < int(car.miles):
                previous = successor
                successor = successor.next
            else:
                if previous is not None:
                    previous.next = car
                else:
                    train.head = car
                car.next = successor
                break
        if successor is None:
            previous.next = car
    train.num_cars += 1
    return train


def train_size(train):
    """
        prints the number of train cars attached
        pre-condition: command is called, train is passed in and num_cars >= 0
        post-condition: train size is printed (the number of cars attached/linked together in the train)
        :param train: the linked list being manipulated
        :return: the number of train cars attached/linked
    """
    return train.num_cars


def show_train(train):
    """
        prints the train cars and the speed in a string presented as a list
        pre-condition: command is called, train is passed in and num_cars >= 0
        post-condition: train cars and train(engine) speed are printed
        :param train: the linked list being manipulated
        :return: engine speed as a float in mph and the string of train cars displayed in list format
    """
    print("engine (" + str(float(train.speed)) + ")")
    if train.head is None:
        result = []
        return result
    else:
        result = "[ Train_Car"
        node = train.head
        while node is not None:
            result += "(contents=" + str(node.contents) + " , "
            result += "destination=" + str(node.destination) + " , "
            result += "miles=" + str(node.miles) + ")"
            if node.next is not None:
                result += " , Train_Car"
            node = node.next
        result += " ]"
        return result


def start(train):
    """
        starts and runs the simulation
        pre-condition: command is called, train is created to the users desire(it is filled) and passed in,
        train speed is > 0
        post-condition: train is empty and appropriate output is printed
        :param train: the linked list being manipulated
        :return: N/A
    """
    travel_time = 0
    travel_dis = 0
    sep_time = 0.50
    if train.head is None:
        print("Illegal Command Use")
    else:
        while train.head is not None:
            if float(travel_dis) != float(train.head.miles):
                print("Moving on to " + str(train.head.destination) + ".")
                print(str(sep_time) + " hours taken to separate cars.")
                travel_time += sep_time
            x = (float(train.head.miles) - travel_dis) / float(train.speed)
            y = round(x, 2)
            if y != 0:
                print("this segment took " + str(y) + " to travel.")
                travel_dis = int(train.head.miles)
            travel_time += round(x, 2)
            print("Unloading " + str(train.head.contents) + " in " + str(train.head.destination) + ".")
            remove(train)
        print("total time for the trip was: " + str(round(travel_time, 2)) + " hours")
        print("total distance traveled is: " + str(travel_dis) + " miles")


def remove(train):
    """
        helper function that removes the head from the linked list
        pre-condition: train.head is not equal to None, and is passed in
        post-condition: train.head is changed to the next train car, train.head.next is the train.head
        :param train: the linked list being manipulated
        :return: the train with one less car, head is removed and replaced
    """
    if train.head is not None:
        temporary = train.head
        train.head = train.head.next
        temporary = None
        train.num_cars -= 1
    return train


def help():
    """
        prints out possible command options
        pre-condition: command is called
        post-condition: possible actions are printed out and shown to the user
        :return: N/A
    """
    print("List of Commands")
    print("=================")
    print("add_car < content > < station > < distance >")
    print("set_speed < speed >")
    print("train_size")
    print("show_train")
    print("start")
    print("help")
    print("quit")


def quit():
    """
        quits the program
        pre-condition: command is called
        post-condition: program is ended
        :return: N/A
    """
    print("Ending Train Yard Simulation")

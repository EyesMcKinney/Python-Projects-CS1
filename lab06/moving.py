"""
Author:Isaac McKinney
moving.py

Takes a text file telling us the box capacities and the items we want to store in those boxes for moving.
Then it takes those items and sorts them accordingly into the boxes
"""
from dataclasses import dataclass


@dataclass
class ITEM:
    """
    data class for items that will be put in boxes
    name: name of item
    weight: weight of item
    """
    name: str
    weight: int


@dataclass
class BOX:
    """
    data class for the boxes holding the items
    capacity: total allowable weight of box
    items: the list of items in that box
    """
    capacity: int
    items: []


def make_boxes_and_items(filename):
    """
    makes the boxes list and items list using the data classes
    pre-condition: filename is entered in
    post-condition: filename is entered in and both the boxes and items have been created
    :param filename: the text file being passed to make_boxes and make_items
    :return: boxes list and items list with appropriate keys and values
    """
    boxes = make_boxes(filename)
    items = make_items(filename)
    return boxes, items


def make_boxes(filename):
    """
    creates a list of empty boxes, which contain the box's weight limit and box's contents as a list from the dataclass
    pre-condition: filename is passed in and boxes list is empty
    post-condition: filename is passed in and boxes list is filled with the appropriate amount of boxes,
    each with corresponding capacities and items are
    :param filename: the text file being passed in to read and make boxes
    :return: the list of boxes, "boxes"
    """
    boxes = []
    with open(filename) as f:
        first_line = f.readline()
        parts = first_line.split(" ")
        for part in parts:
            newBox = BOX(int(part), [])
            boxes.append(newBox)
    return boxes


def make_items(filename):
    """
        creates a list of itens, which contain the item's weight and item's name as parts of the list from the dataclass
        pre-condition: filename is passed in and items list is empty
        post-condition: filename is passed in and items list is filled with the appropriate amount of items,
        each with corresponding capacities and items are
        :param filename: the text file being passed in to read and make items
        :return: the list of items, "items"
    """
    items = []
    with open(filename) as f:
        next(f)
        for part in f:
            newItem = ITEM(part.strip().split()[0], int(part.strip().split()[1]))
            items.append(newItem)
    return items


def sort_items(items):
    """
    sorts the unsorted items list in order of decreasing weight. (largest weight to smallest weight)
    pre-condition: items is passed in and unsorted
    post-condition: items is sorted
    :param items: the initial items list to be sorted
    :return: the sorted items list
    """
    if items == []:
        return []
    else:
        pivot = items[0].weight
        (less, same, more) = partition_items(pivot, items)
        return sort_items(less) + same + sort_items(more)


def sort_boxes(boxes):
    """
    sorts the boxes so the box of lowest capacity is being examined in tightest_fit
    pre-condition: boxes is passed in and unsorted
    post-condition: boxes is sorted from least to greatest
    :param boxes: the boxes list to be sorted
    :return: the sorted boxes list
    """
    if boxes == []:
        return []
    else:
        pivot = boxes[0].capacity
        (less, same, more) = partition_boxes(pivot, boxes)
        return sort_boxes(less) + same + sort_boxes(more)


def roomiest(items, boxes):
    """
    iterates through the items and places the item in the box with the greatest remaining allowed weight
    pre-condition: items and boxes are passed in, boxes are empty
    and all have capacity > than 0, items is sorted
    post-condition: boxes are filled and tell if either all items are packed or not
    :param items: the items being sorted in to the boxes
    :param boxes: the boxes being filled, each with a set capacity
    :return N/A
    """
    for item in items:
        largest_box = boxes[0]
        for box in boxes:
            if box.capacity > largest_box.capacity:
                largest_box = box
        if item.weight <= largest_box.capacity:
            largest_box.items.append(item)
            largest_box.capacity -= item.weight
    print("Box 1 of weight 12 capacity contains")
    for i in boxes[0].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 2 of weight 12 capacity contains")
    for i in boxes[1].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 3 of weight 12 capacity contains")
    for i in boxes[2].items:
        print(str(i.name) + " of weight " + str(i.weight))
    if boxes[0].capacity + boxes[1].capacity + boxes[2].capacity == 0:
        print("Successfully able to pack all items")
    else:
        print("Unable to pack all items")


def tightest_fit(items, boxes):
    """
        iterates through the items and places the item in the box with the least remaining allowed weight
        that will fit the item
        pre-condition: items and boxes are passed in, boxes are empty
        and all have capacity > than 0, items is sorted
        post-condition: boxes are filled and tell if either all items are packed or not
        :param items: the items being sorted in to the boxes
        :param boxes: the boxes being filled, each with a set capacity
        :return N/A
    """
    for item in items:
        boxes = sort_boxes(boxes)
        for box in boxes:
            if item.weight <= box.capacity:
                box.items.append(item)
                box.capacity -= item.weight
                break
    print("Box 1 of weight 12 capacity contains")
    for i in boxes[0].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 2 of weight 12 capacity contains")
    for i in boxes[1].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 3 of weight 12 capacity contains")
    for i in boxes[2].items:
        print(str(i.name) + " of weight " + str(i.weight))
    if boxes[0].capacity + boxes[1].capacity + boxes[2].capacity == 0:
        print("Successfully able to pack all items")
    else:
        print("Unable to pack all items")


def one_at_a_time(items, boxes):
    """
        iterates through the items and checks each box, one by one with the given item to see if it will fit in that box or not.
        if it fits, it will be placed in, even if that placement is not optimal
        pre-condition: items and boxes are passed in, boxes are empty
        and all have capacity > than 0, items is sorted
        post-condition: boxes are filled and tell if either all items are packed or not
        :param items: the items being sorted in to the boxes
        :param boxes: the boxes being filled, each with a set capacity
        :return N/A
    """
    for item in items:
        if item.weight <= boxes[0].capacity:
            boxes[0].items.append(item)
            boxes[0].capacity -= item.weight
        elif item.weight <= boxes[1].capacity:
            boxes[1].items.append(item)
            boxes[1].capacity -= item.weight
        elif item.weight <= boxes[2].capacity:
            boxes[2].items.append(item)
            boxes[2].capacity -= item.weight
    print("Box 1 of weight 12 capacity contains")
    for i in boxes[0].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 2 of weight 12 capacity contains")
    for i in boxes[1].items:
        print(str(i.name) + " of weight " + str(i.weight))
    print("Box 3 of weight 12 capacity contains")
    for i in boxes[2].items:
        print(str(i.name) + " of weight " + str(i.weight))
    if boxes[0].capacity + boxes[1].capacity + boxes[2].capacity == 0:
        print("Successfully able to pack all items")
    else:
        print("Unable to pack all items")


def partition_items(pivot, items):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    pre-condition: a pivot is selected and passed in and items is passed in as an unsorted list of data classes
    post-condition: pivot was used to sort the list around itself and items is now sort by decreasing weight
    :param pivot: the middle term being used to pivot the sorting lists around
    :param items: the items being sorted
    :return: less than list, same as pivot value list, and more than list
    """
    (less, same, more) = ([], [], [])
    for i in items:
        if i.weight < pivot:
            more.append(i)
        elif i.weight > pivot:
            less.append(i)
        else:
            same.append(i)
    return less, same, more


def partition_boxes(pivot, boxes):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    pre-condition: a pivot is selected and passed in and items is passed in as an unsorted list of data classes
    post-condition: pivot was used to sort the list around itself and items is now sort by decreasing weight
    :param pivot: the middle term being used to pivot the sorting lists around
    :param boxes: the items being sorted
    :return: less than list, same as pivot value list, and more than list
    """
    (less, same, more) = ([], [], [])
    for i in boxes:
        if i.capacity < pivot:
            less.append(i)
        elif i.capacity > pivot:
            more.append(i)
        else:
            same.append(i)
    return less, same, more


def main():
    """
        takes an inputted text file from the user and shows how it would work and what results would be given
        when ran through 3 different types of greedy algorithms
        pre-condition: file is an empty input file
        post-condition: file is a text file and has been inputted by the user and the results from each strategy have
        been printed
        :return N/A
    """
    file = input("Enter data filename: ")
    print("results from greedy strategy 1")
    run_roomiest(file)
    print()
    print("results from greedy strategy 2")
    run_tightest_fit(file)
    print()
    print("results from greedy strategy 3")
    run_one_at_a_time(file)


def run_one_at_a_time(filename):
    """
        creates a copy of the boxes and sorted items and then tests our desired file items on one_at_a_time()
        pre-condition: file is passed in, boxes are make and items sorted
        post-condition: one_at_a_time is ran and the boxes are filled accordingly with items
        :param filename: the text file being read off of to make items and boxes
        :return: N/A
    """
    boxes, initial_items = make_boxes_and_items(filename)
    items = sort_items(initial_items)
    one_at_a_time(items, boxes)


def run_tightest_fit(filename):
    """
        creates a copy of the boxes and sorted items and then tests our desired file items on tightest_fit()
        pre-condition: file is passed in, boxes are make and items sorted
        post-condition: tightest_fit is ran and the boxes are filled accordingly with items
        :param filename: the text file being read off of to make items and boxes
        :return: N/A
    """
    boxes, initial_items = make_boxes_and_items(filename)
    items = sort_items(initial_items)
    tightest_fit(items, boxes)


def run_roomiest(filename):
    """
        creates a copy of the boxes and sorted items and then tests our desired file items on roomiest()
        pre-condition: file is passed in, boxes are make and items sorted
        post-condition: roomiest is ran and the boxes are filled accordingly with items
        :param filename: the text file being read off of to make items and boxes
        :return: N/A
    """
    boxes, initial_items = make_boxes_and_items(filename)
    items = sort_items(initial_items)
    roomiest(items, boxes)


if __name__ == '__main__':
    main()

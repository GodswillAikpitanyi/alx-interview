#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    stack = [0]  # Start with the first box
    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]
        for key in keys:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)


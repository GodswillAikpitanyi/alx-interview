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
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    # Starts with the first box
    stack = [0]
    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]
        for key in keys:
            if key >= 0 and key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)

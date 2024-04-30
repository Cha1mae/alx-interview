#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    """ Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of boxes where
        each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    if n == 0:
        return True

    seen = set()  # Set to keep track of visited boxes
    Qyu = deque([0])  # Start with the first box (index 0)

    while Qyu:
        thee_box = Qyu.popleft()  # Dequeue the next box to explore
        if thee_box not in seen:
            seen.add(thee_box)  # Mark the box as visited
            keys = boxes[thee_box]
            for key in keys:
                if key < n and key not in seen:
                    Qyu.append(key)  # Enqueue the key's box if not visited

    return len(seen) == n

# Test cases


boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

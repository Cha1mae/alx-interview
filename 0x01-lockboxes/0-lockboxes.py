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

    seen = set()
    Qyu = deque([0])

    while Qyu:
        thee_box = Qyu.popleft()
        if thee_box not in seen:
            seen.add(thee_box)
            keys = boxes[thee_box]
            for key in keys:
                if key < n and key not in seen:
                    Qyu.append(key)

    return len(seen) == n

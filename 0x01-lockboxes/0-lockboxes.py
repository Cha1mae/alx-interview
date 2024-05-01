#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    n = len(boxes)
    keys = [0]
    opened = [False] * n
    opened[0] = True

    while keys:
        key = keys.pop()
        for box in boxes[key]:
            if box < n and not opened[box]:
                keys.append(box)
                opened[box] = True

    return all(opened)

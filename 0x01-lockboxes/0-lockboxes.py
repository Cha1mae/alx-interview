#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
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

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False

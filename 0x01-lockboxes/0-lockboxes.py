#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False

    g = len(boxes)
    if g == 0:
        return True

    seen = set()
    Qyu = deque([0])

    while Qyu:
        thee_box = Qyu.popleft()
        if thee_box not in seen:
            seen.add(thee_box)
            keys = boxes[thee_box] 
            for key in keys:
                if key < g and key not in seen:
                    Qyu.append(key)

    return len(seen) == g

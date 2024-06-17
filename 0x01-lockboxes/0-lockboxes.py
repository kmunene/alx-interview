#!/usr/bin/python3
"""locboxes"""


def canUnlockAll(boxes):
    """determines if all boxes can be opened"""

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

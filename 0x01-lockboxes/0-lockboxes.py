#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):

    unlocked = [boxes[0]]

    for box in unlocked:
        for key in box:
            try:
                if boxes[key] not in unlocked:
                    unlocked.append(boxes[key])
            except Exception:
                break
    
    if len(unlocked) != len(boxes):
        return False
    return True

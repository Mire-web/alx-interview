#!/usr/bin/python3
"""
Implementation of the Lockbox challenge solution in Python
Author: Mirey-dev(formerly mire-web)
"""


def canUnlockAll(boxes):
    """ Check if all boxes can be unlocked """
    keys = set([0])  # Store found keys
    for idx, box in enumerate(boxes):
        for key in box:
            if key > 0 and key < len(boxes):
                if key != idx:
                    keys.add(key)
        if len(keys) == len(boxes):
            return True
    return False

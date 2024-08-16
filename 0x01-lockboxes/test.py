#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
boxes1 = [[2, 3], [2, 0], [4], [1, 5], [], [3]]
print(canUnlockAll(boxes1))
boxes2 = [[1], [2, 3, 4], [], [], [5], [6], []]
print(canUnlockAll(boxes2))
boxes3 = [[1, 2, 3], [], [4, 5], [1], [], [], [6]]
print(canUnlockAll(boxes3))
boxes1 = [[1], [2], [3], [4], [], []]
print(canUnlockAll(boxes1))
boxes1 = [[1, 4], [2, 5], [], [2, 6], [3], [7], [8], [], [0]]
print(canUnlockAll(boxes1))
boxes2 = [[1, 3], [4], [5], [9], [], [7], [8], [2], []]
print(canUnlockAll(boxes2))

"""
ECE606, F'19, Assignment 2, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following methods. You are
allowed to define whatever subroutines you like to
structure your code.
"""

# Python program for insert and search
# operation in a Trie


def trieInsert(t, s):
    """
    You need to implement this method.
    """
    if not t:
        t = [[[], [], [], []], False]
    root = t
    for level in range(len(s)):
        index = int(s[level])
        if not root[0][index]:
            root[0][index] = [[[], [], [], []], False]
        root = root[0][index]
    root[1] = True


def trieDelete(t, s):
    """
    You need to implement this method.
    """
    if not t:
        return
    for level in range(len(s)):
        index = int(s[level])
        if not t:
            return
        t = t[0][index]
    t[1] = False


def trieFind(t, s):
    """
    You need to implement this method.
    """
    t = [[[], [], [], []], False] if not t else t
    for level in range(len(s)):
        index = int(s[level])
        if not t[0][index]:
            return False
        t = t[0][index]
    return t is not None and t[1]

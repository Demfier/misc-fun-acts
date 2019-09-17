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


def getStringsAsList(t, prefix, result):
    """
    Given trie t, and a prefix string prefix, add all strings we find
    in t to the list result
    """

    if not t:
        return
    if len(t) == 0:
        return
    if t[1]:  # the prefix string is in the set
        result.append(prefix)

    for i in range(4):
        newprefix = prefix + str(i)
        getStringsAsList(t[0][i], newprefix, result)


def trieInsert(t, s):
    """
    You need to implement this method.
    """
    triestrings = []
    getStringsAsList(t, '', triestrings)
    triestrings.append(s)
    t = [[[], [], [], []], False] if not t else t
    for s in triestrings:
        pCrawl = t
        for level in range(len(s)):
            index = int(s[level])
            if not pCrawl[0][index]:
                pCrawl[0][index] = [[[], [], [], []], False]
            pCrawl = pCrawl[0][index]
        pCrawl[1] = True
    return t


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

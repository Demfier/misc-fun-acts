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


class Trie:
    def __init__(self):
        self.epsilon = [[], [], [], []]
        self.is_terminal = False


def insert_helper(t):
    n = Trie()
    t.append(n.epsilon)
    t.append(n.is_terminal)


def trieInsert(t, s):
    sub_t = t
    if(len(t) == 0):
        insert_helper(t)
    if(len(s) == 0):
        t[1] = True
    for i in range(len(s)):
        index = ord(s[i]) - ord('0')
        sub_t = sub_t[0][index]
        if(len(sub_t) == 0):
            insert_helper(sub_t)
    sub_t[1] = True


def delete_helper(t, s, level):
    if(level < len(s)):
        index = int(s[level])
        if(len(t) == 0):
            return []
        t[0][index] = delete_helper(t[0][index], s, level + 1)
        if(t == [[[], [], [], []], False]):
            t = []
    if level == len(s):
        if len(t[0][0]) > 0 or len(t[0][1]) > 0 or len(t[0][2]) > 0 or len(t[0][3]) > 0:
            t[1] = False
        else:
            t = []
    return t


def trieDelete(t, s):
    if(not trieFind(t, s)):
        return
    temp = t
    t = delete_helper(temp, s, 0)
    if(t == [[[], [], [], []], False]):
        t.clear()


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

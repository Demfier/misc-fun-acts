#! /usr/bin/python3

import sys
import random
from a2p4 import trieInsert, trieDelete, trieFind

"""
Some tests.

If you set this file to executable, and have the a2p4.py file in
the same folder, then you should be able to run this.
"""

def isLeaf(t):
    try:
        if(len(t[0][0]) == 0 and len(t[0][1]) == 0 and len(t[0][2]) == 0 and len(t[0][3]) == 0):
            return True
        return False
    except:
        return False

def consistent(t):
    """
    Consistency check on the structure of the trie, t.
    Returns True or False.
    Consistency means: a leaf must be a terminal.
    """
    try:
        if len(t) == 0:
            return True

        if(isLeaf(t)):
            return t[1]

        # Walk the trie recursively
        for i in range(4):
            if(not consistent(t[0][i])):
                return False
        return True
    except Exception as e:
        print(e)
        return False

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

def randstring(len):
    """
    Return a random string of length len
    """
    ret = ''
    for i in range(len):
        ret = ret + str(random.randint(0, 3))
    return ret

def main():
# The following t is the trie from the assignment handout. In case
# you want to construct your own tests with it.
#    t = [[[[[[[], [], [], []], True], [[[[[[[],[],[],[]], True],[],[],[]],True], [], [], []], False], [], []], False], [[[], [], [[[], [], [], [[[], [[[], [], [], []], True], [], []], False]], True], []], False], [[[], [[[[[], [], [], []], True], [], [], []], False], [], []], False], []], False]
#    prefix = ''
#    triestrings = []
#    getStringsAsList(t, prefix, triestrings)
#    print(triestrings)

    slist = []
    nstrings = random.randint(100, 200)
    for i in range(nstrings):
        slen = random.randint(0, 20)
        slist.append(randstring(slen))

    print('Testing trieInsert()...', end='')
    t = []
    for s in slist:
        trieInsert(t, s)
    print(t)
    prefix = ''
    triestrings = []
    getStringsAsList(t, prefix, triestrings)
    slistunique = list(set(slist))

    if((sorted(slistunique) != sorted(triestrings)) or (not consistent(t))):
        print('failed')
    else:
        print('passed')

    print('Testing trieFind()...', end='')
    stofind = []
    for s in slist:
        if random.randint(0, 1):
            stofind.append(s)

    extrafind = random.randint(0, 25)
    for i in range(extrafind):
        stofind.append(randstring(random.randint(10, 20)))

    random.shuffle(stofind)

    failed = False
    for s in stofind:
        if((trieFind(t, s) != (s in slist)) or (not consistent(t))):
            print('failed')
            failed = True
            break
    if not failed:
        print('passed')

    print('Testing trieDelete()...', end='')
    stodelete = stofind
    prefix = ''
    triestringsold = []
    getStringsAsList(t, prefix, triestringsold)
    for s in stodelete:
        trieDelete(t, s)
        if s in slistunique:
            slistunique.remove(s)

    prefix = ''
    triestrings = []
    getStringsAsList(t, prefix, triestrings)
    print((sorted(slistunique) == sorted(triestrings)), consistent(t))
    print(len(triestringsold), len(triestrings), len(slistunique))
    if((sorted(slistunique) != sorted(triestrings)) or (not consistent(t))):
        print('failed')
    else:
        print('passed')


if __name__ == '__main__':
    main()

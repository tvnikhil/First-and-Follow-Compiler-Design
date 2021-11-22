def getFirst(first, completed, productions, lhs):
    if lhs.islower():
        return lhs
    if completed[lhs] == 1:
        return first[lhs]
    rhs = productions[lhs]
    for i in rhs:
        if i[0].isupper():
            s1 = set(first[lhs])
            s2 = set(getFirst(first, completed, productions, i[0]))
            if "#" in s2:
                j = i[1:]
                s2 = (s2 - set("#")).union(getFirst(first, completed, productions, j[0]))
            s1 = s1.union(s2)
            first[lhs] = list(s1)
        else:
            first[lhs].append(i[0])
    completed[lhs] = 1
    return first[lhs]


def First(productions):
    first, completed = {}, {}
    for i in productions:
        completed[i] = 0
        first[i] = []
    for lhs in productions:
        getFirst(first, completed, productions, lhs)
    return first

def getFirstAlpha(first, alpha, tFirst):
    c = alpha[0]
    if (ord(c) >= 33 and ord(c) <= 64) or (ord(c) >= 91 and ord(c) <= 126):
        tFirst = tFirst | {c}
        return tFirst
    f = set(first[c])
    if "#" in f:
        i = 1
        while "#" in f:
            tFirst = tFirst | (f - {"#"})
            if alpha[i:] == "":
                tFirst = tFirst | {"#"}
                break
            f = set(getFirstAlpha(first, alpha[i:], tFirst))
            tFirst = tFirst | (f - {"#"})
            i += 1
    else:
        tFirst = tFirst | f
    return tFirst

def getFollow(first, follow, completed, productions, lhs):
    if completed[lhs] == 1:
        return set(follow[lhs])
    follow_set = set()
    for i in productions:
        rhs = productions[i]
        for j in rhs:
            if j != "#":
                for idx in range(0, len(j)):
                    if j[idx] == lhs:
                        if idx + 1 == len(j):
                            if i != j[idx]:
                                follow_set = follow_set.union(getFollow(first, follow, completed, productions, i))
                        else:
                            temp = set()
                            temp = temp | set(getFirstAlpha(first, j[idx+1:], temp))
                            tFirst = list(temp)
                            if "#" not in tFirst:
                                follow_set = follow_set.union(tFirst)
                            else:
                                follow_set = follow_set.union((set(tFirst) - set("#")).union(getFollow(first, follow, completed, productions, i)))
    follow[lhs] = list(set(follow[lhs]) | follow_set)
    completed[lhs] = 1
    return set(follow[lhs])


def Follow(productions, first):
    follow, completed = {}, {}
    for i in productions:
        completed[i] = 0
        follow[i] = []
    startSymbol = list(productions.keys())[0]
    follow[startSymbol].append("$")
    for lhs in productions:
        getFollow(first, follow, completed, productions, lhs)
    return follow

n = int(input())
productions = {}
for i in range(0, n):
    inpPro = input()
    inpPro = list(inpPro.split("->"))
    productions[inpPro[0]] = list(inpPro[1].split("|"))
print("First for the grammar is ")
first = First(productions)
for i in first:
    print(i, ":", first[i])
print()
print("Follow for the grammar is ")
follow = Follow(productions, first)
for i in follow:
    print(i, ":", follow[i])

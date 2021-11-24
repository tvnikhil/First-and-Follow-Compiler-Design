def getFirstOfAlpha(first, alpha, tFirst):
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
            f = set(getFirstOfAlpha(first, alpha[i:], tFirst))
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
                            temp = temp | set(getFirstOfAlpha(first, j[idx+1:], temp))
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
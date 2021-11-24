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

def checkCombination(comb: tuple, positions: list) -> bool:
    ret = True
    for p in comb:
        if p not in positions:
            ret = False
    return ret

def deleteCombination(comb: tuple, positions: list):
    for p in comb:
        key = positions.index(p)
        del positions[key]

def get(data: list) -> int:

    positions = list(data)
    treeComb   = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6))
    treeRate   = 97
    twoComb    = ((0,1), (3,4), (6,7), (1,2), (4,5), (7,8),(0,3), (1,4), (2,5), (3,6), (4,7), (5,8),(0,4), (2,4), (4,8), (4,6))
    twoRate    = 6
    calc = 0

    for comb in treeComb:
        if checkCombination(comb, positions):
            calc = calc + treeRate
            deleteCombination(comb, positions)

    for comb in twoComb:
        if checkCombination(comb, positions):
            calc = calc + twoRate
            deleteCombination(comb, positions)

    return calc + len(positions)

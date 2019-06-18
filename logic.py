import calc

def do(data: dict) -> int:

    field  = data['field']
    active = data['active']

    positionsUser     = list() 
    positionsOpponent = list() 
    positionsFree     = list()

    i = 0
    for value in field:
        if value == active:
            positionsUser.append(i)
        elif value == 0:
            positionsFree.append(i)
        else:
            positionsOpponent.append(i)
        i = i + 1

    maxCalc = -777
    choose  = 666
    for positionFree in positionsFree:
        #print("\n>>>>>>>>\n")
        #print(positionFree)
        newPositionsUser = list(positionsUser)
        newPositionsUser.append(positionFree)
        newPositionsOpponent = list(positionsOpponent)
        newPositionsOpponent.append(positionFree)
        u = calc.get(newPositionsUser) 
        o = calc.get(newPositionsOpponent)
        #print(u)
        #print(o)
        calculate = u + o
        if maxCalc < calculate:
            #print("ADD")
            choose = positionFree
            maxCalc = calculate 
        #print("\n<<<<<<<\n")
    return choose

#data = {"users":{"bot":1, "device":2}, "active":1, "field":[0,0,2,1,2,1,0,0,0]}
#do(data)

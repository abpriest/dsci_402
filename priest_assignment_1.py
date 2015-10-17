#Alex Priest
def flatten(mess):
        if mess == []:
                return []
        if type(mess[0]) != type([]):
                return [mess[0]] + flatten(mess[1:])
        return flatten(mess[0]) + flatten(mess[1:])

def powerset(foo):
        if foo== []:
                return[foo]
        rest = powerset(foo[1:])
        return map(lambda x: [foo[0]] + x, rest) + powerset(foo[1:])

def all_perms(thing):
        result = []
        if len(thing) <= 1:
                return [thing]
        for i in range(0,len(thing)):
                stuff = thing[i+1:] + thing[:i]
                result += (map(lambda x: [thing[i]] + x, all_perms(stuff)))
        return result

def spiral(n):
        res = []
        for i in range(0,n):
                res.append([])
                for j in range(0,n):
                        res[i].append(-1)
        x = 0
        y = n-1
        currentVal = (n**2)-1
        dist = n-1
        traveled = 0
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        timesMovedInDirection = -1
        res[x][y] = currentVal
        while currentVal > 0:
                currentVal -= 1
                x += directions[0][0]
                y += directions[0][1]
                res[x][y] = currentVal
                traveled += 1
                if traveled == dist:
                        timesMovedInDirection += 1
                        if timesMovedInDirection == 2:
                                dist -= 1
                                timesMovedInDirection = 0
                        directions.append(directions[0])
                        directions = directions[1:]
                        traveled = 0

        return res

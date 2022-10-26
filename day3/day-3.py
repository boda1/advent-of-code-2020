routeFile = open('./input.txt')
routes = routeFile.readlines()
currentPosition = 0
allSquares = []
numberOfTrees = 0


for i in range(len(routes)):
    if currentPosition <= 30:
        allSquares = allSquares + [routes[i][currentPosition]]
        currentPosition += 3
    elif currentPosition > 30:
        currentPosition = currentPosition - 31
        allSquares = allSquares + [routes[i][currentPosition]]
        currentPosition += 3

for j in range(len(allSquares)):
    if allSquares[j] == '#':
        numberOfTrees += 1

print(allSquares)
print(numberOfTrees)


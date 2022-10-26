routeFile = open('./input.txt')
routes = routeFile.readlines()
currentPosition = 0
squaresRight = 1
allSquares = []
numberOfTrees = 0


for i in range(0, len(routes), 2):
    if currentPosition <= 30:
        allSquares = allSquares + [routes[i][currentPosition]]
        currentPosition += squaresRight
    elif currentPosition > 30:
        currentPosition = currentPosition - 31
        allSquares = allSquares + [routes[i][currentPosition]]
        currentPosition += squaresRight


for j in range(len(allSquares)):
    if allSquares[j] == '#':
        numberOfTrees += 1


print(allSquares)
print(numberOfTrees)

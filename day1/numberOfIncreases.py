def calculateIncrease(valueArray):
    increaseCount = 0
    last = valueArray[0]
    for item in valueArray:
        if item > last:
            increaseCount += 1
        last = item
    return increaseCount

inputFile = open("input.txt", "r")
dataArray = []

windowArray = []
for line in inputFile.readlines():
    dataArray.append(int(line.replace("\n", "")))


for i in range(len(dataArray)):
    if i+2 <= len(dataArray)-1:
        windowArray.append(dataArray[i] + dataArray[i+1] + dataArray[i+2])


print(calculateIncrease(dataArray))
print(calculateIncrease(windowArray))


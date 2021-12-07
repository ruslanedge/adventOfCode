inputFile = open("input.txt", "r")
dataArray = []
for line in inputFile.readlines():
    dataArray.append(int(line.replace("\n", "")))

increaseCount = 0
last = dataArray[0]
for item in dataArray:
    if item != dataArray[0] and item > last:
        increaseCount += 1
    last = item

print(increaseCount)

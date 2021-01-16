#========================
# Earthquake Analysis:
# Lists all the states/countries with their respective earthquake magnitudes
#========================


file  = open("2.5_day.csv", "r")
fileType = file.readline().split(",")

placeList = list()
magList = list()
updatedList = list()
mergeList = list()
listFiles = file.readlines()

for i in listFiles:
    updatedList.append(i.split(','))

for j in updatedList:
    magList.append(j[4])
    placeList.append(j[13])
    placeList.append(j[14])

tracker = 0
trackerP = 1
trackerM = 0
trackerL = 0

while trackerL < len(placeList):
    if tracker % 2 != 0:
        if placeList[trackerP] == "earthquake":
            mergeList.append(placeList[trackerP-1].replace("\"", "").lstrip(" "))
            trackerP += 2
            trackerL += 1
            tracker += 1
        else:
            mergeList.append(placeList[trackerP].replace("\"", "").lstrip(" "))
            trackerP += 2
            trackerL += 1
            tracker += 1         
    else:
        mergeList.append(magList[trackerM].lstrip(" "))
        trackerM += 1
        trackerL += 1
        tracker += 1

for k in range(0, len(mergeList), 2):
    print(mergeList[k], mergeList[k+1])

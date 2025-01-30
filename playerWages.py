#COMPUTERS HOMEWORK THURSDAY - PLAYERS WAGES
#TASKS - 1 to 5

import statistics
file = open("playerWages.csv", "r")   #the csv file does not exist!!!! tried a variety of different ways!!!
dataIn = file.read()
myList = dataIn.split("\n")
myList = [int(item) for item in myList]
myList = [item for item in myList if item !=0]

#sorting from highest to lowest
myList.sort(reverse = True)
print(myList)

#finding the maximum and minimum values
maxValue = myList[0]
minValue = myList[-1]
print("The maximum wage is:", maxValue)
print("The minimum wage is:", minValue)

#finding the mean of all the wages
sumValues = 0
for item in myList:
    sumValues += item
average = sumValues / len(myList)
print("The average of the wages are:", )

#finding the median of the wages
if len(myList) % 2 == 0:
    middlePlusOne = len(myList) // 2
    median = (myList[middlePlusOne -1] + myList[middlePlusOne]) / 2
else:
    middle = len(myList) // 2
    median = myList[middle]
print("The middle number is:", median)

#finding the mode of the wages
import statistics
mode = statistics.mode(myList)
print(mode)

#cant figure out frequency!!!!!1

#If the mode is less than the mean it means that more of the population is below the average

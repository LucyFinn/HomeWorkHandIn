#PG 79 + 80 TASKS 1 TO 5!!!
#Task 1
myList = [12, 3, -15, 26, -2, 13, -4, 16]
print(myList)
for i in myList:
    if i < 0:
        myList.remove(i)
print(myList)

#Task 2
file = open("newCSV.csv", "w")
nums = [12, 77, 42, 93, 13, 5, 90, 55, 49, 20, 32, 45, 80, 11, 25, 66, 81, 31, 98,37]
print(len(nums))
nums.sort(reverse = True)
print("Sorted descending: ", nums)
print("Maximum Value:", nums[0])
print("Minmum Value:", nums[-1])
file.close()

#Task 3
file = open("myCSV.csv", "w")
import random
# randNumber = random.randint(0,100)
numList = []
for i in range (10):
    randNumber = random.randint(0,100)
    numList.append(randNumber)
    print(randNumber)
    file.write("," + str(randNumber)) 
print(numList)
file.close()

#now we are going to use list comprehension
#Task 4 
bigNumbers = 0
for i in (numList):
    if i >= 50:
        bigNumbers += 1
print(bigNumbers)
# bigNumbers.sort()
# print("Sorted ascending ", bigNumbers)
#wont allow to sort the data as an int or a string

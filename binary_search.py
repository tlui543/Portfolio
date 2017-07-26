import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)


# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algo
countryIWant = input ("Which country do you want?")

beginningIndex = 0
endingIndex = len(elementsList)-1
index = int((endingIndex+beginningIndex)/2)


while elementsList[index] != countryIWant:
    print (index)
    if index == len(elementsList[index])-2:
        word == list[endingIndex]
    elif countryIWant > elementsList[index]:
        beginningIndex = index
        endingIndex = endingIndex
        index = int((endingIndex+beginningIndex)/2)
    elif countryIWant < elementsList[index]:
        beginningIndex = beginningIndex
        endingIndex = index
        index=int((endingIndex+beginningIndex)/2)



    else:
        print (index)
        break

print(index)

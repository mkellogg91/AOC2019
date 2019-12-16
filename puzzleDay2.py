data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]


def arrayFormatter(myArray, x, y):
    myArray[1] = x
    myArray[2] = y
    for index in xrange(0, len(myArray), 4):

        if index >= (len(myArray) - 4):
            break
        
        pos1Val = myArray[index+1]
        pos2Val = myArray[index+2]
        resultPosVal = myArray[index+3]

        if myArray[index] == 1:
            sumResult = myArray[pos1Val] + myArray[pos2Val]
            myArray[resultPosVal] = sumResult
        elif myArray[index] == 2:
            multResult = myArray[pos1Val] * myArray[pos2Val]
            myArray[resultPosVal] = multResult
        elif myArray[index] == 99:
            break
        else:
            break
    return myArray[0]

x = 0
y = 0
for x in range(0, 100):
    for y in range(0, 100):
        data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,9,19,23,2,23,13,27,1,27,9,31,2,31,6,35,1,5,35,39,1,10,39,43,2,43,6,47,1,10,47,51,2,6,51,55,1,5,55,59,1,59,9,63,1,13,63,67,2,6,67,71,1,5,71,75,2,6,75,79,2,79,6,83,1,13,83,87,1,9,87,91,1,9,91,95,1,5,95,99,1,5,99,103,2,13,103,107,1,6,107,111,1,9,111,115,2,6,115,119,1,13,119,123,1,123,6,127,1,127,5,131,2,10,131,135,2,135,10,139,1,13,139,143,1,10,143,147,1,2,147,151,1,6,151,0,99,2,14,0,0]
        
        resultFound = arrayFormatter(data, x, y)
        
##        print("result found here:")
##        print(resultFound)
        
        if resultFound == 19690720:
            print("result found!")
            print("x was:")
            print(x)
            print("y was:")
            print(y)
        
        y = y + 1
    x = x + 1


print("end")

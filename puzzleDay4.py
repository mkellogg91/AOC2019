
# Rules
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# Input range: 130254-678275     = 548021 (n absolute worst case before checking rules)

# checks if the length of the number is 6 digits
def checkNumLen(num):
    return len(str(num)) == 6

# checks if the number contains two adjacent digits that are the same and that numbers stay the same or are in increasing order
def checkAdjacentDigits(num):
    numArray = list(map(int, list(str(num))))

    adjacentEquivalentDigits = False
    adjacentValue = 0
    definiteSetOfTwoAdjacentValuesOnlyCount = 0

    # only looping to the second to last item as each iteration looks at n compared to n+1 (item to the right)
    for n in range(0, len(numArray) - 1):
        if (not(numArray[n+1] >= numArray[n])):
            return False
        
        # if two numbers were already found next to each other, checks if n+1 equals the value of the last found adjacent value
        if adjacentEquivalentDigits and (numArray[n+1] == adjacentValue):
            adjacentEquivalentDigits = False
        
        # if two numbers were already found next to each other, 
        if adjacentEquivalentDigits and not(numArray[n+1] == adjacentValue):
            definiteSetOfTwoAdjacentValuesOnlyCount += 1

        if numArray[n+1] == numArray[n] and not(numArray[n+1] == adjacentValue):
            adjacentEquivalentDigits = True
            adjacentValue = numArray[n]
    # if we looped through the whole number without returning false, check if there is a set of matching adjacent numbers
    if definiteSetOfTwoAdjacentValuesOnlyCount > 0 or adjacentEquivalentDigits == True:
        return True
    else:
        return False


##### Part 1 #####
meetsCriteriaCount = 0

for x in range(130254, 678275):
    if checkNumLen(x) and checkAdjacentDigits(x):
        meetsCriteriaCount += 1

print("number of passwords that meet criteria:")
print(meetsCriteriaCount)
    


##### Part 2 #####

#guessed 1209, it was TOO LOW 
#guessed 1419, it was Correct!

# test values used to check if checkAdjacentDigits works: 
# 112233 should be true, 
# 123444 should be false, 
# 111122 should be true, 
# 133444 should be true


# part two is the same because I just added an additional "if" to the adjacent checker that checks - 
# if adjacentEquivalentDigits is already true (equivalent side-by-side digits were found last iteration) 
# but the n+1 value this iteration is the same value as the equivalent numbers last iteration (we have 3 or more side by side numbers) 
# set adjacentEquivalentDigits to false

# First guess was wrong because at the end of looping through a 6 digit number I would only check to see if adjacentEquivalentDigits was True, 
# but in a number like 133444, although it has a good pair of 3's it will say false because it found the "444" at the end 
# and set adjacentEquivalentDigits = False. 
# so while 111122 would work having adjacentEquivalentDigits = True at the end of iteration, 133444 would fail. 
# This led me to add a counter for a good pair of digits earlier in the number. 
# if the counter is greater than zero, OR we end the iteration with adjacentEquivalentDigits = true 
# then we have found a legitimate number.



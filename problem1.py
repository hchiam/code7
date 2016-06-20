# python code for problem 1

currentSchoolGrade = ""
currentCity = ""
currentState = ""
currentNumber = ""
# create a dictionary
dict = {}

# a function:
def createEntries(s,c,g,n,*x):
    listFields = [s,c,g,n]
    # print s,c,g,n
    for field in listFields:
        key = field
        if key in dict:
            dict[key] += int(n) # add to running number
        else:
            dict[key] = int(n) # create new entry in dictionary
        # print "CURRENT DICTIONARY:  ", dict

# here is where the file is read & processed:
with open("problem1.csv") as file:
    for line in file:
        # print line
        splitLine = line.split(",")
        # print "ENTRY READ:  ",splitLine
        state = splitLine[0]
        city = splitLine[1]
        schoolGrade = splitLine[2]
        number = int(splitLine[3][1:])
        # print number
        createEntries(state,city,schoolGrade,number)
        if currentSchoolGrade != schoolGrade and currentSchoolGrade != "":
            print currentSchoolGrade,"\t","\t","\t","\t",dict[currentSchoolGrade]
        if currentCity != city and currentCity != "":
            print currentCity,"\t","\t","\t",dict[currentCity]
        if currentState != state and currentState != "":
            print currentState,"\t","\t",dict[currentState]
        currentSchoolGrade = schoolGrade
        currentCity = city
        currentState = state
        currentNumber = number
print state,number
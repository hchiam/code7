# python code for problem 1

# create a dictionary
dict = {}

# a function:
def createEntries(s,c,g,n,*x): # this function has *x, which means it can take any number of parameters, besides the minimum of four
    listFields = [s,c,g,n]
    # print s,c,g,n
    for field in listFields:
        key = field
        if key in dict:
            dict[key] += int(n) # add to running number
        else:
            dict[key] = int(n) # create new entry in dictionary
        # print "CURRENT DICTIONARY:  ", dict

def mainPart():
    currentSchoolGrade = ""
    currentCity = ""
    currentState = ""
    currentNumber = ""
    # here is the main part of the code, where the file is read & processed:
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
    # and then print the items for the last line
    print currentSchoolGrade,"\t","\t","\t","\t",dict[currentSchoolGrade]
    print currentCity,"\t","\t","\t",dict[currentCity]
    print currentState,"\t","\t",dict[currentState]
    output = currentState + "\t" + "\t" + str(dict[currentState])
    return output


# extra stuff to showcase a unittest check
# see https://docs.python.org/2.7/library/unittest.html for more info and where I got derived the following code from:

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        print "\n"
        self.assertEqual(mainPart(), "NY		6686")
        print "\n"

suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner(verbosity=2).run(suite)




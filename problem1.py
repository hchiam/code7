# python code for problem 1

with open("problem1.csv") as file:
    for line in file:
        print line
        splitLine = line.split(",")
        print splitLine
        state = splitLine[0]
        city = splitLine[1]
        schoolGrade = splitLine[2]
        number = splitLine[3]
        print number
        number = number.replace("K","")
        print number

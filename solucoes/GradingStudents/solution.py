#!/bin/python3

def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] >= 38:
            rest = 5 - (grades[i] % 5)
            if rest < 3:
                grades[i] += rest

    return grades

if __name__ == '__main__':
    arr = [73, 67, 38, 33]
    print(gradingStudents(arr))
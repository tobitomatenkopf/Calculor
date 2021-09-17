import re


def checkForError(string) -> bool:
    return False


def checkForInput(string) -> bool:
    if string == '':
        return True
    return False


def transformToList(string) -> list:  # 3 + 3 x 3 -> [3, +, [3, x, 3]]  ) )
    inpList = string.split(' ')
    cleanInpList = []
    for element in inpList:
        if ('(' in element) or (')' in element):
            cleanInpList.append(element[0])
            if len(element) > 1:
                cleanInpList.append(element[1])
        elif element != '':
            cleanInpList.append(element)
        else:
            print(1)
    print(cleanInpList)
    calcList = []
    i = 0
    a = 0
    passing = False
    for piece in cleanInpList:
        if passing:
            passing = False
        elif piece == '(':
            inBracket = []
            bracketCounter = 0
            for piece2 in cleanInpList[i:]:
                if piece2 == '(':
                    bracketCounter += 1
                    inBracket.append('(')
                elif piece2 == ')':
                    bracketCounter -= 1
                    inBracket.append(')')
                elif bracketCounter != 0:
                    inBracket.append(piece2)
                else:
                    # TODO
                    # getting rid of the last bracket
                    calcList.append(transformToList(inBracket))
                    break

        elif piece.isnumeric():
            calcList.append(int(piece))
        elif piece == '+' or piece == '-':
            calcList.append(piece)
        elif piece == 'x' or piece == '/':
            previousPiece = calcList[i - 1]
            calcList = calcList[:-1]
            calcList.append([previousPiece, piece, int(cleanInpList[a + 1])])
            passing = True
            i -= 2

        a += 1
        i += 1
    return calcList


def calc(calcList) -> int:
    midSolution = []
    for piece in calcList:
        if type(piece) == list:
            midSolution.append(calc(piece))
        else:
            midSolution.append(piece)
    solution = midSolution[0]
    i = 0
    for piece in midSolution:
        if piece == '+':
            solution += midSolution[i + 1]
        elif piece == '-':
            solution -= midSolution[i + 1]
        elif piece == 'x':
            solution *= midSolution[i + 1]
        elif piece == '/':
            solution /= midSolution[i + 1]
        i += 1
    return solution


def calcSolution(inp) -> str:
    if checkForInput(inp):
        return ''
    if checkForError(inp):
        return 'Error'
    print(1)
    calcList = transformToList(inp)
    print(calcList)
    return str(calc(calcList))

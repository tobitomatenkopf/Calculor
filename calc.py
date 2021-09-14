def checkForError(string) -> bool:
    calcList = string.split(' ')
    previousPiece = '0'
    for piece in calcList:
        if (not piece.isnumeric()) and (not previousPiece.isnumeric()):
            return True
        previousPiece = piece
    return False


def transformToList(string) -> list:  # 3 + 3 x 3 -> [3, +, [3, x, 3]]
    inpList = string.split(' ')
    calcList = []
    i = 0
    a = 0
    passing = False
    for piece in inpList:
        if passing:
            passing = False
        elif piece.isnumeric():
            calcList.append(int(piece))
        elif piece == '+' or piece == '-':
            calcList.append(piece)
        elif piece == 'x' or piece == '/':
            previousPiece = calcList[i - 1]
            calcList = calcList[:-1]
            calcList.append([previousPiece, piece, int(inpList[a + 1])])
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
    if checkForError(inp):
        return 'Error'
    calcList = transformToList(inp)
    print(str(calc(calcList)))
    return str(calc(calcList))


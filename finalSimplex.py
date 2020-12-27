def createTableau(raw_investments, raw_constraints, objective):
    '''
    using a subroutine so this process can be repeated and altered
    easily
    '''
    
    '''
    assuming the constraints are in the correct format:
     - in the form of a less than or equal to inequality
     - there are no negative variables

        EXAMPLE TABLEAU
    constraint0  = [1, -1.015,   -1.2,  -1.05, -1.005, -1.022,  -1.01, -1.001, 0, 0, 0, 0, 0, 0,     0]
    constraint1  = [0,      1,      1,      1,      1,      1,      1,      1, 1, 0, 0, 0, 0, 0,  5000]
    constraint4  = [0,      0,      0,      0,      1,      0,      1,      1, 0, 1, 0, 0, 0, 0,  1000]
    constraint6  = [0,      1,      1,      1,      0,      0,      1,      1, 0, 0, 1, 0, 0, 0,  2500]
    constraint8  = [0,      0,      0,      0,      0,      1,      0,      0, 0, 0, 0, 1, 0, 0,  4500]
    constraint10 = [0,      1,      1,      6,     10,     15,      3,      1, 0, 0, 0, 0, 1, 0, 40000]
    constraint11 = [0,    5.0,    4.9,    3.8,    2.5,    1.5,    3.2,    5.0, 0, 0, 0, 0, 0, 1, 11000]
    '''

    def addSlack(length, position):
        '''
        adding slack values to the simplex tableau is an often
        repeated task, especially with many constraints, so this
        task has been written into a subroutine
        '''
        slack = []
        for value in range(position - 1):
            slack.append(0)
        slack.append(1)
        while len(slack) < length:
            slack.append(0)
        return slack

    def objective1():
        '''
        the objective line is the first row of the simplex tableau as it is the
        row that needs to be optimised
        the objective row is of varient length and so the program will iterate
        through the objective variable
        the objective row must accomodate for slack variable columns, but the
        objective equation is not an inequality and so does not need any value
        for those columns
        '''
        row1 = [1]
        for each in objective:
            row1.append(-each)
            '''
            using the negative values from the rearranged objective equation
            '''
        for i in range(7 + len(raw_investments)):
            row1.append(0)
            '''
            no slack variables in the objective equation
            '''
        
        return row1

    def constraint1():
        row2 = [0]
        for each in raw_investments:
            row2.append(1)
        for each in addSlack((6 + len(raw_investments)), 1):
            row2.append(each)
        row2.append(raw_constraints[0][1])
        
        return row2

    def constraint4():
        row3 = [0]
        for row in raw_investments:
            if row[2] < raw_constraints[2][1]:
                row3.append(1)
            else:
                row3.append(0)
        for each in addSlack((6 + len(raw_investments)), 2):
            row3.append(each)
        row3.append(raw_constraints[0][1] * raw_constraints[3][1] * 0.01)
        
        return row3

    def constraint6():
        row4 = [0]
        for row in raw_investments:
            if row[3] > raw_constraints[4][1]:
                row4.append(1)
            else:
                row4.append(0)
        for each in addSlack((6 + len(raw_investments)), 3):
            row4.append(each)
        row4.append(raw_constraints[0][1] * raw_constraints[5][1] * 0.01)
        
        return row4

    def constraint8():
        row5 = [0]
        for row in raw_investments:
            if row[1] > raw_constraints[6][1]:
                row5.append(1)
            else:
                row5.append(0)
        for each in addSlack((6 + len(raw_investments)), 4):
            row5.append(each)
        row5.append(raw_constraints[0][1] * raw_constraints[7][1] * 0.01)
        
        return row5

    def constraint10():
        row6 = [0]
        for row in raw_investments:
            row6.append(row[1])
        for each in addSlack((6 + len(raw_investments)), 5):
            row6.append(each)
        row6.append(raw_constraints[0][1] * raw_constraints[9][1])

        return row6

    def constraint11():
        row7 = [0]
        for row in raw_investments:
            row7.append(row[3])
        for each in addSlack((6 + len(raw_investments)), 6):
            row7.append(each)
        row7.append(raw_constraints[0][1] * raw_constraints[10][1])

        return row7

    def constraint2(investment, position):
        '''
        constraint: 'Maximum Percentage Invested Per Investment'
        creating a black row with profit value completed
        only one investment counts towards the solution per row for this constraint
        add the coefficient of 1 to represent that investment
        the slack position is variable depending on the number of rows already added
        the maximum amount per investment is the percentage of the maximum amount
        '''
        addedRow = [0]
        for row in raw_investments:
            if row[0] == investment:
                addedRow.append(1)
            else:
                addedRow.append(0)
        for each in addSlack((6 + len(raw_investments)), position):
            addedRow.append(each)
        addedRow.append(raw_constraints[0][1] * raw_constraints[1][1] * 0.01)

        return addedRow
            
    simplexTableau = [objective1(), constraint1(), constraint4(), constraint6(), constraint8(), constraint10(), constraint11()]

    position = len(simplexTableau)
    for investment in raw_investments:
        simplexTableau.append(constraint2(investment[0], position))
        position += 1

    return simplexTableau

def optimiseTableau(simplexTableau):
    '''
    this subroutine will be used to find the optimum values out of the
    default simplex test data
    to simulate iterations of the simplex tableau, this subroutine will
    be repeated, but because of the test data, it may only take a few
    iterations to come to an optimised solution
    '''

    # FINDING THE PIVOT COLUMN AND ROW INDEXES

    leastValue = simplexTableau[0][1]
    for value in simplexTableau[0]:
        if value < leastValue:
            leastValue = value

    pivotColumn = simplexTableau[0].index(leastValue)

    minValue = (simplexTableau[1][len(simplexTableau[1]) - 1] / simplexTableau[1][pivotColumn])
    pivotRow = 1
    for index in range(2, len(simplexTableau)):
        try:
            if (simplexTableau[index][len(simplexTableau[index]) - 1] > 0 and
            (simplexTableau[index][len(simplexTableau[index]) - 1] / simplexTableau[index][pivotColumn]) < minValue):
                pivotRow = index
        except ZeroDivisionError:
            pass

    '''
    finding the pivot column and row for which the iteration of the
    simplex method is based upon
    the ZeroDivisionError might occur as variables may have a 
    coefficient of zero, meaning this must be caught and passed as a 
    possibility for a pivot row
    using this style of coding using these indexes reduces the hard
    coding within the program and will make the transfer onto the 
    real program easier
    '''

    # CHANGING THE VALUES IN THE SIMPLEX TABLEAU

    for x in range(0, len(simplexTableau)):
        if x == pivotRow:
            continue
        rowMuliplier = -simplexTableau[x][pivotColumn] / simplexTableau[pivotRow][pivotColumn]
        for y in range(0, len(simplexTableau[x])):
            simplexTableau[x][y] += (simplexTableau[pivotRow][y] * rowMuliplier)

    rowDivisor = 1 / simplexTableau[pivotRow][pivotColumn]
    for z in range(0, len(simplexTableau[pivotRow])):
        simplexTableau[pivotRow][z] *= rowDivisor
    '''
    this is the method of altering the values of the simplex tableau
    to get closer to the optimum values for each of the variables
    '''

    return simplexTableau


def checkOptimum(simplexTableau):
    '''
    this subroutine is used to check if the contents of the simplex
    tableau contain an optimum solution by checking the objective
    row in the tableau for any negative numbers; if any are found, the
    tableau is not yet optimised
    '''

    for value in simplexTableau[0]:
        if value < 0:
            return False
    return True


def findOptimum(simplexTableau, raw_investments):
    '''
    this is the subroutine that will find the values of the most optimum
    solution for the problem given that the problem is either optimum or
    there have been too many iterations
    '''

    simplexResults = {}

    for column in range(1, (len(simplexTableau[0]) - (7 + len(raw_investments)))):
        if simplexTableau[0][column] > 0:
            simplexResults[raw_investments[column-1][0]] = 0
        elif simplexTableau[0][column] == 0:
            for row in simplexTableau:
                if 0.99999 < row[column] < 1.00001:
                    simplexResults[raw_investments[column-1][0]] = row[len(simplexTableau[0]) - 1]
                    
    for investment, value in simplexResults.items():
        if value < 0:
            simplexResults[investment] = 0

    return simplexResults

def findProfit(simplexResults, simplexTableau, raw_constraints, raw_investments):
    '''
    separate function to return the values of the total money after the
    investments and the expected profit
    '''

    profit = 0
    total = sum(simplexResults.values())
    for key, value in simplexResults.items():
        for each in raw_investments:
            if each[0] == key:
                profit += (value * (1 + (0.01 * each[2]))) - value
    remaining = raw_constraints[0][1] - sum(simplexResults.values())

    return total, profit, remaining


def findClientInvestments(simplexResults):
    '''
    this subroutine will find all the investments which the simplex
    algorithm has said to give positive value to the profit, and add
    them to a list to be returned to the main program and eventually,
    the user
    '''
    
    clientInvestments = []
    
    for key, value in simplexResults.items():
        if value > 0:
            clientInvestments.append([key, value])

    return clientInvestments

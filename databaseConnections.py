import sqlite3

'''
assign one database file to be used thoughout these subroutines
'''
databaseFile = 'ProgramDatabase.db'


#   CreateNewAccount

def checkUsernameTaken(username):
    '''
    select all of the data in the Advisor table
    iterate thought all the usernames in that data
    if any of them are equal to the new username,
    return that the username is taken
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Advisor''')
    for row in cursor:
        if row[5] == username:
            conn.commit()
            conn.close()
            return True
    
    conn.commit()
    conn.close()
    
    return False

def addAdvisor(firstName, lastName, phoneNumber, email, username, password):
    '''
    pass all the details into the function
    insert into the database the new advisor's details
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO Advisor(FirstName, LastName, PhoneNumber, Email, Username, Password)
                  VALUES(?,?,?,?,?,?)''', (firstName, lastName, phoneNumber, email, username, password))
    
    conn.commit()
    conn.close()


#   LoginPage

def checkPassword(username, password):
    '''
    select everything from the Advisor table
    compare each username and password to the inputted username and password
    if either is not a match,
    return that the login was unsuccessful
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM Advisor''')
    for row in cursor:
        if row[5] == username and row[6] == password:
            conn.commit()
            conn.close()
            return True

    conn.commit()
    conn.close()

    return False

def findAdvisorID(username):
    '''
    
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT AdvisorID FROM Advisor WHERE Username = ?''', (username,))
    for row in cursor:
        constraintID = row[0]
    
    conn.commit()
    conn.close()

    return constraintID


#   InvestmentManagement

def findInvestments():
    '''
    select everything from the Investments table
    for each investment, add the ID and name to separate lists
    concatinate the IDs and names together into the investments list
    return the investments list for use elsewhere
    '''
    investmentIDs = []
    investmentNames = []
    investments = {}
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Investments''')
    for row in cursor:
        investmentIDs.append(row[0])
        investmentNames.append(row[1])

    conn.commit()
    conn.close()

    for index in range(len(investmentIDs)):
        investments[investmentIDs[index]] = (investmentNames[index])

    return investments

def addInvestment(name, maturity, returns, risk):
    '''
    pass all the details into the function
    insert into the database the new advisor's details
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO Investments(Name, Maturity, Returns, Risk)
                  VALUES(?,?,?,?)''', (name, maturity, returns, risk))
    
    conn.commit()
    conn.close()

def checkInvestmentExists(name):
    '''
    select all of the data in the Investments table
    iterate thought all the names in that data
    if any of them are equal to the new investment name,
    return that the name is taken
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM Investments''')
    for row in cursor:
        if row[1] == name:
            conn.commit()
            conn.close()
            return True
    
    conn.commit()
    conn.close()
    
    return False

def removeInvestment(investmentID):
    '''
    pass in the InvestmentID that you want to remove
    drop the row where the InvestmentID is the that ID
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM Investments WHERE InvestmentID = ?''', (investmentID,))

    conn.commit()
    conn.close()


#   ViewInvestment

def displayInvestment(investmentID):
    '''
    pass in an InvestmentID you want to display
    select the investment from the Investments table where the InvestmentID is the ID
    return the whole row
    '''
    details = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT Name, Maturity, Returns, Risk FROM Investments WHERE InvestmentID = ?''', (investmentID,))
    for row in cursor:
        conn.commit()
        conn.close()
        return row


#   ClientManagement

def findClients(advisorID):
    '''
    select everything from the Clients table
    for each client, add the ID, first name and last name to separate lists
    concatinate the IDs and names together into the clients list
    return the clients list for use elsewhere
    '''
    clientIDs = []
    firstNames = []
    lastNames = []
    clients = {}
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Clients WHERE AdvisorID = ?''', (advisorID,))
    for row in cursor:
        clientIDs.append(row[0])
        firstNames.append(row[1])
        lastNames.append(row[2])

    conn.commit()
    conn.close()

    for index in range(len(clientIDs)):
        clients[clientIDs[index]] = (firstNames[index] + ' ' + lastNames[index])

    return clients

def addClient(firstName, lastName, phoneNumber, email, advisorID):
    '''
    pass in the new client's details
    insert the new client into the Clients table
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO Clients(FirstName, LastName, PhoneNumber, Email, AdvisorID)
                  VALUES(?,?,?,?,?)''', (firstName, lastName, phoneNumber, email, advisorID))
    
    conn.commit()
    conn.close()

def checkClientExists(clientID):
    '''
    select all of the data in the Clients table
    iterate thought all the IDs in that data
    if any of them are equal to the given ClientID,
    return that the client already exists
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM Clients''')
    for row in cursor:
        if row[0] == clientID:
            conn.commit()
            conn.close()
            return True
    
    conn.commit()
    conn.close()
    
    return False

def removeClient(clientID):
    '''
    pass the client's ID into the subroutine
    remove details relating the client in all tables
    commit the changes
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM Clients WHERE ClientID = ?''', (clientID,))
    cursor.execute('''DELETE FROM ClientConstraints WHERE ClientID = ?''', (clientID,))
    
    conn.commit()
    conn.close()


#   ClientInvestments

def displayClient(clientID):
    '''
    find the row in the clients table with the ClientID passed in
    take all the details in the row and return them to be used elsewhere
    '''
    details = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT FirstName, LastName, PhoneNumber, Email FROM Clients WHERE ClientID = ?''', (clientID,))
    for row in cursor:
        details = row

    conn.commit()
    conn.close()

    return details


#   UpdateDetails

def updateClient(clientID, firstName, lastName, phoneNumber, email):
    '''
    find the client using the ClientID which is passed in
    update all the details with the new details which are passed in
    commit the new details
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''UPDATE Clients SET FirstName = ?, LastName = ?, PhoneNumber = ?, Email = ? WHERE ClientID = ?''', (firstName, lastName, phoneNumber, email, clientID))

    conn.commit()
    conn.close()


#   ConstraintsManagement

def findClientConstraints(clientID):
    '''
    create an empty list to hold the client constraints
    locates all the constraints in the ClientConstraints table using the ClientID
    fill the empty list with the constraints from each corresponding row
    '''
    clientConstraints = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM ClientConstraints WHERE ClientID = ?''', (clientID,))
    for row in cursor:
        clientConstraints.append(findConstraintName(row[1]))

    conn.commit()
    conn.close()

    return clientConstraints

def findConstraintID(constraintName):
    '''
    
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT ConstraintID FROM Constraints WHERE Name = ?''', (constraintName,))
    for row in cursor:
        constraintID = row[0]
    
    conn.commit()
    conn.close()

    return str(constraintID)

def findConstraintName(constraintID):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT Name FROM Constraints WHERE ConstraintID = ?''', (constraintID,))
    for row in cursor:
        constraintName = row[0]
    
    conn.commit()
    conn.close()

    return constraintName

def findConstraintValue(clientID, constraintID):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT Value FROM ClientConstraints WHERE ClientID = ? AND ConstraintID = ?''', (clientID, constraintID))
    for row in cursor:
        value = row[0]
    
    conn.commit()
    conn.close()

    return value

def findConstraintExists(clientID, constraintID):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT Value FROM ClientConstraints WHERE ClientID = ? AND ConstraintID = ?''', (clientID, constraintID))
    for row in cursor:
        if row[0] != None:
            conn.commit()
            conn.close()
            return True
        
    conn.commit()
    conn.close()

    return False

def addConstraint(clientID, constraintID, value):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO ClientConstraints(ClientID, ConstraintID, Value)
                  VALUES(?,?,?)''', (clientID, constraintID, value))

    conn.commit()
    conn.close()

def updateConstraint(clientID, constraintID, value):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''UPDATE ClientConstraints SET Value = ? WHERE ClientID = ? AND ConstraintID = ?''', (value, clientID, constraintID))

    conn.commit()
    conn.close()

def removeConstraint(clientID, constraintID):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM ClientConstraints WHERE ClientID = ? AND ConstraintID = ?''', (clientID, constraintID))

    conn.commit()
    conn.close()


#   InvestmentOptimization

def checkPairs(clientID):
    '''
    pass the ClientID into the function
    select all of the constraints relating to this client
    fill the first list with all of the constraints
    check() function checks that if the parameter constraint exists,
    its pair (the constraint before it in the table) is in the table
    each of the constraints with paired values is checked
    if any return to not have the paired value, the function returns false;
    otherwise returns true
    '''
    table = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM ClientConstraints WHERE ClientID = ?''', (clientID,))
    for row in cursor:
        table.append(row)

    conn.commit()
    conn.close()
        
    def check(constraintID):
        secondCheck = []
        for row in table:
            if row[1] == constraintID:
                for each in table:
                    secondCheck.append(each[1])
                if str((int(constraintID) - 1)) not in secondCheck:
                    return False
        return True

    if False in (check('4'), check('6'), check('8')):
        return False
    return True

def countConstraints(clientID):
    counter = 0
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM ClientConstraints WHERE ClientID = ?''', (clientID,))
    for row in cursor:
        counter += 1
        if row[1] in ('3', '5', '7', '9'):
            counter -= 1

    conn.commit()
    conn.close()

    return counter

def findInvestmentFromName(investmentName):
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT InvestmentID, Maturity, Returns FROM Investments WHERE Name = ?''', (investmentName,))

    for row in cursor:
        investment = row

    conn.commit()
    conn.close()

    return row

def clearInvestments(clientID):
    '''
    
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM ClientInvestments WHERE ClientID = ?''', (clientID,))

    conn.commit()
    conn.close()

def storeInvestment(clientID, investmentID, amountInvested, timeRemaining, predictedFinal):
    '''
    
    '''
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO ClientInvestments(ClientID, InvestmentID, AmountInvested, TimeRemaining, PredictedFinal)
                  VALUES(?,?,?,?,?)''', (clientID, investmentID, amountInvested, timeRemaining, predictedFinal))

    conn.commit()
    conn.close()

def tableData(clientID):
    '''

    '''
    tupleInvestments = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT InvestmentID, AmountInvested, TimeRemaining, PredictedFinal FROM ClientInvestments WHERE ClientID = ?''', (clientID,))

    for row in cursor:
        tupleInvestments.append(row)
    tableInvestments = [list(item) for item in tupleInvestments]

    for each in tableInvestments:
        cursor.execute('''SELECT Name FROM Investments WHERE InvestmentID = ?''', (each[0],))
        for row in cursor:
            each[0] = row[0]

    conn.commit()
    conn.close()

    return tableInvestments
    

#   Simplex

def packInvestments():
    '''
    
    '''
    investments = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT Name, Maturity, Returns, Risk FROM Investments''')
    for row in cursor:
        investments.append(row)

    conn.commit()
    conn.close()

    return investments

def packConstraints(clientID):
    '''

    '''
    unsortedConstraints = []
    sortedConstraints = []
    conn = sqlite3.connect(databaseFile)
    cursor = conn.cursor()

    cursor.execute('''SELECT ConstraintID, Value FROM ClientConstraints WHERE ClientID = ?''', (clientID,))

    for row in cursor:
        unsortedConstraints.append(row)

    for value in range(1, 12):
        for row in unsortedConstraints:
            if row[0] == str(value):
                sortedConstraints.append(row)

    return sortedConstraints

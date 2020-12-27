from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
from finalSimplex import *
from databaseConnections import *
from createPDF import *
import re
import string


class Ui_MYWINDOW(object):
    
    def setupUi_LoginPage(self, MYWINDOW):

        def clearLoginPage():
            """
            changing the text within the line edits to nothing;
            same effect as clearing the line edits.
            """
            self.lineEdit_Password.setText("")
            self.lineEdit_Username.setText("")

        def enterLoginPage():
            """
            taking the text from the line edits and putting them into
            variables that the program can manipulate and use.
            then clearing the line edits.
            """
            username = self.lineEdit_Username.text()
            password = self.lineEdit_Password.text()
            clearLoginPage()

            """
            using the function from the databaseConnections file to
            check if the username exists and matches the password.
            else the program warns the user of invalid details.
            """
            if checkPassword(username, password) == True:
                global advisorID
                advisorID = findAdvisorID(username)
                openAdvisorLogin()
            else:
                self.label_Error.setText("Incorrect username or password.")
            
        
        MYWINDOW.setObjectName("MYWINDOW")
        MYWINDOW.resize(1000, 500)
        MYWINDOW.setMinimumSize(QtCore.QSize(1000, 500))
        MYWINDOW.setMaximumSize(QtCore.QSize(1000, 500))
        MYWINDOW.setWindowOpacity(1.0)
        MYWINDOW.setAutoFillBackground(False)
        MYWINDOW.setStyleSheet("selection-background-color: rgb(200, 200, 200);\n"
"selection-color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(MYWINDOW)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox_Details = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_Details.setGeometry(QtCore.QRect(360, 240, 280, 210))
        self.groupBox_Details.setObjectName("groupBox_Details")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_Password.setGeometry(QtCore.QRect(60, 100, 160, 22))
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_Enter = QtWidgets.QPushButton(self.groupBox_Details)
        self.pushButton_Enter.setGeometry(QtCore.QRect(170, 150, 80, 30))
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.pushButton_Enter.clicked.connect(enterLoginPage)
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_Details)
        self.pushButton_Clear.setGeometry(QtCore.QRect(40, 150, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Clear.clicked.connect(clearLoginPage)
        self.label_Username = QtWidgets.QLabel(self.groupBox_Details)
        self.label_Username.setGeometry(QtCore.QRect(62, 26, 141, 21))
        self.label_Username.setObjectName("label_Username")
        self.label_Password = QtWidgets.QLabel(self.groupBox_Details)
        self.label_Password.setGeometry(QtCore.QRect(62, 76, 141, 21))
        self.label_Password.setObjectName("label_Password")
        self.lineEdit_Username = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_Username.setGeometry(QtCore.QRect(60, 50, 160, 22))
        self.lineEdit_Username.setText("")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.groupBox_Register = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_Register.setGeometry(QtCore.QRect(740, 420, 240, 60))
        self.groupBox_Register.setObjectName("groupBox_Register")
        self.label_Resigter = QtWidgets.QLabel(self.groupBox_Register)
        self.label_Resigter.setGeometry(QtCore.QRect(21, 24, 113, 16))
        self.label_Resigter.setObjectName("label_Resigter")
        self.pushButton_Register = QtWidgets.QPushButton(self.groupBox_Register)
        self.pushButton_Register.setGeometry(QtCore.QRect(140, 21, 75, 23))
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.pushButton_Register.clicked.connect(openCreateNewAccount)
        self.pushButton_Help = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Help.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.pushButton_Help.clicked.connect(openHelpPage)
        self.label_Image = QtWidgets.QLabel(self.centralWidget)
        self.label_Image.setGeometry(QtCore.QRect(240, 49, 520, 151))
        self.label_Image.setObjectName("label_Image")
        MYWINDOW.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MYWINDOW)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        MYWINDOW.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MYWINDOW)
        self.statusBar.setObjectName("statusBar")
        MYWINDOW.setStatusBar(self.statusBar)
        self.label_Error = QtWidgets.QLabel(self.centralWidget)
        self.label_Error.setGeometry(QtCore.QRect(360, 450, 280, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label")

        _translate = QtCore.QCoreApplication.translate
        MYWINDOW.setWindowTitle(_translate("MYWINDOW", "Login"))
        self.groupBox_Details.setTitle(_translate("MYWINDOW", "Details"))
        self.pushButton_Enter.setText(_translate("MYWINDOW", "Enter"))
        self.pushButton_Clear.setText(_translate("MYWINDOW", "Clear"))
        self.label_Username.setText(_translate("MYWINDOW", "Username"))
        self.label_Password.setText(_translate("MYWINDOW", "Password"))
        self.groupBox_Register.setTitle(_translate("MYWINDOW", "Register"))
        self.label_Resigter.setText(_translate("MYWINDOW", "Don\'t have an account?"))
        self.pushButton_Register.setText(_translate("MYWINDOW", "Register"))
        self.pushButton_Help.setText(_translate("MainWindow", "Help"))
        self.label_Image.setText(_translate("MYWINDOW", "<html><head/><body><p align=\"center\"><img src=\"resources\\InterfaceLogo.png\"/></p></body></html>"))

    def setupUi_AdvisorLogin(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_LoginTitle = QtWidgets.QLabel(self.centralwidget)
        self.label_LoginTitle.setGeometry(QtCore.QRect(290, 30, 420, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_LoginTitle.setFont(font)
        self.label_LoginTitle.setMouseTracking(False)
        self.label_LoginTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_LoginTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_LoginTitle.setLineWidth(1)
        self.label_LoginTitle.setMidLineWidth(0)
        self.label_LoginTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LoginTitle.setObjectName("label_LoginTitle")
        self.groupBox_Menu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Menu.setGeometry(QtCore.QRect(310, 150, 380, 211))
        self.groupBox_Menu.setObjectName("groupBox_Menu")
        self.pushButton_ClientManagement = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_ClientManagement.setGeometry(QtCore.QRect(100, 50, 190, 40))
        self.pushButton_ClientManagement.setObjectName("pushButton_ClientManagement")
        self.pushButton_ClientManagement.clicked.connect(openClientManagement)
        self.pushButton_InvestmentManagement = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_InvestmentManagement.setGeometry(QtCore.QRect(100, 120, 190, 40))
        self.pushButton_InvestmentManagement.setObjectName("pushButton_InvestmentManagement")
        self.pushButton_InvestmentManagement.clicked.connect(openInvestmentManagement)
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openLoginPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.label_LoginTitle.setText(_translate("MainWindow", "Welcome to the \n"
"Investment Advisor Client Management Tool"))
        self.groupBox_Menu.setTitle(_translate("MainWindow", "Menu"))
        self.pushButton_ClientManagement.setText(_translate("MainWindow", "Client Management"))
        self.pushButton_InvestmentManagement.setText(_translate("MainWindow", "Investment Management"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_CreateNewAccount(self, MainWindow):

        def clearCreateNewAccount():
            '''
            clearing each of the line edits on the page by setting
            their text to an empty string
            '''
            self.lineEdit_Username.setText("")
            self.lineEdit_Password.setText("")
            self.lineEdit_FirstName.setText("")
            self.lineEdit_LastName.setText("")
            self.lineEdit_PhoneNumber.setText("")
            self.lineEdit_Email.setText("")

        def createCreateNewAccount():
            '''
            taking in the values of the line edits into variables, no need to
            clear the edits afterwards
            checking for empty strings as an invalid input
            validating the inputs
            checking to see if the advisor username is taken
            if conditions are fulfilled, adding the new account to the database
            '''
            username = self.lineEdit_Username.text()
            password = self.lineEdit_Password.text()
            firstName = self.lineEdit_FirstName.text()
            lastName = self.lineEdit_LastName.text()
            phoneNumber = self.lineEdit_PhoneNumber.text()
            email = self.lineEdit_Email.text()
            if "" in {firstName, lastName, phoneNumber, email, username, password}:
                self.label_Error.setText("One or more fields left blank.")
            elif not(validate('firstName', username)):
                self.label_Error.setText("Invalid username.")
            elif not(validate('firstName', firstName)):
                self.label_Error.setText("Invalid first name.")
            elif not(validate('lastName', lastName)):
                self.label_Error.setText("Invalid last name.")
            elif not(validate('phoneNumber', phoneNumber)):
                self.label_Error.setText("Invalid phone number.")
            elif not(validate('email', email)):
                self.label_Error.setText("Invalid email.")
            elif checkUsernameTaken(username) == True:
                self.label_Error.setText("Username is taken.")
            else:
                addAdvisor(firstName, lastName, phoneNumber, email, username, password)
                self.label_Error.setText("User successfully added.")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Details = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Details.setGeometry(QtCore.QRect(310, 60, 380, 391))
        self.groupBox_Details.setObjectName("groupBox_Details")
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(110, 140, 160, 22))
        self.lineEdit_FirstName.setText("")
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.pushButton_Create = QtWidgets.QPushButton(self.groupBox_Details)
        self.pushButton_Create.setGeometry(QtCore.QRect(220, 340, 80, 30))
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.pushButton_Create.clicked.connect(createCreateNewAccount)
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_Details)
        self.pushButton_Clear.setGeometry(QtCore.QRect(90, 340, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Clear.clicked.connect(clearCreateNewAccount)
        self.label_Password = QtWidgets.QLabel(self.groupBox_Details)
        self.label_Password.setGeometry(QtCore.QRect(112, 66, 141, 21))
        self.label_Password.setObjectName("label_Password")
        self.label_FirstName = QtWidgets.QLabel(self.groupBox_Details)
        self.label_FirstName.setGeometry(QtCore.QRect(112, 116, 141, 21))
        self.label_FirstName.setObjectName("label_FirstName")
        self.label_LastName = QtWidgets.QLabel(self.groupBox_Details)
        self.label_LastName.setGeometry(QtCore.QRect(112, 166, 141, 21))
        self.label_LastName.setObjectName("label_LastName")
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(110, 190, 160, 22))
        self.lineEdit_LastName.setText("")
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.lineEdit_PhoneNumber = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_PhoneNumber.setGeometry(QtCore.QRect(110, 240, 160, 22))
        self.lineEdit_PhoneNumber.setText("")
        self.lineEdit_PhoneNumber.setObjectName("lineEdit_PhoneNumber")
        self.label_PhoneNumber = QtWidgets.QLabel(self.groupBox_Details)
        self.label_PhoneNumber.setGeometry(QtCore.QRect(112, 216, 141, 21))
        self.label_PhoneNumber.setObjectName("label_PhoneNumber")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_Email.setGeometry(QtCore.QRect(110, 290, 160, 22))
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.label_Email = QtWidgets.QLabel(self.groupBox_Details)
        self.label_Email.setGeometry(QtCore.QRect(112, 266, 141, 21))
        self.label_Email.setObjectName("label_Email")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_Password.setGeometry(QtCore.QRect(110, 90, 160, 22))
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.label_Username = QtWidgets.QLabel(self.groupBox_Details)
        self.label_Username.setGeometry(QtCore.QRect(112, 16, 141, 21))
        self.label_Username.setObjectName("label_Username")
        self.lineEdit_Username = QtWidgets.QLineEdit(self.groupBox_Details)
        self.lineEdit_Username.setGeometry(QtCore.QRect(110, 40, 160, 22))
        self.lineEdit_Username.setText("")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.label_FillDetails = QtWidgets.QLabel(self.centralwidget)
        self.label_FillDetails.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FillDetails.setFont(font)
        self.label_FillDetails.setObjectName("label_FillDetails")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openLoginPage)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(310, 450, 381, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create Account"))
        self.groupBox_Details.setTitle(_translate("MainWindow", "Details"))
        self.pushButton_Create.setText(_translate("MainWindow", "Create"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.label_Password.setText(_translate("MainWindow", "Password"))
        self.label_FirstName.setText(_translate("MainWindow", "First Name"))
        self.label_LastName.setText(_translate("MainWindow", "Last Name"))
        self.label_PhoneNumber.setText(_translate("MainWindow", "Phone Number"))
        self.label_Email.setText(_translate("MainWindow", "Email Address"))
        self.label_Username.setText(_translate("MainWindow", "Username"))
        self.label_FillDetails.setText(_translate("MainWindow", "Fill in your details to create a new account"))
        self.pushButton_Back.setText(_translate("MainWindow", "Exit"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_HelpPage(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Instructions = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Instructions.setGeometry(QtCore.QRect(50, 60, 901, 360))
        self.groupBox_Instructions.setObjectName("groupBox_Instructions")
        self.label_Text = QtWidgets.QLabel(self.groupBox_Instructions)
        self.label_Text.setGeometry(QtCore.QRect(20, 30, 861, 321))
        self.label_Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Text.setObjectName("label_Text")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openLoginPage)
        self.label_Help = QtWidgets.QLabel(self.centralwidget)
        self.label_Help.setGeometry(QtCore.QRect(20, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Help.setFont(font)
        self.label_Help.setObjectName("label_Help")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help Page"))
        self.groupBox_Instructions.setTitle(_translate("MainWindow", "Instructions for use"))
        self.label_Text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">- A user has access to all the other users\' investment details.</span></p><p><span style=\" font-size:10pt;\">- A user only has access to their own clients\' details.</span></p><p><span style=\" font-size:10pt;\">- New users can be added by creating a new account in the login page.</span></p><p><br/></p><p><span style=\" font-size:10pt;\">- There must be at least one investment to optimize investments.</span></p><p><span style=\" font-size:10pt;\">- Threshold constraint values must be given to use a constraint that uses said threshold.</span></p><p><span style=\" font-size:10pt;\">- All constraints for a client must be given a value to optimize investments.</span></p><p><span style=\" font-size:10pt;\">- Returns values range from 0.01 to 20.00; Maturity values range from 1 to 100; Risk values range from 0.01 to 5.00.</span></p><p><br/></p><p><span style=\" font-size:10pt;\">- Reports are saved with the client\'s full name as default.</span></p><p><span style=\" font-size:10pt;\">- A new report cannot be made whilst the current PDF is still open.<br/></span></p></body></html>"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.label_Help.setText(_translate("MainWindow", "Help"))

    def setupUi_ClientManagement(self, MainWindow):

        def clearClientManagement():
            '''
            clearing each of the line edits on the page by setting
            their text to an empty string
            '''
            self.lineEdit_FirstName.setText("")
            self.lineEdit_LastName.setText("")
            self.lineEdit_PhoneNumber.setText("")
            self.lineEdit_Email.setText("")

        def addClientManagement():
            '''
            taking in the values of the line edits into variables, no need to
            clear the edits afterwards
            checking for empty strings as an invalid input
            validating the inputs
            details can be shared by multiple clients, so there are no checks to
            differentiate clients 
            if conditions are fulfilled, adding the new client to the database
            '''
            firstName = (self.lineEdit_FirstName.text()).capitalize()
            lastName = (self.lineEdit_LastName.text()).capitalize()
            phoneNumber = self.lineEdit_PhoneNumber.text()
            email = self.lineEdit_Email.text()
            if "" in {firstName, lastName, phoneNumber, email}:
                self.label_Error.setText("One or more fields left blank.")
            elif not(validate('firstName', firstName)):
                self.label_Error.setText("Invalid first name.")
            elif not(validate('lastName', lastName)):
                self.label_Error.setText("Invalid last name.")
            elif not(validate('email', email)):
                self.label_Error.setText("Invalid email.")
            elif not(validate('phoneNumber', phoneNumber)):
                self.label_Error.setText("Invalid phone number.")
            else:
                addClient(firstName, lastName, phoneNumber, email, advisorID)
                openClientManagement()
                self.label_Error.setText("Client successfully added.")

        def removeClientManagement():
            '''
            the variable containing the clientID must have global scope as
            to be used by other pages
            storing the contents of the selected client from the list
            splitting and isolating the clientID from within the selected client's
            string
            removing the client from the database and refreshing the page
            if there is no client selected, this will throw up an error that will
            be caught in the try and except, warning the user of this error
            '''
            try:
                global clientID
                currentItem = self.listWidget_Clients.currentRow()
                clientID = list(clientsDict.keys())[currentItem]
                removeClient(clientID)
                openClientManagement()
                self.label_Error.setText("Client successfully removed.")
            except:
                self.label_Error.setText("No client selected.")

        def viewClientManagement():
            '''
            the variable containing the clientID must have global scope as
            to be used by other pages
            storing the contents of the selected client from the list
            splitting and isolating the clientID from within the selected client's
            string
            opening the client investments page that will use the selected client's
            details
            '''
            try:
                global clientID
                currentItem = self.listWidget_Clients.currentRow()
                clientID = list(clientsDict.keys())[currentItem]
                openClientInvestments()
            except:
                self.label_Error.setText("No client selected.")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_ClientList = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ClientList.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_ClientList.setObjectName("groupBox_ClientList")
        self.listWidget_Clients = QtWidgets.QListWidget(self.groupBox_ClientList)
        self.listWidget_Clients.setGeometry(QtCore.QRect(39, 39, 320, 251))
        self.listWidget_Clients.setObjectName("listWidget_Clients")
        self.pushButton_Remove = QtWidgets.QPushButton(self.groupBox_ClientList)
        self.pushButton_Remove.setGeometry(QtCore.QRect(220, 310, 80, 30))
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.pushButton_Remove.clicked.connect(removeClientManagement)
        self.pushButton_View = QtWidgets.QPushButton(self.groupBox_ClientList)
        self.pushButton_View.setGeometry(QtCore.QRect(90, 310, 80, 30))
        self.pushButton_View.setObjectName("pushButton_View")
        self.pushButton_View.clicked.connect(viewClientManagement)
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openAdvisorLogin)
        self.label_ClientManagement = QtWidgets.QLabel(self.centralwidget)
        self.label_ClientManagement.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ClientManagement.setFont(font)
        self.label_ClientManagement.setObjectName("label_ClientManagement")
        self.groupBox_ClientDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ClientDetails.setGeometry(QtCore.QRect(550, 60, 400, 360))
        self.groupBox_ClientDetails.setObjectName("groupBox_ClientDetails")
        self.label_FillClientDetails = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_FillClientDetails.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FillClientDetails.setFont(font)
        self.label_FillClientDetails.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_FillClientDetails.setObjectName("label_FillClientDetails")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_Email.setGeometry(QtCore.QRect(210, 240, 160, 22))
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_PhoneNumber = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_PhoneNumber.setGeometry(QtCore.QRect(210, 200, 160, 22))
        self.lineEdit_PhoneNumber.setText("")
        self.lineEdit_PhoneNumber.setObjectName("lineEdit_PhoneNumber")
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(210, 160, 160, 22))
        self.lineEdit_LastName.setText("")
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.label_PhoneNumber = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_PhoneNumber.setGeometry(QtCore.QRect(30, 200, 141, 21))
        self.label_PhoneNumber.setObjectName("label_PhoneNumber")
        self.label_Title = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_Title.setGeometry(QtCore.QRect(30, 80, 141, 21))
        self.label_Title.setObjectName("label_Title")
        self.label_LastName = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_LastName.setGeometry(QtCore.QRect(30, 160, 141, 21))
        self.label_LastName.setObjectName("label_LastName")
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(210, 120, 160, 22))
        self.lineEdit_FirstName.setText("")
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.label_FirstName = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_FirstName.setGeometry(QtCore.QRect(30, 120, 141, 21))
        self.label_FirstName.setObjectName("label_FirstName")
        self.label_Email = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_Email.setGeometry(QtCore.QRect(30, 240, 141, 21))
        self.label_Email.setObjectName("label_Email")
        self.comboBox_Title = QtWidgets.QComboBox(self.groupBox_ClientDetails)
        self.comboBox_Title.setGeometry(QtCore.QRect(210, 80, 160, 22))
        self.comboBox_Title.setObjectName("comboBox_Title")
        self.comboBox_Title.addItem("")
        self.comboBox_Title.addItem("")
        self.comboBox_Title.addItem("")
        self.comboBox_Title.addItem("")
        self.comboBox_Title.addItem("")
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_ClientDetails)
        self.pushButton_Clear.setGeometry(QtCore.QRect(100, 310, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Clear.clicked.connect(clearClientManagement)
        self.pushButton_Add = QtWidgets.QPushButton(self.groupBox_ClientDetails)
        self.pushButton_Add.setGeometry(QtCore.QRect(230, 310, 80, 30))
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Add.clicked.connect(addClientManagement)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(550, 420, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label_Error")

        '''
        taking the clients from the database and populating the
        list of clients
        '''
        clientsDict = findClients(advisorID)
        clientsList = []
        for client in clientsDict.values():
            clientsList.append(client)
        self.listWidget_Clients.addItems(clientsList)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Management"))
        self.groupBox_ClientList.setTitle(_translate("MainWindow", "Client List"))
        self.pushButton_Remove.setText(_translate("MainWindow", "Remove"))
        self.pushButton_View.setText(_translate("MainWindow", "View"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.label_ClientManagement.setText(_translate("MainWindow", "Client Management"))
        self.groupBox_ClientDetails.setTitle(_translate("MainWindow", "Client Details"))
        self.label_FillClientDetails.setText(_translate("MainWindow", "Fill in the client\'s details to make a new account."))
        self.label_PhoneNumber.setText(_translate("MainWindow", "Phone Number"))
        self.label_Title.setText(_translate("MainWindow", "Title"))
        self.label_LastName.setText(_translate("MainWindow", "Last Name"))
        self.label_FirstName.setText(_translate("MainWindow", "First Name"))
        self.label_Email.setText(_translate("MainWindow", "Email Address"))
        self.comboBox_Title.setItemText(0, _translate("MainWindow", "Mr"))
        self.comboBox_Title.setItemText(1, _translate("MainWindow", "Ms"))
        self.comboBox_Title.setItemText(2, _translate("MainWindow", "Mrs"))
        self.comboBox_Title.setItemText(3, _translate("MainWindow", "Miss"))
        self.comboBox_Title.setItemText(4, _translate("MainWindow", "Mx"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_InvestmentManagement(self, MainWindow):

        def clearInvestmentManagement():
            '''
            clearing each of the line edits on the page by setting
            their text to an empty string
            '''
            self.plainTextEdit_InvestmentName.setPlainText("")
            self.spinBox_Maturity.setValue(0)
            self.doubleSpinBox_Returns.setValue(0.00)
            self.doubleSpinBox_Risk.setValue(0.00)

        def addInvestmentManagement():
            '''
            taking in the values of the line edits into variables, no need to
            clear the edits afterwards
            checking for empty strings as an invalid input
            validating the inputs
            investment name is unique so must be checked against the existing
            names in the database
            if conditions are fulfilled, adding the new investment to the database
            '''
            name = self.plainTextEdit_InvestmentName.toPlainText()
            maturity = self.spinBox_Maturity.value()
            returns = self.doubleSpinBox_Returns.value()
            risk = self.doubleSpinBox_Risk.value()
            if "" in {name, maturity, returns, risk}:
                self.label_Error.setText("One or more fields left blank.")
            elif not(validate('investmentName', name)):
                self.label_Error.setText("Invalid investment name.")
            elif not(validate('maturity', maturity)):
                self.label_Error.setText("Maturity values have to be between 1 and 99.")
            elif not(validate('returns', returns)):
                self.label_Error.setText("Returns values have to be between 0.01 and 20.")
            elif not(validate('risk', risk)):
                self.label_Error.setText("Risk values have to be between 0.01 and 5.")
            else:
                addInvestment(name, maturity, returns, risk)
                openInvestmentManagement()
                self.label_Error.setText("Investment successfully added.")

        def removeInvestmentManagement():
            '''
            the variable containing the investmentID must have global scope as
            to be used by other pages
            storing the contents of the selected investment from the list
            splitting and isolating the investmentID from within the selected
            investment's string
            removing the client from the database and refreshing the page
            if there is no investment selected, this will throw up an error that will
            be caught in the try and except, warning the user of this error
            '''
            try:
                global investmentID
                currentItem = self.listWidget_Investments.currentRow()
                investmentID = list(investmentsDict.keys())[currentItem]
                removeInvestment(investmentID)
                openInvestmentManagement()
                self.label_Error.setText("Investment successfully removed.")
            except:
                self.label_Error.setText("No investment selected.")

        def viewInvestmentManagement():
            '''
            the variable containing the investmentID must have global scope as
            to be used by other pages
            storing the contents of the selected investment from the list
            splitting and isolating the investmentID from within the selected investment's
            string
            opening the view investment page that will use the selected investment's
            details
            '''
            try:
                global investmentID
                currentItem = self.listWidget_Investments.currentRow()
                investmentID = list(investmentsDict.keys())[currentItem]
                openViewInvestment()
            except:
                self.label_Error.setText("No investment selected.")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openAdvisorLogin)
        self.label_InvestmentManagement = QtWidgets.QLabel(self.centralwidget)
        self.label_InvestmentManagement.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_InvestmentManagement.setFont(font)
        self.label_InvestmentManagement.setObjectName("label_InvestmentManagement")
        self.groupBox_InvestmentDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_InvestmentDetails.setGeometry(QtCore.QRect(550, 60, 400, 360))
        self.groupBox_InvestmentDetails.setObjectName("groupBox_InvestmentDetails")
        self.label_FillInvestmentDetails = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_FillInvestmentDetails.setGeometry(QtCore.QRect(40, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FillInvestmentDetails.setFont(font)
        self.label_FillInvestmentDetails.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_FillInvestmentDetails.setObjectName("label_FillInvestmentDetails")
        self.label_Risk = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Risk.setGeometry(QtCore.QRect(30, 230, 141, 21))
        self.label_Risk.setObjectName("label_Risk")
        self.label_InvestmentName = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_InvestmentName.setGeometry(QtCore.QRect(30, 80, 141, 21))
        self.label_InvestmentName.setObjectName("label_InvestmentName")
        self.label_Returns = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Returns.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_Returns.setObjectName("label_Returns")
        self.label_Maturity = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Maturity.setGeometry(QtCore.QRect(30, 150, 141, 21))
        self.label_Maturity.setObjectName("label_Maturity")
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_InvestmentDetails)
        self.pushButton_Clear.setGeometry(QtCore.QRect(100, 310, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Clear.clicked.connect(clearInvestmentManagement)
        self.pushButton_Add = QtWidgets.QPushButton(self.groupBox_InvestmentDetails)
        self.pushButton_Add.setGeometry(QtCore.QRect(230, 310, 80, 30))
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Add.clicked.connect(addInvestmentManagement)
        self.doubleSpinBox_Risk = QtWidgets.QDoubleSpinBox(self.groupBox_InvestmentDetails)
        self.doubleSpinBox_Risk.setGeometry(QtCore.QRect(210, 230, 81, 22))
        self.doubleSpinBox_Risk.setObjectName("doubleSpinBox_Risk")
        self.plainTextEdit_InvestmentName = QtWidgets.QPlainTextEdit(self.groupBox_InvestmentDetails)
        self.plainTextEdit_InvestmentName.setGeometry(QtCore.QRect(210, 80, 161, 51))
        self.plainTextEdit_InvestmentName.setObjectName("plainTextEdit_InvestmentName")
        self.label_Months = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Months.setGeometry(QtCore.QRect(300, 150, 71, 21))
        self.label_Months.setObjectName("label_Months")
        self.label_Percentage = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Percentage.setGeometry(QtCore.QRect(300, 190, 71, 21))
        self.label_Percentage.setObjectName("label_Percentage")
        self.doubleSpinBox_Returns = QtWidgets.QDoubleSpinBox(self.groupBox_InvestmentDetails)
        self.doubleSpinBox_Returns.setGeometry(QtCore.QRect(210, 190, 81, 22))
        self.doubleSpinBox_Returns.setObjectName("doubleSpinBox_Returns")
        self.spinBox_Maturity = QtWidgets.QSpinBox(self.groupBox_InvestmentDetails)
        self.spinBox_Maturity.setGeometry(QtCore.QRect(210, 150, 81, 22))
        self.spinBox_Maturity.setObjectName("spinBox_Maturity")
        self.groupBox_InvestmentsList = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_InvestmentsList.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_InvestmentsList.setObjectName("groupBox_InvestmentsList")
        self.listWidget_Investments = QtWidgets.QListWidget(self.groupBox_InvestmentsList)
        self.listWidget_Investments.setGeometry(QtCore.QRect(39, 39, 320, 251))
        self.listWidget_Investments.setObjectName("listWidget_Investments")
        self.pushButton_Remove = QtWidgets.QPushButton(self.groupBox_InvestmentsList)
        self.pushButton_Remove.setGeometry(QtCore.QRect(220, 310, 80, 30))
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.pushButton_Remove.clicked.connect(removeInvestmentManagement)
        self.pushButton_View = QtWidgets.QPushButton(self.groupBox_InvestmentsList)
        self.pushButton_View.setGeometry(QtCore.QRect(90, 310, 80, 30))
        self.pushButton_View.setObjectName("pushButton_View")
        self.pushButton_View.clicked.connect(viewInvestmentManagement)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(550, 420, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label_Error")

        '''
        taking the investments from the database and populating the
        list of investments
        '''
        investmentsDict = findInvestments()
        investmentsList = []
        for investment in investmentsDict.values():
            investmentsList.append(investment)
        self.listWidget_Investments.addItems(investmentsList)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Investment Management"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.label_InvestmentManagement.setText(_translate("MainWindow", "Investment Management"))
        self.groupBox_InvestmentDetails.setTitle(_translate("MainWindow", "Investment Details"))
        self.label_FillInvestmentDetails.setText(_translate("MainWindow", "Fill in the investment\'s details to add a new\n"
"investment to the database."))
        self.label_Risk.setText(_translate("MainWindow", "Risk Rating"))
        self.label_InvestmentName.setText(_translate("MainWindow", "Investment Name"))
        self.label_Returns.setText(_translate("MainWindow", "Returns"))
        self.label_Maturity.setText(_translate("MainWindow", "Maturity"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.label_Months.setText(_translate("MainWindow", "Months"))
        self.label_Percentage.setText(_translate("MainWindow", "%"))
        self.groupBox_InvestmentsList.setTitle(_translate("MainWindow", "Investment List"))
        self.pushButton_Remove.setText(_translate("MainWindow", "Remove"))
        self.pushButton_View.setText(_translate("MainWindow", "View"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_ConstraintsManagement(self, MainWindow):

        def addConstraintsManagement():
            '''
            the constraint name can be taken from the selected combo box value
            the constraintID can then be taken from the database using the
            constraint name; it can remain within the scope of this subroutine
            as it is only needed for this page
            the value of the constraint is taken from the line edit and is
            passed through validation for every format of constriant
            if the constriant has no value in the database, it is added;
            if the constraint already has a value in the database, it is updated
            erroneous data will cause an error in the valudation function, and so
            the try and except will catch the error and report an invalid input
            '''
            constraintName = self.comboBox_Format.currentText()
            constraintID = findConstraintID(constraintName)
            value = self.lineEdit_Value.text()
            try:
                if value == '':
                    self.label_Error.setText("Value field left blank.")
                elif not(validate(constraintID, float(value))):
                    if constraintID == '1':
                        self.label_Error.setText("Maximum amount invested must be greater than 100.")
                    elif constraintID == '2':
                        self.label_Error.setText("Invalid percentage.")
                    elif constraintID == '3':
                        self.label_Error.setText("Returns values must be between 0.01 and 20.")
                    elif constraintID in ('5', '11'):
                        self.label_Error.setText("Risk values must be between 0.01 and 5")
                    elif constraintID in ('7', '9', '10'):
                        self.label_Error.setText("Maturity values must be between 1 and 100.")
                    elif constraintID in ('4', '6', '8'):
                        self.label_Error.setText("Percentages must be between 0 and 100.")
                else:
                    if findConstraintExists(clientID, constraintID) == False:
                        addConstraint(clientID, constraintID, value)
                        openConstraintsManagement()
                        self.label_Error.setText("Constraint successfully added.")
                    else:
                        updateConstraint(clientID, constraintID, value)
                        openConstraintsManagement()
                        self.label_Error.setText("Constraint successfully updated.")
            except:
                self.label_Error.setText("Invalid input.")
            

        def removeConstraintManagement():
            '''
            the constraint name can be taken from the selected combo box value
            the constraint's value will be removed from the database if a
            constraint has been successfully selected, otherwise, the try and
            except will warn the user of the error
            '''
            try:
                constraintName = (self.listWidget_Constraints.currentItem()).text()
                constraintID = findConstraintID(constraintName)
                removeConstraint(clientID, constraintID)
                openConstraintsManagement()
                self.label_Error.setText("Constraint successfully removed.")
            except:
                self.label_Error.setText("No constraint selected.")

        def showValueConstraintsManagement():
            '''
            the constraint name can be taken from the selected combo box value
            display the current constraint's value in the line edit, ready to
            be updated or given a value
            '''
            constraintName = (self.listWidget_Constraints.currentItem()).text()
            constraintID = findConstraintID(constraintName)
            self.lineEdit_Value.setText(str(findConstraintValue(clientID, constraintID)))
            self.comboBox_Format.setCurrentText(constraintName)

        def clearValueConstraintsManagement():
            ''' clear the value line edit '''
            self.lineEdit_Value.setText("")
            
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_ConstraintsList = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ConstraintsList.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_ConstraintsList.setObjectName("groupBox_ConstraintsList")
        self.listWidget_Constraints = QtWidgets.QListWidget(self.groupBox_ConstraintsList)
        self.listWidget_Constraints.setGeometry(QtCore.QRect(39, 39, 320, 251))
        self.listWidget_Constraints.setObjectName("listWidget_Constraints")
        self.listWidget_Constraints.currentItemChanged.connect(showValueConstraintsManagement)
        self.pushButton_Remove = QtWidgets.QPushButton(self.groupBox_ConstraintsList)
        self.pushButton_Remove.setGeometry(QtCore.QRect(160, 310, 80, 30))
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.pushButton_Remove.clicked.connect(removeConstraintManagement)
        self.label_ConstraintsManagement = QtWidgets.QLabel(self.centralwidget)
        self.label_ConstraintsManagement.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ConstraintsManagement.setFont(font)
        self.label_ConstraintsManagement.setObjectName("label_ConstraintsManagement")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openClientInvestments)
        self.groupBox_ConstraintDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ConstraintDetails.setGeometry(QtCore.QRect(550, 60, 400, 360))
        self.groupBox_ConstraintDetails.setObjectName("groupBox_ConstraintDetails")
        self.label_ChooseFormat = QtWidgets.QLabel(self.groupBox_ConstraintDetails)
        self.label_ChooseFormat.setGeometry(QtCore.QRect(100, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ChooseFormat.setFont(font)
        self.label_ChooseFormat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ChooseFormat.setObjectName("label_ChooseFormat")
        self.label_Value = QtWidgets.QLabel(self.groupBox_ConstraintDetails)
        self.label_Value.setGeometry(QtCore.QRect(100, 200, 31, 21))
        self.label_Value.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Value.setObjectName("label_Value")
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_ConstraintDetails)
        self.pushButton_Clear.setGeometry(QtCore.QRect(100, 310, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_Clear.clicked.connect(clearValueConstraintsManagement)
        self.pushButton_Add = QtWidgets.QPushButton(self.groupBox_ConstraintDetails)
        self.pushButton_Add.setGeometry(QtCore.QRect(230, 310, 80, 30))
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Add.clicked.connect(addConstraintsManagement)
        self.comboBox_Format = QtWidgets.QComboBox(self.groupBox_ConstraintDetails)
        self.comboBox_Format.setGeometry(QtCore.QRect(30, 140, 341, 22))
        self.comboBox_Format.setObjectName("comboBox_Format")
        self.comboBox_Format.addItem("Maximum Amount Invested")
        self.comboBox_Format.addItem("Maximum Percentage Invested Per Investment")
        self.comboBox_Format.addItem("Returns Threshold")
        self.comboBox_Format.addItem("Maximum Percentage Invested In Returns Less Than Threshold")
        self.comboBox_Format.addItem("Risk Threshold")
        self.comboBox_Format.addItem("Maximum Percentage Invested In Risk More Than Threshold")
        self.comboBox_Format.addItem("Maturity Threshold")
        self.comboBox_Format.addItem("Maximum Percentage Invested In Maturity More Than Threshold")
        self.comboBox_Format.addItem("Maximum Maturity")
        self.comboBox_Format.addItem("Maximum Average Maturity")
        self.comboBox_Format.addItem("Maximum Average Risk")
        self.lineEdit_Value = QtWidgets.QLineEdit(self.groupBox_ConstraintDetails)
        self.lineEdit_Value.setGeometry(QtCore.QRect(140, 200, 160, 22))
        self.lineEdit_Value.setText("")
        self.lineEdit_Value.setObjectName("lineEdit_Value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(550, 420, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label_Error")

        '''
        taking the constraints from the database and populating the
        list of constraints
        '''
        constraintsList = findClientConstraints(clientID)
        self.listWidget_Constraints.addItems(constraintsList)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Constraints Management"))
        self.groupBox_ConstraintsList.setTitle(_translate("MainWindow", "Constraints List"))
        self.pushButton_Remove.setText(_translate("MainWindow", "Remove"))
        self.label_ConstraintsManagement.setText(_translate("MainWindow", "Constraints Management"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.groupBox_ConstraintDetails.setTitle(_translate("MainWindow", "Constraint Details"))
        self.label_ChooseFormat.setText(_translate("MainWindow", "Choose a constraint format."))
        self.label_Value.setText(_translate("MainWindow", "Value"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_UpdateDetails(self, MainWindow):

        def clearUpdateDetails():
            '''
            clearing each of the line edits on the page by setting
            their text to an empty string
            '''
            self.lineEdit_Title.setText("")
            self.lineEdit_FirstName.setText("")
            self.lineEdit_LastName.setText("")
            self.lineEdit_PhoneNumber.setText("")
            self.lineEdit_Email.setText("")

        def saveUpdateDetails():
            '''
            taking in the values of the line edits into variables, no need to
            clear the edits afterwards
            checking for empty strings as an invalid input
            validating the inputs
            details can be shared by multiple clients, so there are no checks to
            differentiate clients 
            if conditions are fulfilled, adding the new client to the database
            '''
            firstName = (self.lineEdit_FirstName.text()).capitalize()
            lastName = (self.lineEdit_LastName.text()).capitalize()
            phoneNumber = self.lineEdit_PhoneNumber.text()
            email = self.lineEdit_Email.text()
            if "" in {firstName, lastName, phoneNumber, email}:
                self.label_Error.setText("One or more fields left blank.")
            elif not(validate('firstName', firstName)):
                self.label_Error.setText("Invalid first name")
            elif not(validate('lastName', lastName)):
                self.label_Error.setText("Invalid last name")
            elif not(validate('email', email)):
                self.label_Error.setText("Invalid email")
            elif not(validate('phoneNumber', phoneNumber)):
                self.label_Error.setText("Invalid phone number")
            else:
                updateClient(clientID, firstName, lastName, phoneNumber, email)
                self.label_Error.setText("Details successfully updated.")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_FillDetails = QtWidgets.QLabel(self.centralwidget)
        self.label_FillDetails.setGeometry(QtCore.QRect(20, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FillDetails.setFont(font)
        self.label_FillDetails.setObjectName("label_FillDetails")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(openClientInvestments)
        self.groupBox_ChangeDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ChangeDetails.setGeometry(QtCore.QRect(280, 60, 480, 360))
        self.groupBox_ChangeDetails.setObjectName("groupBox_ChangeDetails")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.groupBox_ChangeDetails)
        self.lineEdit_Email.setGeometry(QtCore.QRect(270, 230, 160, 22))
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.label_FirstName = QtWidgets.QLabel(self.groupBox_ChangeDetails)
        self.label_FirstName.setGeometry(QtCore.QRect(50, 110, 141, 21))
        self.label_FirstName.setObjectName("label_FirstName")
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.groupBox_ChangeDetails)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(270, 150, 160, 22))
        self.lineEdit_LastName.setText("")
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.label_Email = QtWidgets.QLabel(self.groupBox_ChangeDetails)
        self.label_Email.setGeometry(QtCore.QRect(50, 230, 141, 21))
        self.label_Email.setObjectName("label_Email")
        self.lineEdit_PhoneNumber = QtWidgets.QLineEdit(self.groupBox_ChangeDetails)
        self.lineEdit_PhoneNumber.setGeometry(QtCore.QRect(270, 190, 160, 22))
        self.lineEdit_PhoneNumber.setText("")
        self.lineEdit_PhoneNumber.setObjectName("lineEdit_PhoneNumber")
        self.label_Title = QtWidgets.QLabel(self.groupBox_ChangeDetails)
        self.label_Title.setGeometry(QtCore.QRect(50, 70, 141, 21))
        self.label_Title.setObjectName("label_Title")
        self.label_PhoneNumber = QtWidgets.QLabel(self.groupBox_ChangeDetails)
        self.label_PhoneNumber.setGeometry(QtCore.QRect(50, 190, 141, 21))
        self.label_PhoneNumber.setObjectName("label_PhoneNumber")
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.groupBox_ChangeDetails)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(270, 110, 160, 22))
        self.lineEdit_FirstName.setText("")
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.label_LastName = QtWidgets.QLabel(self.groupBox_ChangeDetails)
        self.label_LastName.setGeometry(QtCore.QRect(50, 150, 141, 21))
        self.label_LastName.setObjectName("label_LastName")
        self.pushButton_Save = QtWidgets.QPushButton(self.groupBox_ChangeDetails)
        self.pushButton_Save.setGeometry(QtCore.QRect(270, 300, 80, 30))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Save.clicked.connect(saveUpdateDetails)
        self.pushButton_Clear = QtWidgets.QPushButton(self.groupBox_ChangeDetails)
        self.pushButton_Clear.setGeometry(QtCore.QRect(140, 300, 80, 30))
        self.pushButton_Clear.setObjectName("pushButton_Cancel")
        self.pushButton_Clear.clicked.connect(clearUpdateDetails)
        self.lineEdit_Title = QtWidgets.QLineEdit(self.groupBox_ChangeDetails)
        self.lineEdit_Title.setGeometry(QtCore.QRect(270, 70, 160, 22))
        self.lineEdit_Title.setText("")
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(280, 420, 480, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label_Error")

        '''
        the client's current details are taken from the database
        each of the line edits pertaining to the details
        are filled from the list of details
        '''
        details = displayClient(clientID)
        self.lineEdit_FirstName.setText(details[0])
        self.lineEdit_LastName.setText(details[1])
        self.lineEdit_PhoneNumber.setText(details[2])
        self.lineEdit_Email.setText(details[3])

        titles = ['Mr', 'Mrs', 'Miss', 'Ms', 'Mx']
        self.lineEdit_Title.setText(titles[randint(0,4)])

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Details"))
        self.label_FillDetails.setText(_translate("MainWindow", "Update Personal Details"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.groupBox_ChangeDetails.setTitle(_translate("MainWindow", "Change Details"))
        self.label_FirstName.setText(_translate("MainWindow", "First Name"))
        self.label_Email.setText(_translate("MainWindow", "Email Address"))
        self.label_Title.setText(_translate("MainWindow", "Title"))
        self.label_PhoneNumber.setText(_translate("MainWindow", "Phone Number"))
        self.label_LastName.setText(_translate("MainWindow", "Last Name"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_ClientInvestments(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_ClientDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ClientDetails.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_ClientDetails.setObjectName("groupBox_ClientDetails")
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(180, 110, 190, 22))
        self.lineEdit_FirstName.setText("")
        self.lineEdit_FirstName.setReadOnly(True)
        self.lineEdit_FirstName.setPlaceholderText("")
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.label_PhoneNumber = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_PhoneNumber.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_PhoneNumber.setObjectName("label_PhoneNumber")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_Email.setGeometry(QtCore.QRect(180, 230, 190, 22))
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setReadOnly(True)
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_PhoneNumber = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_PhoneNumber.setGeometry(QtCore.QRect(180, 190, 190, 22))
        self.lineEdit_PhoneNumber.setText("")
        self.lineEdit_PhoneNumber.setReadOnly(True)
        self.lineEdit_PhoneNumber.setObjectName("lineEdit_PhoneNumber")
        self.label_FirstName = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_FirstName.setGeometry(QtCore.QRect(30, 110, 141, 21))
        self.label_FirstName.setObjectName("label_FirstName")
        self.label_LastName = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_LastName.setGeometry(QtCore.QRect(30, 150, 141, 21))
        self.label_LastName.setObjectName("label_LastName")
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.groupBox_ClientDetails)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(180, 150, 190, 22))
        self.lineEdit_LastName.setText("")
        self.lineEdit_LastName.setReadOnly(True)
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.label_Email = QtWidgets.QLabel(self.groupBox_ClientDetails)
        self.label_Email.setGeometry(QtCore.QRect(30, 230, 141, 21))
        self.label_Email.setObjectName("label_Email")
        self.label_ClientInvestments = QtWidgets.QLabel(self.centralwidget)
        self.label_ClientInvestments.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ClientInvestments.setFont(font)
        self.label_ClientInvestments.setObjectName("label_ClientInvestments")
        self.groupBox_Menu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Menu.setGeometry(QtCore.QRect(550, 60, 400, 360))
        self.groupBox_Menu.setObjectName("groupBox_Menu")
        self.pushButton_FormulateInvestments = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_FormulateInvestments.setGeometry(QtCore.QRect(110, 230, 190, 40))
        self.pushButton_FormulateInvestments.setObjectName("pushButton_FormulateInvestments")
        self.pushButton_FormulateInvestments.clicked.connect(openInvestmentOptimization)
        self.pushButton_SetConstraints = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_SetConstraints.setGeometry(QtCore.QRect(110, 160, 190, 40))
        self.pushButton_SetConstraints.setObjectName("pushButton_SetConstraints")
        self.pushButton_SetConstraints.clicked.connect(openConstraintsManagement)
        self.pushButton_UpdateDetails = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_UpdateDetails.setGeometry(QtCore.QRect(110, 90, 190, 40))
        self.pushButton_UpdateDetails.setObjectName("pushButton_FormulateInvestments_2")
        self.pushButton_UpdateDetails.clicked.connect(openUpdateDetails)
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openClientManagement)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        '''
        the selected client's details are taken from the database
        each of the read only line edits pertaining to the details
        are filled from the list of details
        '''
        details = displayClient(clientID)
        self.lineEdit_FirstName.setText(details[0])
        self.lineEdit_LastName.setText(details[1])
        self.lineEdit_PhoneNumber.setText(details[2])
        self.lineEdit_Email.setText(details[3])

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client Investments"))
        self.groupBox_ClientDetails.setTitle(_translate("MainWindow", "Client Details"))
        self.label_PhoneNumber.setText(_translate("MainWindow", "Phone Number"))
        self.label_FirstName.setText(_translate("MainWindow", "First Name"))
        self.label_LastName.setText(_translate("MainWindow", "Last Name"))
        self.label_Email.setText(_translate("MainWindow", "Email Address"))
        self.label_ClientInvestments.setText(_translate("MainWindow", "Client Investments"))
        self.groupBox_Menu.setTitle(_translate("MainWindow", "Menu"))
        self.pushButton_FormulateInvestments.setText(_translate("MainWindow", "Formulate Investments"))
        self.pushButton_SetConstraints.setText(_translate("MainWindow", "Set Constraints"))
        self.pushButton_UpdateDetails.setText(_translate("MainWindow", "Update Details"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_ViewInvestment(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_InvestmentDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_InvestmentDetails.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_InvestmentDetails.setObjectName("groupBox_InvestmentDetails")
        self.label_Risk = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Risk.setGeometry(QtCore.QRect(30, 245, 141, 21))
        self.label_Risk.setObjectName("label_Risk")
        self.label_InvestmentName = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_InvestmentName.setGeometry(QtCore.QRect(30, 95, 141, 21))
        self.label_InvestmentName.setObjectName("label_InvestmentName")
        self.label_Returns = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Returns.setGeometry(QtCore.QRect(30, 205, 141, 21))
        self.label_Returns.setObjectName("label_Returns")
        self.label_Maturity = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Maturity.setGeometry(QtCore.QRect(30, 165, 141, 21))
        self.label_Maturity.setObjectName("label_Maturity")
        self.plainTextEdit_InvestmentName = QtWidgets.QPlainTextEdit(self.groupBox_InvestmentDetails)
        self.plainTextEdit_InvestmentName.setGeometry(QtCore.QRect(180, 95, 190, 51))
        self.plainTextEdit_InvestmentName.setReadOnly(True)
        self.plainTextEdit_InvestmentName.setObjectName("plainTextEdit_InvestmentName")
        self.label_Months = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Months.setGeometry(QtCore.QRect(300, 165, 71, 21))
        self.label_Months.setObjectName("label_Months")
        self.label_Percentage = QtWidgets.QLabel(self.groupBox_InvestmentDetails)
        self.label_Percentage.setGeometry(QtCore.QRect(300, 205, 71, 21))
        self.label_Percentage.setObjectName("label_Percentage")
        self.lineEdit_Maturity = QtWidgets.QLineEdit(self.groupBox_InvestmentDetails)
        self.lineEdit_Maturity.setGeometry(QtCore.QRect(180, 165, 110, 22))
        self.lineEdit_Maturity.setText("")
        self.lineEdit_Maturity.setReadOnly(True)
        self.lineEdit_Maturity.setObjectName("lineEdit_Maturity")
        self.lineEdit_Returns = QtWidgets.QLineEdit(self.groupBox_InvestmentDetails)
        self.lineEdit_Returns.setGeometry(QtCore.QRect(180, 205, 110, 22))
        self.lineEdit_Returns.setText("")
        self.lineEdit_Returns.setReadOnly(True)
        self.lineEdit_Returns.setObjectName("lineEdit_Returns")
        self.lineEdit_Risk = QtWidgets.QLineEdit(self.groupBox_InvestmentDetails)
        self.lineEdit_Risk.setGeometry(QtCore.QRect(180, 245, 110, 22))
        self.lineEdit_Risk.setText("")
        self.lineEdit_Risk.setReadOnly(True)
        self.lineEdit_Risk.setObjectName("lineEdit_Risk")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openInvestmentManagement)
        self.label_ViewInvestment = QtWidgets.QLabel(self.centralwidget)
        self.label_ViewInvestment.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ViewInvestment.setFont(font)
        self.label_ViewInvestment.setObjectName("label_ViewInvestment")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        '''
        the selected investment's details are taken from the database
        each of the read only line edits pertaining to the details
        are filled from the list of details
        '''
        details = displayInvestment(investmentID)
        self.plainTextEdit_InvestmentName.setPlainText(details[0])
        self.lineEdit_Maturity.setText(str(details[1]))
        self.lineEdit_Returns.setText(str(details[2]))
        self.lineEdit_Risk.setText(str(details[3]))

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Investment"))
        self.groupBox_InvestmentDetails.setTitle(_translate("MainWindow", "Investment Details"))
        self.label_Risk.setText(_translate("MainWindow", "Risk Rating"))
        self.label_InvestmentName.setText(_translate("MainWindow", "Investment Name"))
        self.label_Returns.setText(_translate("MainWindow", "Returns"))
        self.label_Maturity.setText(_translate("MainWindow", "Maturity"))
        self.label_Months.setText(_translate("MainWindow", "Months"))
        self.label_Percentage.setText(_translate("MainWindow", "%"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.label_ViewInvestment.setText(_translate("MainWindow", "View Investment"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUi_InvestmentOptimization(self, MainWindow):

        def clearInvestmentOptimization():
            '''
            clear the investments
            reopen the page to refresh the table
            '''
            clearInvestments(clientID)
            openInvestmentOptimization()
            
        def optimizeInvestmentOptimization():
            '''
            first the constraints must be checked to ensure that there are enough to start
            the simplex method, this validates that there is a threhold for every variable
            and succeeding that, there are sufficient constraints in the first place
            '''
            if len(packInvestments()) == 0:
                self.label_Error.setText("No investments provided.")
            elif checkPairs(clientID) == False:
                self.label_Error.setText("Threshold constraint is missing.")
            elif countConstraints(clientID) < 7:
                self.label_Error.setText("Insufficient constraints provided.")
            else:
                '''
                the investments and constraints must be taken from the database for the
                algorithm
                '''
                raw_investments = packInvestments()
                raw_constraints = packConstraints(clientID)
                objective = []
                iterationNum = 0

                '''
                investments are filtered out of the available pool if they have a maturtiy
                greater than the maximum maturity constraint
                the objective row must be formed separately, each return value is expressed
                as a decimal and then converted to a muliple of the amount invested; this
                is then made negative to fit the format used in the objective row of the
                initial tableau
                '''
                for index in range(1, (len(raw_investments) + 1)):
                    if raw_investments[len(raw_investments) - index][1] > raw_constraints[8][1]:                
                        del raw_investments[len(raw_investments) - index]

                for row in raw_investments:
                    objective.append(1 + (0.01 * row[2]))

                '''
                the simplex tableau is made, then the optimisation method is run until
                the tableau is optimum or the number of iterations has exceeded 1000
                the results of the simplex are then taken into a dictionary with an
                investment name key and the amount value
                '''
                simplexTableau = createTableau(raw_investments, raw_constraints, objective)
                while True:
                    if checkOptimum(simplexTableau) or (iterationNum == 1000):
                        break
                    simplexTableau = optimiseTableau(simplexTableau)
                    iterationNum += 1
                simplexResults = findOptimum(simplexTableau, raw_investments)
                
                ''' the investments have to been cleared before the new ones can be added '''
                clearInvestments(clientID)

                '''
                iterating through the results of the simplex tableau and finding the details
                of each investment with a value to add to the database
                refreshing the page to show new investments in the interface's table
                warning to the interface if the simplex method did not find an optimum
                solution within the itertation limit
                returning the important values from the simplex method to be used in
                creating the pdf
                '''
                for investment in findClientInvestments(simplexResults):
                    investmentRow = findInvestmentFromName(investment[0])
                    predictedFinal = (1 + (0.01 * investmentRow[2])) * investment[1]
                    storeInvestment(clientID, investmentRow[0], investment[1], investmentRow[1], predictedFinal)

                openInvestmentOptimization()
                
                if iterationNum == 1000:
                    self.label_Error.setText("Solution may not be optimum.")
                
                return findProfit(simplexResults, simplexTableau, raw_constraints, raw_investments)

        def pdfInvestmentOptimization():
            '''
            this runs the optimize function to ensure that the optimum investments are available;
            the total, profit and remaining values are assigned to variables in this function
            this then takes the packaged investment and client data from the database, to be sent
            to the pdf
            the imported subroutines for creating the graph and new pdf are then ran; the pdf
            function returns False if it cannot create a new pdf, so this must be displayed on
            the interface to warn the user to close the current pdf so the new one can be made
            '''
            clientDetails = displayClient(clientID)
            investmentDetails = tableData(clientID)
            path = QtWidgets.QFileDialog.getSaveFileName(filter = ("(*.pdf)"), caption = 'Save Report', directory = (clientDetails[0] + ' ' + clientDetails[1]))
            if path[0] != '':
                total, profit, remaining = optimizeInvestmentOptimization()
                createGraph(investmentDetails, profit)
                if not(createPdf(path[0], clientDetails, investmentDetails, total, profit, remaining)):
                    self.label_Error.setText("PDF already open.")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_InvestmentOptimization = QtWidgets.QLabel(self.centralwidget)
        self.label_InvestmentOptimization.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_InvestmentOptimization.setFont(font)
        self.label_InvestmentOptimization.setObjectName("label_InvestmentOptimization")
        self.groupBox_OptimumInvestments = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_OptimumInvestments.setGeometry(QtCore.QRect(50, 60, 400, 360))
        self.groupBox_OptimumInvestments.setObjectName("groupBox_OptimumInvestments")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_OptimumInvestments)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 320, 290))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setVerticalHeaderLabels(['Investment Name', 'Amount Invested', 'Time Remaining', 'Predicted Final Amount'])
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(20, 450, 80, 30))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.pushButton_Back.clicked.connect(openClientInvestments)
        self.groupBox_Menu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Menu.setGeometry(QtCore.QRect(550, 60, 400, 360))
        self.groupBox_Menu.setObjectName("groupBox_Menu")
        self.pushButton_CreatePDF = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_CreatePDF.setGeometry(QtCore.QRect(110, 230, 190, 40))
        self.pushButton_CreatePDF.setObjectName("pushButton_CreatePDF")
        self.pushButton_CreatePDF.clicked.connect(pdfInvestmentOptimization)
        self.pushButton_Optimize = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_Optimize.setGeometry(QtCore.QRect(110, 160, 190, 40))
        self.pushButton_Optimize.setObjectName("pushButton_Optimize")
        self.pushButton_Optimize.clicked.connect(optimizeInvestmentOptimization)
        self.pushButton_ClearInvestments = QtWidgets.QPushButton(self.groupBox_Menu)
        self.pushButton_ClearInvestments.setGeometry(QtCore.QRect(110, 90, 190, 40))
        self.pushButton_ClearInvestments.setObjectName("pushButton_ClearInvestments")
        self.pushButton_ClearInvestments.clicked.connect(clearInvestmentOptimization)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_Error = QtWidgets.QLabel(self.centralwidget)
        self.label_Error.setGeometry(QtCore.QRect(550, 420, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Error.setFont(font)
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Error.setObjectName("label_Error")

        '''
        the data formatted to be used in the table is taken from the database
        the table widget is then created with only headers
        rows from the table data are then added based on the row number which is
        incremented
        items populate the row from the data
        '''
        rowNumber = 0
        tableInvestments = tableData(clientID)

        for record in tableInvestments:
            self.tableWidget.insertRow(rowNumber)
            columnNumber = 0

            for item in record:
                self.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(item)))
                columnNumber += 1
            rowNumber += 1

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Investment Optimization"))
        self.label_InvestmentOptimization.setText(_translate("MainWindow", "Investment Optimization"))
        self.groupBox_OptimumInvestments.setTitle(_translate("MainWindow", "Optimum Investments"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Investment Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount Invested"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time Remaining"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Predicted Final Amount"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.groupBox_Menu.setTitle(_translate("MainWindow", "Menu"))
        self.pushButton_CreatePDF.setText(_translate("MainWindow", "Create PDF"))
        self.pushButton_Optimize.setText(_translate("MainWindow", "Optimize For Client"))
        self.pushButton_ClearInvestments.setText(_translate("MainWindow", "Clear Investments"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

def validate(validateType, validateData):
    '''
    the validate function uses the input case as its 'validateType' to identify which
    method of validation to use, and the 'validateData' as the input itself

    validations for string inputs use regular expressions to ensure the string is in
    the correct format and contains a valid data type
    other float or integer based inputs use ranges to specify the acceptable values of that
    input
    certain constraints use the same validation such as ensuring a valid percentage or
    ensuring a valid risk value each have multiple constraints assigned to the same method
    '''
    if validateType == 'firstName':
        return re.match(r'(^[a-zA-Z]+$)', validateData)
    elif validateType == 'lastName':
        return re.match(r'(^[a-zA-Z]+$)', validateData)
    elif validateType == 'email':
        return re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', validateData)
    elif validateType == 'phoneNumber':
        return re.match(r'(^(07\d{8,12}|447\d{7,11})$)', validateData)
    elif validateType == 'investmentName':
        if checkInvestmentExists(validateData):
            return False
        return re.match(r'(^[a-zA-Z0-9._ ]*$)', validateData)
    elif validateType in ('maturity', '7', '9', '10'):
        if 0 < validateData < 100:
            return True
        return False
    elif validateType in ('returns', '3'):
        if 0 < validateData < 20:
            return True
        return False
    elif validateType in ('risk', '5', '11'):
        if 0 < validateData < 5:
            return True
        return False
    elif validateType == '1':
        if validateData < 100:
            return False
        return True
    elif validateType == '2':
        raw_constraints = packConstraints(clientID)
        raw_investments = packInvestments()
        base = 100 / len(raw_investments)
        if base <= validateData <= 100:
            return True
        return False
    elif validateType in ('4', '6', '8'):
        if 0 <= validateData <= 100:
            return True
        return False
    

def openLoginPage():
    QtWidgets.qApp.quit
    ui.setupUi_LoginPage(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openAdvisorLogin():
    QtWidgets.qApp.quit
    ui.setupUi_AdvisorLogin(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openCreateNewAccount():
    QtWidgets.qApp.quit
    ui.setupUi_CreateNewAccount(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openHelpPage():
    QtWidgets.qApp.quit
    ui.setupUi_HelpPage(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openClientManagement():
    QtWidgets.qApp.quit
    ui.setupUi_ClientManagement(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openInvestmentManagement():
    QtWidgets.qApp.quit
    ui.setupUi_InvestmentManagement(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openConstraintsManagement():
    QtWidgets.qApp.quit
    ui.setupUi_ConstraintsManagement(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openUpdateDetails():
    QtWidgets.qApp.quit
    ui.setupUi_UpdateDetails(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openClientInvestments():
    QtWidgets.qApp.quit
    ui.setupUi_ClientInvestments(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openViewInvestment():
    QtWidgets.qApp.quit
    ui.setupUi_ViewInvestment(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

def openInvestmentOptimization():
    QtWidgets.qApp.quit
    ui.setupUi_InvestmentOptimization(MYWINDOW)
    MYWINDOW.show()
    app.exec_()


if __name__ == "__main__":
    import sys
    import time
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("resources\\icon.png")))
    MYWINDOW = QtWidgets.QMainWindow()
    ui = Ui_MYWINDOW()
    ui.setupUi_LoginPage(MYWINDOW)
    MYWINDOW.show()
    app.exec_()

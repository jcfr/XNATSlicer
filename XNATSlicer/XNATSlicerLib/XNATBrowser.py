## SLICER INCLUDES
#from __main__ import vtk, qt, ctk, slicer
#import os
#import glob 
#import sys 
#import inspect
## GLOBALS
#WIDGETPATH = os.path.normpath(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe()))[0])))
#sys.path.append(WIDGETPATH)
## MODULE INCLUDES
#from XNATFileInfo import *
#from XNATLoadWorkflow import *
#from XNATMRMLParser import *
#from XNATUtils import *
#from XNATInstallWizard import *
#from XNATScenePackager import *
#from XNATSessionManager import *
#from XNATTimer import *
#from XNATSettings import *
#from XNATTreeView import *
#from XNATCommunicator import *
#import XNATView
#
##===============================================================================
## XNATBrowser is the hook script/class that communicates with Slicer.  
## All processes related to XNATSlicer begin here.
## Layout information, browser type (in this case, the XNATTreeView), etc.  
##===============================================================================
#
#class XNATBrowser:
#    """ Initiates module intro data to slicer.  
#    """
#    def __init__(self, parent):
#        parent.title = "XNATSlicer"
#        parent.categories = ["XNAT"]
#        parent.contributors = ["Sunil Kumar"]
#        parent.helpText = """
#        The XNATSlicer Browser 1.0
#        """
#        parent.acknowledgementText = """
#        Sunil Kumar - NRG - kumars@mir.wustl.edu
#        """
#        self.parent = parent
#
#class XNATBrowserWidget:
#    def __init__(self, parent=None):
#        if not parent:
#            self.parent = slicer.qMRMLWidget()
#            self.parent.setLayout(qt.QVBoxLayout())
#            self.parent.setMRMLScene(slicer.mrmlScene)
#        else:
#            self.parent = parent
#        
#        self.utils = XNATUtils()    
#        self.layout = self.parent.layout()
#        #===========================================================================
#        # XNAT SETTINGS
#        #===========================================================================
#        self.settings = XNATSettings(slicer.qMRMLWidget(), self.utils.utilPath, self)
#        #===========================================================================
#        # STATUS BAR
#        #===========================================================================
#        self.labelStatusBar = labelStatusBar(self, 3)
#        #===========================================================================
#        # VIEWER - TREE VIEW
#        #===========================================================================
#        self.XNATView = XNATTreeView(self.parent, 
#                                     self.settings, self)    
#        #===========================================================================
#        # USERNAME AND PASSWORD LINES  
#        #===========================================================================
#        self.usernameLabel = qt.QLabel('username:')
#        self.usernameLabel.setFont(self.utils.labelFontBold)
#        self.passwordLabel = qt.QLabel('password:')
#        self.passwordLabel.setFont(self.utils.labelFontBold)    
#        self.usernameLine = qt.QLineEdit()   
#        self.passwordLine = qt.QLineEdit() # encrypted
#        self.usernameLine.setFixedWidth(100)
#        self.passwordLine.setFixedWidth(100)
#        #=======================================================================
#        # PROGRESS BAR
#        #=======================================================================
#        self.generalProgressBar = qt.QProgressBar()
#        #===========================================================================
#        # LOGIN BUTTON
#        #===========================================================================
#        self.loginButton = None
#        #===========================================================================
#        # HOST DROPDOWN
#        #===========================================================================
#        self.hostLabel = qt.QLabel('host:')
#        self.hostLabel.setFont(self.utils.labelFontBold)
#        self.hostDropdown = None
#        self.hostLoggedIn = False
#        #===========================================================================
#        # GLOBALS
#        #===========================================================================
#        self.currHostUrl = None
#        self.currHostName = None
#        self.currHostAddress = None
#        self.XNATHosts = None
#        #===========================================================================
#        # SETTINGS BUTTON
#        #===========================================================================
#        self.settingsButton = None  
#        self.networkRequest = None
#        #===========================================================================
#        # POPUPS
#        #===========================================================================
#        self.statusPopup = None
#        self.progressPopup = None
#        #===========================================================================
#        # LAYOUTS
#        #===========================================================================
#        self.browserLayout = None
#        self.loginLayout = None
#        self.statusLayout = None #qt.QGridLayout()
#        self.XNATViewLayout = qt.QGridLayout()
#        #===========================================================================
#        # INIT GUI
#        #===========================================================================
#        self.initGUI()
#        #===========================================================================
#        # LISTENERS/OBSERVERS FROM GUI INTERACTION
#        #===========================================================================
#        slicer.mrmlScene.AddObserver(slicer.mrmlScene.EndCloseEvent, self.sceneClosedListener)
#        slicer.mrmlScene.AddObserver(slicer.mrmlScene.EndImportEvent, self.sceneImportedListener)
#        self.parent.show()
#        
#    def sceneClosedListener(self, caller, event):
#        """Actions for when the user closes a scene from the GUI.
#        """ 
#        print("'Close Scene' called. Resetting XNAT session data.")    
#        self.XNATView.sessionManager.clearCurrentSession()  
#    
#    def sceneImportedListener(self, caller, event): 
#        """Actions for when the user imports a scene from the GUI.
#           NOTE: This technically is not used, as the user must refer to files from an 
#           XNAT location. Nonetheless, it is implemented in the event that it is needed.
#        """
#        if self.XNATView.lastButtonClicked == None:
#            print("'Import Data' called. Resetting XNAT session data.")
#            self.XNATView.sessionManager.clearCurrentSession() 
#
#          
#    def initGUI(self):  
#        #===========================================================================
#        # Login Section
#        #===========================================================================
#        loginCollapsibleButton = ctk.ctkCollapsibleButton()
#        loginCollapsibleButton.text = "XNAT Login"
#        #===========================================================================
#        # Browser Section
#        #===========================================================================
#        browserCollapsibleButton = ctk.ctkCollapsibleButton()
#        browserCollapsibleButton.text = "XNAT TreeView"
#        #===========================================================================
#        # Status Section
#        #===========================================================================
#        statusCollapsibleButton = ctk.ctkCollapsibleButton()
#        statusCollapsibleButton.text = "Status"
#        #===========================================================================
#        # Add all sections to parent layout.
#        #===========================================================================
#        self.layout.addWidget(loginCollapsibleButton)
#        self.layout.addWidget(statusCollapsibleButton)
#        self.layout.addWidget(browserCollapsibleButton)
#        #===========================================================================
#        # Define section layouts.
#        #===========================================================================
#        self.loginLayout = qt.QVBoxLayout(loginCollapsibleButton)
#        self.browserLayout = qt.QVBoxLayout(browserCollapsibleButton)
#        self.statusLayout = qt.QVBoxLayout(statusCollapsibleButton)    
#        #===========================================================================
#        # Host Dropdown
#        #===========================================================================
#        self.initHostDropdown()       
#        #===========================================================================
#        # Manage Hosts Button
#        #===========================================================================
#        self.initSettingsButton()
#        #===========================================================================
#        # Login Lines
#        #===========================================================================
#        self.initLoginLines()
#        #===========================================================================
#        # Login Button
#        #===========================================================================
#        self.initLoginButton()
#        #===========================================================================
#        # XNAT Window
#        #===========================================================================
#        self.viewerLayout = qt.QVBoxLayout()
#        self.cleanTempDir(500)
#        #===========================================================================
#        # Username/Password Row
#        #===========================================================================
#        credentialsRow = qt.QHBoxLayout()
#        credentialsRow.addWidget(self.settingsButton)
#        credentialsRow.addWidget(self.hostDropdown)
#        credentialsRow.addSpacing(20)
#        credentialsRow.addWidget(self.usernameLine)
#        credentialsRow.addWidget(self.passwordLine)
#        credentialsRow.addWidget(self.loginButton)
#        #===========================================================================
#        # Everything related to logging in
#        #===========================================================================
#        fullLoginLayout = qt.QGridLayout() 
#        #fullLoginLayout.addLayout(hostRow, 0,0)
#        #fullLoginLayout.addWidget(spaceLabel, 0,1)
#        fullLoginLayout.addLayout(credentialsRow, 0,2)
#        #===========================================================================
#        # Load/Save button
#        #===========================================================================
#        self.buttonColumnLayout = qt.QVBoxLayout()
#        self.buttonColumnLayout.addWidget(self.XNATView.loadButton)#, 2, 0)
#        self.buttonColumnLayout.addWidget(self.XNATView.saveButton)#, 0, 0) 
#
#        self.buttonRowLayout = qt.QHBoxLayout()
#        self.buttonRowLayout.addWidget(self.XNATView.deleteButton)
#        self.buttonRowLayout.addSpacing(15)
#        self.buttonRowLayout.addWidget(self.XNATView.addProjButton)
#        self.buttonRowLayout.addStretch()
#        #===========================================================================
#        # XNATViewer
#        #===========================================================================
#        self.XNATViewLayout.addWidget(self.XNATView.viewWidget, 0, 0)
#        self.XNATViewLayout.addLayout(self.buttonColumnLayout, 0, 1)
#        self.XNATViewLayout.addLayout(self.buttonRowLayout, 1, 0)
#        self.XNATView.statusView.textField.setFixedHeight(25)
#        #===========================================================================
#        # Apply to globals
#        #===========================================================================
#        self.loginLayout.addLayout(fullLoginLayout)
#        self.browserLayout.addLayout(self.XNATViewLayout)
#        self.statusLayout.addLayout(self.labelStatusBar.layout)
#           
#        self.generalProgressBar.setVisible(False)
#        self.generalProgressBar.setFixedHeight(17)
#        
#        self.statusLayout.addWidget(self.generalProgressBar)
#
#    def initLoginLines(self):
#        """ Password and login lines
#        """
#        #=======================================================================
#        # DESCRIPTIONS
#        #=======================================================================
#        self.defaultPasswordText = "Password"
#        self.defaultUsernameText = "Login"
#        #=======================================================================
#        # ASTHETICS  
#        #=======================================================================
#        self.usernameLine.setText(self.defaultUsernameText)
#        self.usernameLine.setFont(self.utils.labelFontItalic)
#        self.passwordLine.setFont(self.utils.labelFontItalic) 
#        self.passwordLine.setText(self.defaultPasswordText)
#        self.passwordLine.selectAll()
#        #=======================================================================
#        # SIGNALS
#        #=======================================================================
#        self.usernameLine.connect('cursorPositionChanged(int, int)', 
#                                  self.usernameLineEdited)  
#        self.passwordLine.connect('cursorPositionChanged(int, int)', 
#                                  self.passwordLineEdited)
#        self.passwordLine.connect('returnPressed()', 
#                                  self.simulateLoginClicked) 
#        
#        self.populateCurrUser()
#        
#    def initHostDropdown(self):
#        """ Initiates the dropdown that allows the user to select hosts
#        """
#        self.hostDropdown = qt.QComboBox()
#        self.hostDropdown.setFont(self.utils.labelFont)
#        self.hostDropdown.toolTip = "Select XNAT host"
#        self.currHostUrl = qt.QUrl(self.hostDropdown.currentText)
#        self.addHosts()
#        self.hostDropdown.connect('currentIndexChanged(const QString&)',
#                                  self.hostDropdownClicked) 
#        
#    def initSettingsButton(self):
#        """ Initiates the button aesthetics for the button that opens the manage 
#        hosts popup 
#        """
#        self.settingsButton = qt.QPushButton()
#        self.settingsButton.setIcon(qt.QIcon(os.path.join(self.utils.iconPath, 
#                                                          'wrench.png')) )
#        self.settingsButton.toolTip = "Settings"
#        self.settingsButton.setFixedSize(self.utils.buttonSizeMed.width() - 10, 26)
#        #self.settingsButton.setFixedSize(self.utils.buttonSize)
#        self.settingsButton.connect('pressed()', self.settingsButtonClicked)
#
#    def initLoginButton(self):
#        """ Connects the login to the first treeView call
#        """
#        plt = qt.QPalette()
#        plt.setColor(qt.QPalette().Button, qt.QColor(255,255,255))    
#        self.loginButton = qt.QPushButton("Login")
#        
#        self.loginButton.setFont(self.utils.labelFontBold)    
#        self.loginButton.toolTip = "Login to selected XNAT host"    
#        self.loginButton.connect('clicked()', self.loginButtonClicked)
#        self.loginButton.setFixedSize(self.utils.buttonSizeMed.width(), self.utils.buttonSizeSmall.height() - 4) 
#            
#    def updateStatus(self, strings):
#        """Updates the status bar with the given strings.
#        """
#        if not self.XNATView.viewWidget.isEnabled():
#            self.XNATView.viewWidget.setEnabled(True)
#        self.labelStatusBar.showMessage(strings)
#        self.statusLayout.update()
#        
#    def updateStatus_Locked(self, strings):
#        """Updates the status bar by locking the viewer widget.
#        """
#        self.XNATView.viewWidget.setEnabled(False)
#        self.labelStatusBar.showMessage(strings)
#      
#    def cleanTempDir(self, maxSize):
#        """ Empties contents of the temp directory based upon maxSize
#        """
#        import math
#        folder = self.utils.tempPath
#        folder_size = 0
#        #=======================================================================
#        # Loop through files to get file paths.
#        #=======================================================================
#        for (path, dirs, files) in os.walk(folder):
#          for file in files:
#            folder_size += os.path.getsize(os.path.join(path, file))
#        print ("XNATSlicer Data Folder = %0.1f MB" % (folder_size/(1024*1024.0)))
#        folder_size = math.ceil(folder_size/(1024*1024.0))
#        if folder_size > maxSize:
#            self.utils.removeFilesInDir(self.utils.tempPath)    
#            self.utils.removeFilesInDir(self.utils.tempUploadPath)   
#    
#    def addHosts(self):
#        """ Adds and stores the entered host
#        """
#        self.hostDropdown.clear()
#        hostDict = self.settings.hostNameAddressDictionary()
#        for name in hostDict:     
#            self.hostDropdown.addItem(name)
#        #=======================================================================
#        # LOOP THROUGH TO FIND DEFAULT HOST
#        #=======================================================================
#        if not self.currHostName:
#            for i in range(0, len(hostDict.keys())):    
#                if int(self.settings.isDefault(hostDict.keys()[i]))>0:
#                    self.hostDropdown.setCurrentIndex(i)
#                    self.currHostName = hostDict.keys()[i]
#                    break
#            
#    def beginXNAT(self, XNATCommunicatorType, viewType):
#        """ Opens the view class linked to the XNATRestAPI
#        """
#        XNATCommunicator = None
#        if XNATCommunicatorType == "pyxnat":
#            print("XNATSlicer Module: Seeing if PyXNAT is installed...")
#            #===================================================================
#            # CAN PYXNAT BE IMPORTED?
#            #===================================================================
#            try:      
#                import pyxnat
#                print("XNATSlicer Module: Found PyXNAT!")
#            #===================================================================
#            # IF NOT, TRY INSTALL WIZARD.
#            #===================================================================
#            except Exception, e:
#                print("XNATSlicer Module: PyXNAT not found! Beginning installation wizard.")
#                self.installWizard= XNATInstallWizard()
#                if not self.installWizard.pyXNATInstalled():
#                    self.installWizard.beginWizard()
#                    return  
#            # Init communicator.
#            XNATCommunicator = PyXNAT(browser = self, 
#                               server = self.settings.getAddress(self.hostDropdown.currentText), 
#                               user = self.usernameLine.text, password=self.passwordLine.text, 
#                               cachedir = self.utils.pyXNATCache)
#        #=======================================================================
#        # BEGIN COMMUNICATOR
#        #=======================================================================
#        self.XNATView.begin(XNATCommunicator)
#
#    def populateCurrUser(self):
#        """ If "Remember username" is clicked, queries the settings file to bring up 
#        the username saved.
#        """
#        #=======================================================================
#        # Does the username exist in the settings file?
#        #=======================================================================
#        if self.currHostName:    
#            currUser = self.settings.getCurrUsername(self.currHostName).strip("").strip(" ")
#            if len(currUser) > 0:  
#                self.usernameLine.setText(currUser)
#            else: 
#                self.usernameLine.setText(self.defaultUsernameText)
#        #=======================================================================
#        # IF NOT, POPULATE WITH DEFAULT LINE
#        #=======================================================================
#        else:
#            self.usernameLine.setText(self.defaultUsernameText)        
#  
#    def simulateLoginClicked(self):
#        """ Equivalent of clicking the login button.
#        """
#        self.loginButton.animateClick()
#        self.loginButtonClicked()
#          
#    def settingsButtonClicked(self):
#        """ Equivalent of clicking the settings button.
#        """
#        self.settingsPopup = SettingsPopup(self, self.settings)
#        self.settingsPopup.show()
#  
#    def usernameLineEdited(self):
#        """ Listener when the username line is edited.
#        """     
#        if self.defaultUsernameText in str(self.usernameLine.text): 
#            self.usernameLine.setText("")   
#        
#    def passwordLineEdited(self):  
#        """ Listener for when the password line is edited.
#        """     
#        if self.defaultPasswordText in str(self.passwordLine.text): 
#            self.passwordLine.setText("")
#        self.passwordLine.setEchoMode(2)
#        
#    def hostDropdownClicked(self, name):
#        """ Signal methods once dropdown is clicked -- loads the stored hosts.
#        """
#        self.currHostName = self.hostDropdown.currentText
#        if self.hostDropdown.currentText:    
#            self.populateCurrUser()
#      
#    def loginButtonClicked(self):
#        """ Signal methods once the login button is clicked.
#        """        
#        self.settings.setCurrUsername(self.hostDropdown.currentText, self.usernameLine.text)
#        self.XNATView.viewWidget.clear()
#        if self.settings.getAddress(self.hostDropdown.currentText):
#            self.currHostUrl = qt.QUrl(self.settings.getAddress(self.hostDropdown.currentText))
#        else:
#            pass  
#        self.loggedIn = True
#        self.beginXNAT(XNATCommunicatorType = "pyxnat", viewType = "treeview")
#
#class labelStatusBar(object):    
#    def __init__(self, parent = None, numLabels = 3):
#        self.labels = []
#        self.qtLayout = qt.QVBoxLayout()
#        for i in range (0, numLabels):
#            lab = qt.QLabel("")
#            lab.setWordWrap(True)
#            self.labels.append(lab)
#            self.labels[i].setFont(qt.QFont("Arial", 7, 0, False))
#            self.layout.addWidget(lab)
#        self.showMessage(["Not logged in to XNAT server.", "Please login.", ""], True)
#    
#    def showMessage(self, strings, ital = False, bold = False):      
#        for i in range(0, len(strings)):
#            if ital: strings[i] = "<i>" + strings[i] + "</i>"
#            if bold: strings[i] = "<b>" + strings[i] + "</b>"
#            self.labels[i].setText(strings[i])
#            
#    @property
#    def layout(self):
#       return self.qtLayout

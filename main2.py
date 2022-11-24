import sys
from PyQt5.QtWidgets import QMainWindow , QApplication,QToolBar, QPushButton , QLineEdit
from PyQt5.QtGui import QIcon , QFont
from PyQt5.QtCore import QSize , QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage,QWebEngineView 

class Window(QMainWindow) :
    def __init__(self):#instance,one can easily access all attributes and methods init:constructor this method called when object is formed
        super().__init__()#attributes are required to access

        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("icons/python.png"))
        self.setGeometry(200,200, 900,600)
        toolbar=QToolBar()
        self.addToolBar(toolbar)

        self.backButton=QPushButton()
        self.backButton.setIcon(QIcon("icons/back.png"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backbtn)
        toolbar.addWidget(self.backButton)

        self.reload=QPushButton()
        self.reload.setIcon(QIcon("icons/reload.png"))
        self.reload.setIconSize(QSize(36,36))
        self.reload.clicked.connect(self.rldbtn)
        toolbar.addWidget(self.reload)

        self.home=QPushButton()
        self.home.setIcon(QIcon("icons/Home.png"))
        self.home.setIconSize(QSize(36,36))
        self.home.clicked.connect(self.homebtn)
        toolbar.addWidget(self.home)

        self.forwardButton=QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize(36,36))
        self.forwardButton.clicked.connect(self.forwrdbtn)
        toolbar.addWidget(self.forwardButton)
        

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif",18))
        self.addressLineEdit.returnPressed.connect(self.searchbutn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchbutton=QPushButton()
        self.searchbutton.setIcon(QIcon("icons/search.png"))
        self.searchbutton.setIconSize(QSize(36,36))
        self.searchbutton.clicked.connect(self.searchbutn)
        toolbar.addWidget(self.searchbutton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl="https://www.google.com"
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    def searchbutn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backbtn(self):
        self.webEngineView.back()

    def forwrdbtn(self):
        self.webEngineView.forward()

    def rldbtn(self):
        self.webEngineView.reload()
    def homebtn(self):
        self.webEngineView.load(QUrl("https://www.google.com"))




app =QApplication(sys.argv)#list in py that contain all command line arguments script

window =Window()
window.show()
sys.exit(app.exec_())

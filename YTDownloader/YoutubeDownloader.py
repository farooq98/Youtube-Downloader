from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import requests
import pytube
from PIL import Image
import io
import os
import time


class Ui_MainWindow(object):

    def __init__(self):
        self.streamData = None
        self.videoTitle = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(0.85)
        MainWindow.setStyleSheet("background-color: #831010; color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.urlTxtbox = QtWidgets.QLineEdit(self.centralwidget)
        self.urlTxtbox.setGeometry(QtCore.QRect(130, 130, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urlTxtbox.setFont(font)
        self.urlTxtbox.setStyleSheet("#urlTxtbox{\n"
"border: 0px solid black;\n"
"border-bottom: 2px solid white;\n"
"background-color: transparent;\n"
"color: white;\n"
"}")
        self.urlTxtbox.setObjectName("urlTxtbox")
        self.titleLbl = QtWidgets.QLabel(self.centralwidget)
        self.titleLbl.setGeometry(QtCore.QRect(10, 170, 791, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setStyleSheet("color: white;")
        self.titleLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLbl.setObjectName("titleLbl")
        self.getVideoDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getVideoDataBtn.setGeometry(QtCore.QRect(680, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getVideoDataBtn.setFont(font)
        self.getVideoDataBtn.setStyleSheet("#getVideoDataBtn{\n"
"    color: white;\n"
"    background-color: black;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#getVideoDataBtn:hover{\n"
"    color: back;\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}")
        self.getVideoDataBtn.setObjectName("getVideoDataBtn")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 560, 741, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: white")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.downloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downloadBtn.setGeometry(QtCore.QRect(340, 500, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.downloadBtn.setFont(font)
        self.downloadBtn.setStyleSheet("#downloadBtn{\n"
"    color: white;\n"
"    background-color: black;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#downloadBtn:hover{\n"
"    color: back;\n"
"    background-color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"}")
        self.downloadBtn.setObjectName("downloadBtn")
        self.qualityComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.qualityComboBox.setGeometry(QtCore.QRect(120, 440, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qualityComboBox.setFont(font)
        self.qualityComboBox.setStyleSheet("#qualityComboBox{\n"
"border: 0px solid black;\n"
"border-bottom: 2px solid white;\n"
"background-color: transparent;\n"
"}")
        self.qualityComboBox.setObjectName("qualityComboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(300, 230, 211, 201))
        self.imageLbl.setText("")
        self.imageLbl.setPixmap(QtGui.QPixmap("./BZJJiW.png"))
        self.imageLbl.setScaledContents(True)
        self.imageLbl.setObjectName("imageLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.getVideoDataBtn.clicked.connect(self.fetchData)
        self.downloadBtn.clicked.connect(self.downloadBtnClcik)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.label.setText(_translate("MainWindow", "YouTube Downloader"))
        self.label_2.setText(_translate("MainWindow", "Video Url:"))
        self.titleLbl.setText(_translate("MainWindow", "Fetching Data"))
        self.getVideoDataBtn.setText(_translate("MainWindow", "Enter"))
        self.downloadBtn.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Quality:"))

    def enterBtnClick(self):
        self.qualityComboBox.clear()
        url = self.urlTxtbox.text()
        self.video = pytube.YouTube(url)
        self.titleLbl.setText(self.video.title)
        
        self.videoTitle = self.filterTilte(self.video.title)
        
        data = requests.get(self.video.thumbnail_url)
        image_data = data.content
        try:
            thumbnail = Image.open(io.BytesIO(image_data))
            thumbnail.save("thumbnail.jpg")
            time.sleep(0.2)
            self.imageLbl.setPixmap(QtGui.QPixmap("./thumbnail.jpg"))
            os.remove("./thumbnail.jpg")
        except Exception as e:
            print(e)

        # Getting Stream Data
        lst = [str(i).split()[1:4] for i in self.video.streams]
        self.streamData = list(map(lambda x: [int(x[0][6:-1]), x[1][11:-1], x[2][5:-1]], lst))
        comboValues = list(map(lambda x: " ".join(x[1:]), self.streamData))
        self.qualityComboBox.addItems(comboValues)
        self.qualityComboBox.setCurrentIndex(0)

    def downloadBtnClcik(self):
        videofile = self.video.streams.get_by_itag(self.streamData[self.qualityComboBox.currentIndex()][0])
        self.size = videofile.filesize
        
        #self.t2 = Thread(target = videofile.download)
        #self.t2.start()

        self.downloadThread = DownloadThread(videofile.download)
        self.downloadThread.start()

        time.sleep(0.5)

        self.thread = ProgressThread(self.size, self.getSize)
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressBar.setValue(val)

    def filterTilte(self, title):
        return "".join(list(map(lambda x: "" if x in "/\\<>.:|?*\"" else x, title)))

    def getSize(self):
        return os.path.getsize("./" + self.videoTitle + "." + self.streamData[self.qualityComboBox.currentIndex()][1].split("/")[1])
        
    def fetchData(self):
        t1 = Thread(target = self.enterBtnClick)
        t1.start()

class ProgressThread(QThread):

    change_value = pyqtSignal(int)
    
    def __init__(self, size, getSize):
        self.size = size
        self.getSize = getSize
        super().__init__()

    def run(self):
        while self.size != self.getSize():
            self.change_value.emit(round((self.getSize()*100)/self.size))

class DownloadThread(QThread):
    def __init__(self, downloadObject):
        self.downloadObject = downloadObject
        super().__init__()
    
    def run(self):
        self.downloadObject()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    sys.exit()

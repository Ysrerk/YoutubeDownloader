import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pytube import YouTube
import os

fonta=QFont("Arial",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader @Yasar ERKAN")
        self.setGeometry(50,50,400,450)
        self.setStyleSheet("background-color:#7575a3;")


        self.ui()


    def ui(self):
        ###label
        self.linklabel=QLabel("Youtube Video Download ",self)
        self.linklabel.move(130,100)
        self.linklabel.setFont(fonta)
        ###link text
        self.linktext=QLineEdit(self)
        self.linktext.move(25,130)
        self.linktext.resize(350,25)
        self.linktext.setPlaceholderText("Please Enter Youtube Adress")
        self.linktext.setStyleSheet("background-color:#ffffff;")
        ####Download Buton
        self.dowload=QPushButton("Download",self)
        self.dowload.move(125,180)
        self.dowload.setStyleSheet("background-color:#ffff66;")
        self.dowload.resize(150,25)
        self.dowload.clicked.connect(self.youtubedownload)


        #self.file.move(125,205)
        


        self.show()
    def youtubedownload(self):
        self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        adress=str(self.linktext.text())



        yt=YouTube(adress).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists('C:/Users/Administrator/Desktop/video'):
           os.makedirs('C:/Users/Administrator/Desktop/video')
        yt.download(str(self.file))
        QMessageBox.information(self, "QMessageBox.Information()", "This video downloaded")

        #yt.download('C:/Users/Administrator/Desktop/video')

def main():
    application=QApplication(sys.argv)
    window=Window()
    sys.exit(application.exec_())
if __name__ == '__main__':
     main()
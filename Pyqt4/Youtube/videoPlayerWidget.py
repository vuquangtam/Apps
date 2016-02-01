import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.phonon import Phonon
import qrc_resources

class VideoPlayer(QWidget):
    def __init__(self, url=None, parent=None):
        self.url = ''
        QWidget.__init__(self, parent)
        self.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        self.player = Phonon.VideoPlayer(Phonon.VideoCategory, self)
        self.player.setMinimumSize(640, 360)
        self.player.mediaObject().setTickInterval(100)
        self.player.mediaObject().tick.connect(self.tock)

        self.play_pause = QPushButton(self)
        self.play_pause.setIcon(QIcon(':/play.png'))
        self.play_pause.released.connect(self.playClicked)

        self.stop = QPushButton(self)
        self.stop.setIcon(QIcon(':/stop.png'))
        self.stop.clicked.connect(self.stopClicked)

        self.player.mediaObject().stateChanged.connect(self.stateChanged)

        self.slider = Phonon.SeekSlider(self.player.mediaObject() , self)

        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignRight |
            Qt.AlignVCenter)

        self.volume = Phonon.VolumeSlider(self.player.audioOutput(), self)

        topLayout = QVBoxLayout(self)
        topLayout.addWidget(self.player, 2)
        layout = QHBoxLayout(self)
        layout.addWidget(self.play_pause)
        layout.addWidget(self.stop)
        layout.addWidget(self.slider, 2)
        layout.addWidget(self.status)
        layout.addWidget(self.volume)
        topLayout.addLayout(layout)
        self.setLayout(topLayout)

    def changeUrl(self, url):
        self.url = url
        self.player.load(Phonon.MediaSource(url))

    def playClicked(self):
        if self.player.mediaObject().state() == Phonon.PlayingState:
            self.player.pause()
        else:
            self.player.play(Phonon.MediaSource(self.url))

    def stopClicked(self):
        self.player.stop()

    def stateChanged(self, new, old):
        if new == Phonon.PlayingState:
            self.play_pause.setIcon(QIcon(':/pause.png'))
        else:
            self.play_pause.setIcon(QIcon(':/play.png'))

    def tock(self, time):
        time = time/1000
        h = time/3600
        m = (time-3600*h) / 60
        s = (time-3600*h-m*60)
        self.status.setText('%02d:%02d:%02d'%(h,m,s))

def main():
    app = QApplication(sys.argv)
    url = r'C:\guitar.mp4'
    url = r'https://r3---sn-8qj-nboel.googlevideo.com/videoplayback?ip=14.169.166.192&gcr=vn&initcwndbps=2210000&requiressl=yes&mime=video%2Fmp4&key=yt5&upn=NJEWTrP5G1g&itag=18&mt=1437850840&sparams=dur%2Cgcr%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpcm2cms%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&sver=3&source=youtube&ipbits=0&mv=m&pl=19&ms=au&mm=31&mn=sn-8qj-nboel&id=o-AE8HyMx6EJG6wbtv2cvXsJTV96ry2imYzVgpiMUWYqYz&fexp=901803%2C901816%2C9407165%2C9407991%2C9408710%2C9408863%2C9412477%2C9413150%2C9414764%2C9415365%2C9415485%2C9415657%2C9416126%2C9416293%2C9416333%2C9416984%2C9418189%2C9418246&pcm2cms=yes&expire=1437872529&lmt=1394296721739208&dur=228.530&ratebypass=yes&signature=9CE2A5DDA477C5D9223AA78ADF960AEF9C46ABCB.CDCADCFBD6101C22BFDE782B18403242C29745D1'

    window=VideoPlayer()
    window.changeUrl(url)
    window.show()
    #window.playClicked()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
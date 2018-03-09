# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created: Tue Oct 17 15:57:50 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *


import pygame
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

reload(sys)
sys.setdefaultencoding('utf8')



class SetTimer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = MyTimer()

        self.initUi()

        self.show()


    def initUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(471, 315)
        self.pushButton_begin = QtGui.QPushButton(self)
        self.pushButton_begin.setGeometry(QtCore.QRect(180, 270, 91, 31))
        self.pushButton_begin.setObjectName(_fromUtf8("pushButton_begin"))
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(40, 20, 391, 241))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_title = QtGui.QLabel(self.widget)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.horizontalLayout_4.addWidget(self.label_title)
        self.lineEdit_title = QtGui.QLineEdit(self.widget)
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.horizontalLayout_4.addWidget(self.lineEdit_title)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.pushButton_titlefont = QtGui.QPushButton(self.widget)
        self.pushButton_titlefont.setObjectName(_fromUtf8("pushButton_titlefont"))
        self.horizontalLayout_15.addWidget(self.pushButton_titlefont)
        self.pushButton_titlecolor = QtGui.QPushButton(self.widget)
        self.pushButton_titlecolor.setObjectName(_fromUtf8("pushButton_titlecolor"))
        self.horizontalLayout_15.addWidget(self.pushButton_titlecolor)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_background = QtGui.QLabel(self.widget)
        self.label_background.setObjectName(_fromUtf8("label_background"))
        self.horizontalLayout_7.addWidget(self.label_background)
        self.pushbutton_setbackground = QtGui.QPushButton(self.widget)
        self.pushbutton_setbackground.setObjectName(_fromUtf8("pushbutton_setbackground"))
        self.horizontalLayout_7.addWidget(self.pushbutton_setbackground)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_time = QtGui.QLabel(self.widget)
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.horizontalLayout_2.addWidget(self.label_time)
        self.lineEdit_time_hour = QtGui.QLineEdit(self.widget)
        self.lineEdit_time_hour.setObjectName(_fromUtf8("lineEdit_time_hour"))
        self.horizontalLayout_2.addWidget(self.lineEdit_time_hour)
        self.lineEdit_time_minute = QtGui.QLineEdit(self.widget)
        self.lineEdit_time_minute.setObjectName(_fromUtf8("lineEdit_time_minute"))
        self.horizontalLayout_2.addWidget(self.lineEdit_time_minute)
        self.lineEdit_time_seconds = QtGui.QLineEdit(self.widget)
        self.lineEdit_time_seconds.setObjectName(_fromUtf8("lineEdit_time_seconds"))
        self.horizontalLayout_2.addWidget(self.lineEdit_time_seconds)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_timefont = QtGui.QPushButton(self.widget)
        self.pushButton_timefont.setObjectName(_fromUtf8("pushButton_timefont"))
        self.horizontalLayout_6.addWidget(self.pushButton_timefont)
        self.pushButton_timecolor = QtGui.QPushButton(self.widget)
        self.pushButton_timecolor.setObjectName(_fromUtf8("pushButton_timecolor"))
        self.horizontalLayout_6.addWidget(self.pushButton_timecolor)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_zheng = QtGui.QRadioButton(self.widget)
        self.radioButton_zheng.setObjectName(_fromUtf8("radioButton_zheng"))
        self.buttonGroup_time = QtGui.QButtonGroup(self)
        self.buttonGroup_time.setObjectName(_fromUtf8("buttonGroup_time"))
        self.buttonGroup_time.addButton(self.radioButton_zheng)
        self.horizontalLayout_3.addWidget(self.radioButton_zheng)
        self.radioButton_dao = QtGui.QRadioButton(self.widget)
        self.radioButton_dao.setObjectName(_fromUtf8("radioButton_dao"))
        self.buttonGroup_time.addButton(self.radioButton_dao)
        self.horizontalLayout_3.addWidget(self.radioButton_dao)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_audio = QtGui.QLabel(self.widget)
        self.label_audio.setObjectName(_fromUtf8("label_audio"))
        self.horizontalLayout_5.addWidget(self.label_audio)
        self.pushButton_audio = QtGui.QPushButton(self.widget)
        self.pushButton_audio.setObjectName(_fromUtf8("pushButton_audio"))
        self.horizontalLayout_5.addWidget(self.pushButton_audio)
        self.lineEdit_audio_minute = QtGui.QLineEdit(self.widget)
        self.lineEdit_audio_minute.setStatusTip(_fromUtf8(""))
        self.lineEdit_audio_minute.setInputMask(_fromUtf8(""))
        self.lineEdit_audio_minute.setDragEnabled(True)
        self.lineEdit_audio_minute.setReadOnly(False)
        self.lineEdit_audio_minute.setObjectName(_fromUtf8("lineEdit_audio_minute"))
        self.horizontalLayout_5.addWidget(self.lineEdit_audio_minute)
        self.lineEdit_audio_seconds = QtGui.QLineEdit(self.widget)
        self.lineEdit_audio_seconds.setObjectName(_fromUtf8("lineEdit_audio_seconds"))
        self.horizontalLayout_5.addWidget(self.lineEdit_audio_seconds)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):


        self.setWindowTitle("设置")

        self.pushButton_begin.setText(_translate("self", "开始", None))
        self.label_title.setText(_translate("self", "标题", None))
        self.pushButton_titlefont.setText(_translate("self", "大小", None))
        self.pushButton_titlecolor.setText(_translate("self", "颜色", None))
        self.label_background.setText(_translate("self", "背景图片", None))
        self.pushbutton_setbackground.setText(_translate("self", "设置", None))
        self.label_time.setText(_translate("self", "时间", None))
        self.lineEdit_time_hour.setText(_translate("self", "0", None))
        self.lineEdit_time_minute.setText(_translate("self", "0", None))
        self.lineEdit_time_seconds.setText(_translate("self", "0", None))
        self.pushButton_timefont.setText(_translate("self", "大小", None))
        self.pushButton_timecolor.setText(_translate("self", "颜色", None))
        self.radioButton_zheng.setText(_translate("self", "正计时", None))
        self.radioButton_dao.setText(_translate("self", "倒计时", None))
        self.label_audio.setText(_translate("self", "声音", None))
        self.pushButton_audio.setText(_translate("self", "设置", None))
        self.lineEdit_audio_minute.setText(_translate("self", "0", None))
        self.lineEdit_audio_seconds.setText(_translate("self", "0", None))

        self.pushbutton_setbackground.clicked.connect(self.setBackground)
        self.pushButton_timefont.clicked.connect(self.setTimeSize)
        self.pushButton_timecolor.clicked.connect(self.setTimeColor)
        self.pushButton_audio.clicked.connect(self.setAudio)
        self.connect(self.pushButton_titlefont, QtCore.SIGNAL('clicked()'), self.setTitleSize)
        self.pushButton_titlecolor.clicked.connect(self.setTitleColor)

        self.pushButton_begin.clicked.connect(self.beginShow)

        self.timeString=""

        #更新红色
        self.timerLightRed = QTimer(self)
        self.timerLightRed.timeout.connect(self.updateLightRed)

        # 更新黑色
        self.timerLightBlack = QTimer(self)
        self.timerLightBlack.timeout.connect(self.updateLightBlack)


        #更新秒
        self.timerSecond = QTimer(self)
        self.timerSecond.timeout.connect(self.updateSecond)



        self.hour = 0
        self.minute = 0
        self.second = 0



    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()



    def setTitleSize(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.ui.label_title.setFont(font)


    def setTitleColor(self):
        color = QtGui.QColorDialog.getColor()  # 创建颜色选择对话框
        if color.isValid():
            #self.ui.label_title.setText(color.name())
            self.mycolor = "color:" + str(color.name())
            self.ui.label_title.setStyleSheet(self.mycolor)


    def setBackground(self):
        palette1 = QtGui.QPalette(self)

        self.imgName = QtGui.QFileDialog.getOpenFileName(self, "open file dialog", "C:\Users\Administrator\Desktop",
                                                         "all files(*.*)")

        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(self.imgName)))
        self.ui.setPalette(palette1)

        self.ui.setAutoFillBackground(True)  # 不设置也可以



    def setTimeSize(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.ui.label_time.setFont(font)



    def setTimeColor(self):
        color = QtGui.QColorDialog.getColor()  # 创建颜色选择对话框
        if color.isValid():
            # self.ui.label_title.setText(color.name())
            self.mycolor = "color:" + str(color.name())
            self.ui.label_time.setStyleSheet(self.mycolor)


    def setAudio(self):

        #寻找音频文件的路径
        pygame.mixer.init()

        self.audioPath = QtGui.QFileDialog.getOpenFileName(self, "open file dialog", "C:\Users\Administrator\Desktop",
                                                            "all files(*.*)")


    def updateLightRed(self):
        self.ui.label_time.setStyleSheet(_fromUtf8(

                                             "color: rgb(255, 0, 0);"))

        #self.ui.label_time.setVisible(False)

    def updateLightBlack(self):
        self.ui.label_time.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"

                                             ))
        #self.ui.label_time.setVisible(True)


    #开始展示倒计时界面
    def beginShow(self):

        checkAll=self.detectInput()

        if checkAll:
            # 时间倒计时
            self.setTitleTime()
            # 声音倒计时
            self.ui.audio_m = int(str(self.lineEdit_audio_minute.text()))
            self.ui.audio_s = int(str(self.lineEdit_audio_seconds.text()))
            self.minuteFirst=True
            self.hourFirst=True
            #开启倒计时

            self.timerSecond.start(1000)

            self.audioMinute = int(self.lineEdit_audio_minute.text())
            self.audioSecond = int(self.lineEdit_audio_seconds.text())



        else:
            msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "提示", "请设置好所有输入内容！")
            msg_box.show()
            msg_box.exec_()
            return



    #检测是否输入了所需数据
    def detectInput(self):
        if self.lineEdit_title.text()=="":
            return False
        if self.lineEdit_time_seconds.text()=="":
            return False
        if self.lineEdit_time_minute.text()=="":
            return False
        if self.lineEdit_time_hour.text()=="":
            return False
        if self.lineEdit_audio_seconds.text()=="":
            return False
        if self.lineEdit_audio_minute.text()=="":
            return False
        if self.radioButton_dao.isChecked() or self.radioButton_zheng.isChecked():
            return True
        else:
            return False


    #获取倒计时时间
    def setTitleTime(self):
        #设置标题
        self.ui.label_title.setText(self.lineEdit_title.text())
        #设置时间
        hour=int(self.lineEdit_time_hour.text())
        minute=int(self.lineEdit_time_minute.text())
        second=int(self.lineEdit_time_seconds.text())

        self.hour=hour
        self.minute=minute
        self.second=second

        self.hourTemp=hour
        self.minuteTemp=minute
        self.secondTemp=second

        if hour>60 or minute>60 or second>60:
            msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "提示", "输入的时间不正确！")
            msg_box.show()
            msg_box.exec_()
            return

        if hour<10:
            hourStr="0"+str(hour)
        else:
            hourStr=str(hour)

        if minute<10:
            minuteStr="0"+str(minute)
        else:
            minuteStr=str(minute)
        if second<10:
            secondStr="0"+str(second)
        else:
            secondStr=str(second)



        #假如是倒计时
        if self.radioButton_dao.isChecked():
            strTime = hourStr + ":" + minuteStr + ":" + secondStr

        #假如是正计时
        if self.radioButton_zheng.isChecked():
            strTime="00:00:00"

            self.hour = 0
            self.minute = 0
            self.second = 0


        self.ui.label_time.setText(strTime)




    def updateSecond(self):

        if self.radioButton_dao.isChecked():

            if self.second==0:
                if self.minute==0:
                    if self.hour==0:
                        self.timerSecond.stop()
                        return
                    if self.hour > 0:
                        self.hour=self.hour -1
                        self.minute=60
                if self.minute > 0:
                    self.minute=self.minute-1
                    self.second=60

            if self.second>0:
               self.second=self.second-1



            if self.hour < 10:
                hourStr = "0" + str(self.hour)
            else:
                hourStr = str(self.hour)

            if self.minute < 10:
                minuteStr = "0" + str(self.minute)
            else:
                minuteStr = str(self.minute)
            if self.second < 10:
                secondStr = "0" + str(self.second)
            else:
                secondStr = str(self.second)

            strTime = hourStr + ":" + minuteStr + ":" + secondStr
            self.ui.label_time.setText(strTime)


            # 播放音频文件
            if self.hour == 0:
                if self.minute == self.audioMinute and self.second == self.audioSecond:
                    # 播放音频文件


                    self.timerLightRed.start(1000)
                    self.timerLightBlack.start(1080)


                    audioStr = str(self.audioPath)

                    if len(audioStr) != 0:
                        track = pygame.mixer.music.load(audioStr)
                        pygame.mixer.music.play()
            return

        if self.radioButton_zheng.isChecked():

            # 如果时，分，秒都等于给定时间，那么计时结束

            if self.second==self.secondTemp:
                if self.minute>=self.minuteTemp:
                    if self.hour>=self.hourTemp:
                        self.timerSecond.stop()
                        return

            self.second = self.second + 1

            if self.second==60:
                self.second=0

                if self.hour  <self.hourTemp or self.minute  < self.minuteTemp:

                    self.minute=self.minute+1

                    if self.minute==60:
                        self.minute=0
                        self.hour=self.hour+1




            if self.hour < 10:
                hourStr = "0" + str(self.hour)
            else:
                hourStr = str(self.hour)

            if self.minute < 10:
                minuteStr = "0" + str(self.minute)
            else:
                minuteStr = str(self.minute)
            if self.second < 10:
                secondStr = "0" + str(self.second)
            else:
                secondStr = str(self.second)

            strTime = hourStr + ":" + minuteStr + ":" + secondStr
            self.ui.label_time.setText(strTime)

            # 播放音频文件
            if self.hour== 0:
                if (self.minuteTemp-self.minute) == self.audioMinute and (self.secondTemp-self.second) == self.audioSecond:
                    # 播放音频文件

                    self.timerLightRed.start(1000)
                    self.timerLightBlack.start(1080)


                    audioStr = str(self.audioPath)

                    if len(audioStr) != 0:
                        track = pygame.mixer.music.load(audioStr)
                        pygame.mixer.music.play()


            return



class MyTimer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initUi()

        self.showFullScreen()


    def initUi(self):
        self.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_title = QtGui.QLabel(self)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.horizontalLayout.addWidget(self.label_title)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 69, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_time = QtGui.QLabel(self)
        self.label_time.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_time)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):

        self.label_title.setText("标题")
        self.label_time.setText("00:00:00")



        #设置总时间
        self.time_h=0
        self.time_m=1
        self.time_s=10

        #设置声音倒计时
        self.audio_m=0
        self.audio_s=10





    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()

        if  key == QtCore.Qt.Key_Space:
            self.openConfigDialog()

        if  key == QtCore.Qt.Key_T:
            self.setTitleFont()



    def setTitleFont(self,font):
        self.label_title.setFont(font)




if __name__ == "__main__":
    import sys


    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)

    ui =SetTimer()
    ui.show()



    sys.exit(app.exec_())



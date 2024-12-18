import os
import configparser
import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
import asyncio
import telegram
from datetime import datetime
#from playsound import playsound
import threading
from colorama import Fore, Back, Style
import pygame
import functions as func
if sys.platform == "linux":
    from pynput.keyboard import Key, KeyCode, Listener, Controller
    import subprocess
    import time
    

else:
    import pygetwindow as gw



#keyboard = Controller()
whispernicks = []
lastwhispernick = ""

#x = threading.Thread(target=func.thread_function, name="input_thread", args=(whispernicks, lastwhispernick, ))
#x.start()

y = threading.Thread(target=func.thread_keypress, name="keypress")
y.start()



#y = threading.Thread(target=func.onlineCount, name="online_counter_threade")
#y.start()



def main_progress(window):
    

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

    open(config['FILES']['clienttxt'], "r")
    originalTime = os.path.getmtime(config['FILES']['clienttxt'])

    lastlinesold = sum(1 for line in open(
        config['FILES']['clienttxt'], 'r', encoding='UTF8'))
    lastseenline = ""

    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    getpath = os.path.join(bundle_dir, 'trade.db')
    verbindung = sqlite3.connect(getpath)

    l=0



    while True:
        time.sleep(0.5)
        if os.path.getmtime(config['FILES']['clienttxt']) > originalTime:



            config = configparser.ConfigParser()
            config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
            ding = open(config['FILES']['clienttxt'], 'r', encoding='UTF8')
            lastlinesnew = sum(1 for line in ding)


            while lastlinesold < lastlinesnew:
                last_line = open(config['FILES']['clienttxt'],
                                'r', encoding='UTF8').readlines()[lastlinesold]


                if "has been slain" in last_line:
                    cursor = verbindung.cursor()
                    exucute = f'SELECT * FROM deaths'
                    cursor.execute(exucute)
                    zeile = cursor.fetchone()

                    deaths = zeile[0]

                    deaths += 1

                    cursor = verbindung.cursor()
                    cursor.execute(f'update deaths set counter = "{deaths}"')

                    verbindung.commit()

                    print(Fore.RED + f'Aktuelle Tode: {deaths}')
                    print(Style.RESET_ALL)

                    #getpath = os.path.join(bundle_dir, 'fail-trombone-01.mp3')
                    #pygame.mixer.init()
                    #pygame.mixer.music.load(getpath)
                    #pygame.mixer.music.play()

                if config['FILES']['league'] in last_line and "@From" in last_line and "buy" in last_line and "position" in last_line:
                    l=l+1
                    splitmsg = last_line.split()
                    buyer = splitmsg[splitmsg.index("Hi,") - 1]
                    #buyer = buyer[1:]
                    del splitmsg[0:splitmsg.index("Hi,")]
                    buyer = buyer[:-1]
                    item = splitmsg[splitmsg.index("your") + 1:splitmsg.index("listed")]
                    price = splitmsg[splitmsg.index("for") + 1:splitmsg.index("for") + 3]
                    stash = splitmsg[splitmsg.index(config['FILES']['league']) + 1:splitmsg.index(config['FILES']['league']) + 11]

                    windowtext = " ".join(item)
                    windowprice = " ".join(price)
                    windowstash = " ".join(stash)

                    now = datetime.now()

                    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

                    cursor = verbindung.cursor()
                    cursor.execute(f'insert into trades ("nick", "item", "price", "time") values ("{buyer}", "{windowtext}", "{windowprice}", "{current_time}")')
                    x = len(whispernicks)

                    whispernicks.append(buyer)

                    lastwhispernick = buyer
                    verbindung.commit()



                    window.listWidget.addItem(f'{l}. Buyer: {buyer} - Item {windowtext} - Price: {windowprice} - {current_time}')


                    print(Fore.MAGENTA + f'{l}. Buyer: {buyer} - Item {windowtext} - Price: {windowprice} - {current_time}')
                    print(Style.RESET_ALL)
                    getpath = os.path.join(bundle_dir, 'horn.mp3')
                    pygame.mixer.init()
                    pygame.mixer.music.load(getpath)
                    pygame.mixer.music.play()


                    window.setWindowState(QtCore.Qt.WindowActive)

                    async def send(chat, msg):
                        await telegram.Bot('7770976930:AAGiIoVEjcVR5CF8y4I3EtdUjN02ZVBaFrs').sendMessage(chat_id=chat, text=msg)

                    asyncio.run(send('856990350', f'Neuer Trade über {windowprice}' ))


                if config['FILES']['league'] in last_line and "@From" in last_line and "buy" in last_line and "I'd like" in last_line:
                    l=l+1
                    splitmsg = last_line.split()
                    buyer = splitmsg[splitmsg.index("Hi,") - 1]
                    #buyer = buyer[1:]
                    del splitmsg[0:splitmsg.index("Hi,")]
                    buyer = buyer[:-1]
                    item = splitmsg[splitmsg.index("your") + 1:splitmsg.index("for")]
                    price = splitmsg[splitmsg.index("my") + 1:splitmsg.index("my") + 3]


                    windowtext = " ".join(item)
                    windowprice = " ".join(price)


                    now = datetime.now()

                    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

                    cursor = verbindung.cursor()
                    cursor.execute(f'insert into trades ("nick", "item", "price", "time") values ("{buyer}", "{windowtext}", "{windowprice}", "{current_time}")')



                    window.listWidget.addItem(f'{l}. Buyer: {buyer} - Item {windowtext} - Price: {windowprice} - {current_time}')
                    x = len(whispernicks)

                    whispernicks.append(buyer)

                    lastwhispernick = buyer
                    verbindung.commit()



                    print(Fore.MAGENTA + f'{l}. Buyer: {buyer} - Item {windowtext} - Price: {windowprice} - {current_time}')
                    print(Style.RESET_ALL)
                    getpath = os.path.join(bundle_dir, 'horn.mp3')
                    pygame.mixer.init()
                    pygame.mixer.music.load(getpath)
                    pygame.mixer.music.play()

                    window.setWindowState(QtCore.Qt.WindowActive)
                    async def send(chat, msg):
                        await telegram.Bot('7770976930:AAGiIoVEjcVR5CF8y4I3EtdUjN02ZVBaFrs').sendMessage(chat_id=chat, text=msg)

                    asyncio.run(send('856990350', f'Neuer Trade über {windowprice}' ))


                lastlinesold = lastlinesold + 1
                lastseenline = last_line



class Dialog(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        getpath = os.path.join(bundle_dir, 'trade.ui')

        self = uic.loadUi(getpath, self)
        self.setWindowTitle('Trades')



        self.pushButton.clicked.connect(self.removeSel)
        self.inviteButton.clicked.connect(self.inviteSel)
        self.tradeButton.clicked.connect(self.tradeSel)
        self.kickbutton.clicked.connect(self.KickSel)
        self.kickbutton.clicked.connect(self.removeSel)
        self.momentButton.clicked.connect(self.MomSel)
        self.soldButton.clicked.connect(self.SoldSel)



        z = threading.Thread(target=main_progress, args=(self,))
        z.start()


    def removeSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))


    def inviteSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        msg = self.listWidget.currentItem().text()
        buyer = msg[(msg.index(":") + 1) + 1:msg.index(" -")]
        func.invitebutton(buyer)

    def tradeSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        msg = self.listWidget.currentItem().text()
        buyer = msg[(msg.index(":") + 1) + 1:msg.index(" -")]
        func.tradebutton(buyer)

    def KickSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        msg = self.listWidget.currentItem().text()
        buyer = msg[(msg.index(":") + 1) + 1:msg.index(" -")]
        func.kickbutton(buyer)

    def MomSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        msg = self.listWidget.currentItem().text()
        buyer = msg[(msg.index(":") + 1) + 1:msg.index(" -")]
        func.momentbutton(buyer)

    def SoldSel(self):
        listItems=self.listWidget.selectedItems()
        if not listItems: return
        msg = self.listWidget.currentItem().text()
        buyer = msg[(msg.index(":") + 1) + 1:msg.index(" -")]
        func.soldbutton(buyer)





if __name__ == '__main__':
    

    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

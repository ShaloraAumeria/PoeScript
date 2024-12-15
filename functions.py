import threading
from colorama import Fore, Back, Style
import pygame
import os
import sqlite3
import time
from sys import exit
import threading
import subprocess
import sys
if sys.platform == "linux":
    from pynput.keyboard import Key, KeyCode, Listener, Controller
    import subprocess
    import time
    import pyautogui
else:
    import pygetwindow as gw



#import keyboard

def run_poe():
    time.sleep(2)
    subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 238960")
    time.sleep(2)
    subprocess.call(r"C:\Users\Tora\AppData\Roaming\Path of Building Community\Path of Building.exe")
    time.sleep(2)
    subprocess.call(r"C:\Users\Tora\AppData\Local\Programs\Awakened PoE Trade\Awakened PoE Trade.exe")

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def invitebutton(invite):
    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #invite = invite.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite]) 
        
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    
    

    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-invite {}".format(invite))
    keyboard.type("invite {}".format(invite))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
   

def tradebutton(invite):
    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        
        #invite = invite.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
        
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-tradewith {}".format(invite))
    keyboard.type("tradewith {}".format(invite))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    getpath = os.path.join(bundle_dir, 'trade.db')
    verbindung = sqlite3.connect(getpath)

    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM trades where nick = "{invite}" ORDER BY tid DESC LIMIT 1'
    cursor.execute(exucute)
    zeile = cursor.fetchone()
    windowprice = zeile[3]

    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM incoming'
    cursor.execute(exucute)
    zeile = cursor.fetchone()
    chaos = float(zeile[0])
    exalted = float(zeile[1])
    divine = float(zeile[2])

    if "chaos" in windowprice:
        add = float(windowprice[:windowprice.find("chaos")-1])
        chaos = chaos + add
    if "exalted" in windowprice:
        exalted = exalted + float(windowprice[:windowprice.find("exalted")])
    if "divine" in windowprice:
        divine = divine + float(windowprice[:windowprice.find("divine")])

    cursor = verbindung.cursor()
    cursor.execute(f'update incoming set chaos = "{chaos}", exalted = {exalted}, divine = {divine}')

    verbindung.commit()

def kickbutton(invite):
    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #invite = invite.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.1)
    #keyboard.press(Key.alt_gr)
    #time.sleep(0.1)
    #keyboard.press('q')
    #time.sleep(0.1)
    #keyboard.release('q')
    #time.sleep(0.1)
    #keyboard.release(Key.alt_gr)
    #time.sleep(0.1)
    #time.sleep(0.1)
    #keyboard.press(Key.shift_l)
    #time.sleep(0.1)
    #keyboard.press('5')
    #time.sleep(0.1)
    #keyboard.release('5')
    #time.sleep(0.1)
    #keyboard.release(Key.shift_l)
    #time.sleep(0.1)
    #pyautogui.write("\u0022{} Tz have a nice daz".format(invite))
    
    #keyboard.type(" Ty have a nice day")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-leave")
    keyboard.type("leave")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def momentbutton(invite):
    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #invite = invite.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)
    #test = "@"
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.1)
    #keyboard.press(Key.alt_gr)
    #time.sleep(0.1)
    #keyboard.press('q')
    #time.sleep(0.1)
    #keyboard.release('q')
    #time.sleep(0.1)
    #keyboard.release(Key.alt_gr)
    time.sleep(0.1)
    pyautogui.write(u"\u0040")
    time.sleep(0.1)
    pyautogui.write("{} just a moment".format(invite))
    #keyboard.type("{} just a moment".format(invite))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def soldbutton(invite):
    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #invite = invite.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)
    #test = "@"
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.1)
    #keyboard.press(Key.alt_gr)
    #time.sleep(0.1)
    #keyboard.press('q')
    #time.sleep(0.1)
    #keyboard.release('q')
    #time.sleep(0.1)
    #keyboard.release(Key.alt_gr)
    time.sleep(0.1)
    pyautogui.write("\u0040{} sry Sold".format(invite))
    #keyboard.type("{} just a moment".format(invite))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def func_lastinvite():
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    getpath = os.path.join(bundle_dir, 'trade.db')
    verbindung = sqlite3.connect(getpath)
    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM trades ORDER BY tid DESC LIMIT 1'
    cursor.execute(exucute)
    zeile = cursor.fetchone()

    lastwhispernick = zeile[1]



    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #lastwhispernick = lastwhispernick.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-invite {}".format(lastwhispernick))
    keyboard.type("invite {}".format(lastwhispernick))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def func_tradeleave():
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    getpath = os.path.join(bundle_dir, 'trade.db')
    verbindung = sqlite3.connect(getpath)
    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM trades ORDER BY tid DESC LIMIT 1'
    cursor.execute(exucute)
    zeile = cursor.fetchone()

    lastwhispernick = zeile[1]

    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
        #lastwhispernick = lastwhispernick.replace("_", "?")
        #invite = ''.join(['y' if char == 'z' else 'z' if char == 'y' else char for char in invite])
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    keyboard = Controller()

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.1)
    #keyboard.press(Key.alt_gr)
    #time.sleep(0.1)
    #keyboard.press('q')
    #time.sleep(0.1)
    #keyboard.release('q')
    #time.sleep(0.1)
    #keyboard.release(Key.alt_gr)
    #time.sleep(0.1)
    pyautogui.write("\u0022{} Ty have a nice day".format(lastwhispernick))

    #keyboard.type("Ty have a nice day".format(lastwhispernick))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-leave")
    keyboard.type("leave")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def func_tradelast():
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    getpath = os.path.join(bundle_dir, 'trade.db')
    verbindung = sqlite3.connect(getpath)
    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM trades ORDER BY tid DESC LIMIT 1'
    cursor.execute(exucute)
    zeile = cursor.fetchone()

    lastwhispernick = zeile[1]
    windowprice = zeile[3]


    if sys.platform == "linux":
        subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
    else:
        win = gw.getWindowsWithTitle('Path of Exile')[0]
        win.activate()

    time.sleep(0.5)

    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    keyboard.type("/tradewith {}".format(lastwhispernick))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    cursor = verbindung.cursor()
    exucute = f'SELECT * FROM incoming'
    cursor.execute(exucute)
    zeile = cursor.fetchone()
    chaos = float(zeile[0])
    exalted = float(zeile[1])
    divine = float(zeile[2])

    if "chaos" in windowprice:
        add = float(windowprice[:windowprice.find("chaos")-1])
        chaos = chaos + add
    if "exalted" in windowprice:
        exalted = exalted + float(windowprice[:windowprice.find("exalted")])
    if "divine" in windowprice:
        divine = divine + float(windowprice[:windowprice.find("divine")])

    cursor = verbindung.cursor()
    cursor.execute(f'update incoming set chaos = "{chaos}", exalted = {exalted}, divine = {divine}')

    verbindung.commit()

def func_hideout():
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.press(Key.shift_l)
    time.sleep(0.1)
    keyboard.press('7')
    time.sleep(0.1)
    keyboard.release('7')
    time.sleep(0.1)
    keyboard.release(Key.shift_l)
    time.sleep(0.1)
    #pyautogui.write("-invite {}".format(lastwhispernick))
    keyboard.type("hideout")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def thread_keypress():
    def on_press(key):
        #print('{0} pressed'.format(
            #key))
        check_key(key)

    def on_release(key):
        #print('{0} release'.format(
            #key))
        if key == Key.esc:
            # Stop listener
            return False
        if key == Key.f5:
            func_hideout()
        if key == Key.f7:
            func_lastinvite()
        if key == Key.f8:
            func_tradelast()
        if key == Key.f9:
            func_tradeleave()

    def check_key(key):
        if key in [Key.up, Key.down, Key.left, Key.right]:
            print('-')

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    #keyboard.on_press_key("F7", lambda _:func_lastinvite())
    #keyboard.on_press_key("F8", lambda _:func_tradelast())
    #keyboard.on_press_key("F9", lambda _:func_tradeleave())



def thread_function(whispernicks, lastwhispernick):


    value = ""

    while True:


        value = input("Command:\n")

        if value == "deaths":
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
            getpath = os.path.join(bundle_dir, 'trade.db')
            verbindungth = sqlite3.connect(getpath)

            cursorth = verbindungth.cursor()
            exucuteth = f'SELECT * FROM deaths'
            cursorth.execute(exucuteth)
            zeile = cursorth.fetchone()

            deaths = zeile[0]

            print(Fore.RED + f'Aktuelle Tode: {deaths}')
            print(Style.RESET_ALL)

  
        if "lastinv" in value:


            bundle_dir = os.path.dirname(os.path.abspath(__file__))
            getpath = os.path.join(bundle_dir, 'trade.db')
            verbindung = sqlite3.connect(getpath)
            cursor = verbindung.cursor()
            exucute = f'SELECT * FROM trades ORDER BY tid DESC LIMIT 1'
            cursor.execute(exucute)
            zeile = cursor.fetchone()

            lastwhispernick = zeile[1]

            if sys.platform == "linux":
                subprocess.Popen("wmctrl -R 'Path of Exile'", stdout=subprocess.PIPE, shell=True)
            else:
                win = gw.getWindowsWithTitle('Path of Exile')[0]
                win.activate()

            time.sleep(1)

            keyboard = Controller()
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            #time.sleep(0.1)
            #keyboard.press(Key.shift_l)
            #time.sleep(0.1)
            #keyboard.press('7')
            #time.sleep(0.1)
            #keyboard.release('7')
            #time.sleep(0.1)
            #keyboard.release(Key.shift_l)
            #time.sleep(0.1)
            keyboard.type("/invite {}".format(lastwhispernick))
            time.sleep(0.1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)



        elif value == "incoming":
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
            getpath = os.path.join(bundle_dir, 'trade.db')
            verbindungth = sqlite3.connect(getpath)

            cursorth = verbindungth.cursor()
            exucuteth = f'SELECT * FROM incoming'
            cursorth.execute(exucuteth)
            zeile = cursorth.fetchone()

            chaos = float(zeile[0])
            exalted = float(zeile[1])
            divine = float(zeile[2])

            print(Fore.GREEN + f'Aktuelles Einkommen: {chaos} Chaos {exalted} Exalted {divine} Divine')
            print(Style.RESET_ALL)

        elif value == "online":
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
            getpath = os.path.join(bundle_dir, 'trade.db')
            verbindungth = sqlite3.connect(getpath)

            cursorth = verbindungth.cursor()
            exucuteth = f'SELECT * FROM zeit'
            cursorth.execute(exucuteth)
            zeile = cursorth.fetchone()

            sec = zeile[0]



            print(Fore.GREEN + f'Aktuelle Zeit: {convert(sec)}')
            print(Style.RESET_ALL)

        elif value == "exit":
            process = threading.current_thread()
            print(process.name)

        elif value == "start":
            t2 = threading.Thread(target=run_poe)
            t2.start()

        elif value == "reset":
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
            getpath = os.path.join(bundle_dir, 'trade.db')
            verbindungth = sqlite3.connect(getpath)

            cursor = verbindungth.cursor()
            cursor.execute(f'update incoming set chaos = 0, exalted = 0, divine = 0')

            verbindungth.commit()

            print(Fore.GREEN + f'Incoming resetet')
            print(Style.RESET_ALL)






def onlineCount():
    while True:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        getpath = os.path.join(bundle_dir, 'trade.db')
        verbindungth = sqlite3.connect(getpath)

        cursorth = verbindungth.cursor()
        exucuteth = f'SELECT * FROM zeit'
        cursorth.execute(exucuteth)
        zeile = cursorth.fetchone()

        zeit = zeile[0]

        zeit += 1

        cursorth = verbindungth.cursor()
        cursorth.execute(f'update zeit set time = "{zeit}"')

        verbindungth.commit()
        time.sleep(1)

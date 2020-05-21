from pynput.keyboard import Key, Controller
import pyautogui
import time
import webbrowser

keyboard = Controller()
links = []
hours = []
classesTaken = 0
totalClasses = 0

def joinZoom(link):
    webbrowser.open(link)
    time.sleep(10)
    for x in range(3):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    pyautogui.click(682, 382)

def getNextClass(dia):
    minimumHours = 24
    minimumMins = 59
    totalClasses = 0
    now = time.localtime()
    index = -1
    f = open("../../Schedule/"+dia+".txt", "r")
    for x in f:
        links.append(x.split(',')[0])
        hours.append(x.split(',')[1])
        hour = int(x.split(',')[1].split(':')[0])
        minute = int(x.split(',')[1].split(':')[1])
        hoursToNextClass = hour - now.tm_hour
        minsToNextClass = minute - now.tm_min
        # print(hoursToNextClass, minsToNextClass)
        if hoursToNextClass == 0 and minsToNextClass >= 0 and minsToNextClass < minimumMins:
            minimumHours = 0
            minimumMins = minsToNextClass
            index = totalClasses
        elif hoursToNextClass > 0 and hoursToNextClass <= minimumHours and minsToNextClass <= 0 and minsToNextClass <= minimumMins:
            minimumHours = hoursToNextClass
            minimumMins = minsToNextClass
            index = totalClasses
        totalClasses += 1
    return index, totalClasses

day = input("What day is today? ")
index, totalClasses = getNextClass(day)
nextHour = hours[index].split(':')
print("It's working! Your next class is at"+hours[index]+"(do not close this window)")
print("Total classes today: ", totalClasses)
while classesTaken <= totalClasses:
    time.sleep(20)
    now = time.localtime()
    inSession = False
    if now.tm_hour == int(nextHour[0]) and now.tm_min == int(nextHour[1]) and inSession == False:
        joinZoom(links[index])
        classesTaken += 1;
        print("Joined!")
        getNextClass(day)
        print("Your next class is at"+hours[index]+"(do not close this window)")
        print("You're missing "+(totalClasses-classesTaken)+" classes")
        inSession = True
        time.sleep(60)

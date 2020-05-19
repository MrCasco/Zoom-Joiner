from pynput.mouse import Button, Controller
from pynput.keyboard import Key
import time
import webbrowser

mouse = Controller()
def joinZoom(link):
    webbrowser.open(link)
    mouse.position = (695, 528)
    for x in range(3, 5):
        time.sleep(x)
        mouse.click(Button.left, 1)

links = []
hours = []
joined = False
classesTaken = 0
totalClasses = 0
now = time.localtime()
minimumHours = 24
minimumMins = 59
index = 0
dia = input("What day is today? ")
f = open("Horarios por día/"+dia+".txt", "r")
for x in f:
    links.append(x.split(',')[0])
    hours.append(x.split(',')[1])
    hour = int(x.split(',')[1].split(':')[0])
    minute = int(x.split(',')[1].split(':')[1])
    hoursToNextClass = hour - now.tm_hour
    minsToNextClass = minute - now.tm_min
    if hoursToNextClass >= 0 and hoursToNextClass <= minimumHours:
        if minsToNextClass >= 0 and minsToNextClass <= minimumMins:
            minimumHours = hoursToNextClass
            minimumMins = minsToNextClass
            index = totalClasses
    totalClasses += 1

nextHour = hours[index].split(':')
print("Ya funciona! Espera tu siguiente clase (no cierres esta ventana)")
while joined == False:
    time.sleep(20)
    now = time.localtime()
    if now.tm_hour == int(nextHour[0]) and now.tm_min == int(nextHour[1]):
        classesTaken += 1;
        joinZoom(links[classesTaken])
        print("now")
        joined = True

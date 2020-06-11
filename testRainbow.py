import os, sys, subprocess, time
from rainbowhatwrapper.handlers import *

#CONSTANTS
BUTTON_A_STATE = False
BUTTON_B_STATE = False
BUTTON_C_STATE = False

def showUptime():
    while True:
        test = subprocess.Popen(["uptime"], stdout=subprocess.PIPE)
        output = test.communicate()[0].split()[0].split(':')
        hour = output[0]
        mins = output[1]
        RhDisplayHandler.printOnDisplay(hour + mins)
        time.sleep(15)

def main():
    RhPixelHandler.setPixel(0, 1, 1, 1)
    RhPixelHandler.setPixel(1, 1, 1, 1)
    RhPixelHandler.setPixel(2, 1, 1, 1)
    RhPixelHandler.setPixel(3, 1, 1, 1)
    RhPixelHandler.setPixel(4, 1, 1, 1)
    RhPixelHandler.setPixel(5, 1, 1, 1)
    RhPixelHandler.setPixel(6, 1, 1, 1)
    RhBuzzerHandler.playBeginning()
    # showUptime()
    # song = [68, 68, 68, 69, 70, 70, 69, 70, 71, 72]
    # for note in song:
    #     RhBuzzerHandler.playMidi(note, 0.5)
    #     time.sleep(1)
    # RhBuzzerHandler.play(261, 1)
    # print (RhWeatherHandler.getTemperature())
    # print (RhWeatherHandler.getPressure())
    RhDisplayHandler.printOnDisplay("hello.world.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('Interrupted!')
        try:
            RhDisplayHandler.clear()
            sys.exit(0)
        except SystemExit:
            os._exit(0)


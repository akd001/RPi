import rainbowhat as rh
import os, sys, subprocess, time

#CONSTANTS
BUTTON_A_STATE = False
BUTTON_B_STATE = False
BUTTON_C_STATE = False

def showUptime():
    while True:
        clearRhDisplay()
        test = subprocess.Popen(["uptime"], stdout=subprocess.PIPE)
        output = test.communicate()[0].split()[0].split(':')
        hour = output[0]
        mins = output[1]
        rh.display.print_str(hour + mins)
        showRhDisplay()
        time.sleep(15)


def showRhDisplay():
    try:
        rh.display.show()
    except Exception as e:
        print str(e)
        
def clearRhDisplay():
    try:
        rh.display.clear()
    except Exception as e:
        print str(e)


def updateButtonLedState():
    led_a = 1 if BUTTON_A_STATE else 0
    led_b = 1 if BUTTON_B_STATE else 0
    led_c = 1 if BUTTON_C_STATE else 0
    rh.lights.rgb(led_a, led_b, led_c)

def toggleButtonA():
    global BUTTON_A_STATE
    BUTTON_A_STATE = False if BUTTON_A_STATE else True
    updateButtonLedState()
    
def toggleButtonB():
    global BUTTON_B_STATE
    BUTTON_B_STATE = False if BUTTON_B_STATE else True
    updateButtonLedState()

def toggleButtonC():
    global BUTTON_C_STATE
    BUTTON_C_STATE = False if BUTTON_C_STATE else True
    updateButtonLedState()

@rh.touch.A.press()
def touch_a(channel):
    print ("Button A pressed")

@rh.touch.A.release()
def release_a(channel):
    print ("Button A released")
    toggleButtonA()
    
@rh.touch.B.press()
def touch_b(channel):
    print ("Button B pressed")

@rh.touch.B.release()
def release_b(channel):
    print ("Button B released")
    toggleButtonB()

@rh.touch.C.press()
def touch_c(channel):
    print ("Button C pressed")
    
@rh.touch.C.release()
def release_c(channel):
    print ("Button C released")
    toggleButtonC()


def main():
    showUptime()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ('Interrupted!')
        try:
            clearRhDisplay()
            sys.exit(0)
        except SystemExit:
            os._exit(0)

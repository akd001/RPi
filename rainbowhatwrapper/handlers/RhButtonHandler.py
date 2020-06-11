import rainbowhatwrapper.util.RhButtonUtil as rhButton

#CONSTANTS
BUTTON_A_STATE = False
BUTTON_B_STATE = False
BUTTON_C_STATE = False

class RhButtonHandler:

    @classmethod
    def updateButtonLedState(cls):
        global BUTTON_A_STATE, BUTTON_B_STATE, BUTTON_C_STATE
        rhButton.updateButtonLedState(
            BUTTON_A_STATE,
            BUTTON_B_STATE,
            BUTTON_C_STATE
        )

    @classmethod
    def toggleButtonA(cls):
        global BUTTON_A_STATE
        BUTTON_A_STATE = False if BUTTON_A_STATE else True
        cls.updateButtonLedState()
    
    @classmethod
    def toggleButtonB(cls):
        global BUTTON_B_STATE
        BUTTON_B_STATE = False if BUTTON_B_STATE else True
        cls.updateButtonLedState()
    
    @classmethod
    def toggleButtonC(cls):
        global BUTTON_C_STATE
        BUTTON_C_STATE = False if BUTTON_C_STATE else True
        cls.updateButtonLedState()

    @classmethod
    def setLedState(cls, led_a, led_b, led_c):
        rhButton.updateButtonLedState(led_a, led_b, led_c)
        
    @rhButton.rhtouch.A.press()
    def touch_a(channel):
        print ("Button A pressed")
        
    @rhButton.rhtouch.A.release()
    def release_a(channel):
        print ("Button A released")
        RhButtonHandler.toggleButtonA()
    
    @rhButton.rhtouch.B.press()
    def touch_b(channel):
        print ("Button B pressed")
    
    @rhButton.rhtouch.B.release()
    def release_b(channel):
        print ("Button B released")
        RhButtonHandler.toggleButtonB()
    
    @rhButton.rhtouch.C.press()
    def touch_c(channel):
        print ("Button C pressed")
    
    @rhButton.rhtouch.C.release()
    def release_c(channel):
        print ("Button C released")
        RhButtonHandler.toggleButtonC()
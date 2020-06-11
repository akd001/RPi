import rainbowhatwrapper.util.RhDisplayUtil as rhDisplay

class RhDisplayHandler:
    
    @classmethod
    def show(cls):
        rhDisplay.showRhDisplay()

    @classmethod
    def clear(cls):
        rhDisplay.clearRhDisplay()
    
    @classmethod
    def printOnDisplay(cls, stringToPrint):
        rhDisplay.clearRhDisplay()
        rhDisplay.printRhDisplay(stringToPrint)
        rhDisplay.showRhDisplay()
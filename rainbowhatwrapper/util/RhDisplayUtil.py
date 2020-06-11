import rainbowhat as rh

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

def printRhDisplay(stringToPrint):
    try:
        rh.display.print_str(stringToPrint)
    except Exception as e:
        print str(e)
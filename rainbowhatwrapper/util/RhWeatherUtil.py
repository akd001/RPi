import rainbowhat as rh

def getTemperature():
    try:
        return rh.weather.temperature()
    except Exception as e:
        print (str(e))

def getPressure():
    try:
        return rh.weather.pressure()
    except Exception as e:
        print (str(e))
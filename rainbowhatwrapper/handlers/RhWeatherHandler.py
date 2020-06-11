import rainbowhatwrapper.util.RhWeatherUtil as rhWeather

class RhWeatherHandler:

    @classmethod
    def getTemperature(cls):
        return rhWeather.getTemperature()
    
    @classmethod
    def getPressure(cls):
        return rhWeather.getPressure()
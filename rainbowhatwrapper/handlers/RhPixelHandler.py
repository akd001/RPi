import rainbowhatwrapper.util.RhPixelUtil as rhPixel

class RhPixelHandler:

    @classmethod
    def switchPixelOff(cls, pixel_id):
        setPixel(pixel_id, 0, 0, 0);
    
    @classmethod
    def setPixel(cls, pixel_id, r_value, g_value, b_value):
        rhPixel.updatePixel(pixel_id, r_value, g_value, b_value)
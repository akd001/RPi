import rainbowhat as rh

def updatePixel(pixel_id, r_value, g_value, b_value):
    try:
        rh.rainbow.set_pixel(pixel_id, r_value, g_value, b_value);
        rh.rainbow.show();
    except Exception as e:
        print srt(e)

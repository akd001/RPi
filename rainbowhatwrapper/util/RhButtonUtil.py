import rainbowhat as rh

rhtouch = rh.touch

def updateButtonLedState(led_a, led_b, led_c):
    try:

        led_a = ( 1 if led_a else 0 ) if isinstance(led_a, bool) else led_a

        led_b = ( 1 if led_b else 0 ) if isinstance(led_b, bool) else led_b

        led_c = ( 1 if led_c else 0 ) if isinstance(led_c, bool) else led_c

        rh.lights.rgb(led_a, led_b, led_c)

    except Exception as e:
        
        print str(e)
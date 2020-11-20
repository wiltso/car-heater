import RPi.GPIO as GPIO
in1 = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, False)

def turnOnHeater():
    """\
    turnOnHeater: turns on the heater
    """
    GPIO.output(in1, True)
    return "Heater is now on", True


def turnOffHeater():
    """\
    turnOffHeater: turns off the heater
    """
    GPIO.output(in1, False)
    return "Heater is now off", True


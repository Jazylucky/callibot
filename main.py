

def on_forever():
    pass
basic.forever(on_forever)

def check_line_l():
    if callibot.read_line_sensor(KSensor.LINKS, KSensorStatus.DUNKEL):
        rotate("right", 90)


def rotate(direction, angle):
    callibot.motor(KMotor.LINKS, KDir.VORWÄRTS, 0)


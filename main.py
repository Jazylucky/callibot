

def on_forever():
    pass
basic.forever(on_forever)

def check_line_l():
    if callibot.read_line_sensor(KSensor.LINKS, KSensorStatus.DUNKEL):
        rotate("right")
        callibot.motor(KMotor.BEIDE, KDir.VORWÄRTS, 100)
        basic.pause(200)
        rotate("left")


def rotate(direction):
    if direction == "right":
        callibot.motor(KMotor.LINKS, KDir.VORWÄRTS, 50)
    elif direction == "left":
        callibot.motor(KMotor.RECHTS, KDir.VORWÄRTS, 50)

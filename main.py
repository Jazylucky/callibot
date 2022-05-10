

def on_forever():
    pass
basic.forever(on_forever)

def tick():
    check_line()



def check_abs_vorne():
    if callibot.entfernung(KEinheit.CM) <= 20:
        

def check_line():
    if callibot.read_line_sensor(KSensor.LINKS, KSensorStatus.DUNKEL):
        rotate("right")
        callibot.motor(KMotor.BEIDE, KDir.VORWÄRTS, 100)
        basic.pause(200)
        rotate("left")
    if callibot.read_line_sensor(KSensor.RECHTS, KSensorStatus.DUNKEL):
        rotate("left")
        callibot.motor(KMotor.BEIDE, KDir.VORWÄRTS, 100)
        basic.pause(200)
        rotate("right")

def rotate(direction):
    if direction == "right":
        callibot.motor(KMotor.LINKS, KDir.VORWÄRTS, 50)
        basic.pause(500)
        callibot.motor_stop(KMotor.BEIDE, KStop.BREMSEN)
    elif direction == "left":
        callibot.motor(KMotor.RECHTS, KDir.VORWÄRTS, 50)
        basic.pause(500)
        callibot.motor_stop(KMotor.BEIDE, KStop.BREMSEN)

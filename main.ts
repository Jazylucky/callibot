basic.forever(function on_forever() {
    
})
function tick() {
    check_line()
}

function check_line() {
    if (callibot.readLineSensor(KSensor.links, KSensorStatus.dunkel)) {
        rotate("right")
        callibot.motor(KMotor.beide, KDir.vorwärts, 100)
        basic.pause(200)
        rotate("left")
    }
    
    if (callibot.readLineSensor(KSensor.rechts, KSensorStatus.dunkel)) {
        rotate("left")
        callibot.motor(KMotor.beide, KDir.vorwärts, 100)
        basic.pause(200)
        rotate("right")
    }
    
}

function rotate(direction: string) {
    if (direction == "right") {
        callibot.motor(KMotor.links, KDir.vorwärts, 50)
        basic.pause(500)
        callibot.motorStop(KMotor.beide, KStop.Bremsen)
    } else if (direction == "left") {
        callibot.motor(KMotor.rechts, KDir.vorwärts, 50)
        basic.pause(500)
        callibot.motorStop(KMotor.beide, KStop.Bremsen)
    }
    
}


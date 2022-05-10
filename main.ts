basic.forever(function on_forever() {
    
})
function check_line_l() {
    if (callibot.readLineSensor(KSensor.links, KSensorStatus.dunkel)) {
        rotate("right")
        callibot.motor(KMotor.beide, KDir.vorwärts, 100)
        basic.pause(200)
        rotate("left")
    }
    
}

function rotate(direction: string) {
    if (direction == "right") {
        callibot.motor(KMotor.links, KDir.vorwärts, 50)
    } else if (direction == "left") {
        callibot.motor(KMotor.rechts, KDir.vorwärts, 50)
    }
    
}


basic.forever(function on_forever() {
    
})
function check_line_l() {
    if (callibot.readLineSensor(KSensor.links, KSensorStatus.dunkel)) {
        rotate("right", 90)
    }
    
}

function rotate(direction: string, angle: number) {
    callibot.motor(KMotor.links, KDir.vorwärts, 0)
}


I2C_LCD1602.LcdInit(63)
let my_ds = DS1302.create(DigitalPin.P5, DigitalPin.P4, DigitalPin.P3)
my_ds.start()
let czas = "" + my_ds.getHour() + ":" + ("" + my_ds.getMinute()) + ":" + ("" + my_ds.getSecond())
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    my_ds.setHour(21)
    my_ds.setMinute(44)
    
})
basic.forever(function on_forever() {
    
    I2C_LCD1602.clear()
    czas = "" + my_ds.getHour() + ":" + ("" + my_ds.getMinute()) + ":" + ("" + my_ds.getSecond())
    I2C_LCD1602.ShowString(czas, 0, 0)
    pause(500)
    
})

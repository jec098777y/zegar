I2C_LCD1602.lcd_init(63)

my_ds = DS1302.create(DigitalPin.P5, DigitalPin.P4, DigitalPin.P3)
my_ds.start()
czas = str(my_ds.get_hour()) + ":" + str(my_ds.get_minute()) + ":" + str(my_ds.get_second())

    
    
 
    
def on_button_pressed_b():
    my_ds.set_hour(21)
    my_ds.set_minute(44)
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_forever():
    global czas
    I2C_LCD1602.clear()
    czas = str(my_ds.get_hour()) + ":" + str(my_ds.get_minute()) + ":" + str(my_ds.get_second())
    I2C_LCD1602.show_string(czas, 0, 0)
            
    pause(500)
    pass
basic.forever(on_forever)
    
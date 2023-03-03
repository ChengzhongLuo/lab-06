from grove_rgb_lcd import *
import time
import grovepi

# Connect the Grove Rotary Angle Sensor to analog port A0
potentiometer = 0

grovepi.pinMode(potentiometer,"INPUT")

# set I2C to use the hardware bus
grovepi.set_bus("RPI_1")

ultrasonic_ranger = 4


time.sleep(1)





# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = grovepi.analogRead(potentiometer)

        # Calculate voltage
        distance_threahold = round((float)(sensor_value) * 517 / 1023, 2)

        distance_measured = grovepi.ultrasonicRead(ultrasonic_ranger)

        if distance_threahold >= distance_measured:
        	setText(f"{distance_threahold} OBJ PRES\n{distance_measured}")
			setRGB(255,0,0)
			
		else:
        	setText(f"{distance_threahold}\n{distance_measured}")
			setRGB(0,255,0)



    except Exception as e:
        print ("Error:{}".format(e))
    
    time.sleep(0.1) # don't overload the i2c bus
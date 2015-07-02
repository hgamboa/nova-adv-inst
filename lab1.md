# Lab 1 - Setting up Arduino


## Starting steps

* Install arduino IDE at  https://www.arduino.cc/en/Main/Software
* Connect via USB cable (A-B usb cable) to your laptop
* Set connection on **tools** menu 
 * Check that **board** sub menu is "Arduino Uno"
 * Adjust **port** sub menu to the arduino comm port.

Macos: 
/dev/cu.usbmodemNNNN

Windows:

**WARNING**

__THE ARDUINO SHOULD NEVER RECEIVE VOLTAGE HIGHER THAN 5V. THIS WILL IRREPARABLLY DAMAGE THE BOARD.__

## Lab Goals

## Goal 1 - Blinking Led
* Run the code on the ide to run the blinkng code: **Blink**.

 * learn the following functions
```
> pinMode
> digitalWrite
```
## Goal 2 - Measuring 

* Read a value function with from an analog entry: **ReadAnalogVoltage**. 
* Validate the reading using the multimeter. 


 * learn the following functions:
```
> analogRead
> Serial.begin
> Serial.println
```

## Goal 3 - Deciding on threshold.

* Combine the previous two goals on a threshold detector
* Read an analog input and if higher than 3V turn on the led.
* Attention the amplitude should be lower than 5v (TO CHECK)

## Goal 4 - Dimming a light.
* Activate the PWM with a 1kHz function and to dim the led light. 
* Use the code example
* Verify on the osciloscope the PWM frequency and the width of the square wave. 
 
 * learn the following functions
```
> analogWrite
```

## Going deeper 
* Get to know the Atmega arquitecture: http://www.atmel.com/devices/atmega328p.aspx
* Check project done with arduino: 
 * http://www.makeuseof.com/tag/10-great-arduino-projects-for-beginners
 * https://startingelectronics.org/beginners/start-electronics-now/tut10-ten-arduino-projects-for-absolute-beginners/
 * http://www.instructables.com/id/Beginner-Arduino/
* You can used 123D circuits to simulate, program and test Arduino code: https://123d.circuits.io







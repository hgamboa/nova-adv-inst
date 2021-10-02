# Lab 5 - Setting up Arduino and Controlling Arduino from Raspberry Pi

## PART I - Setting up Arduino

## Pre lab requirements

* Install the [**Arduino Software (IDE)**](https://www.arduino.cc/en/software)


## Starting steps
1. Open the Arduino IDE
2. Connect via USB cable (A-B USB cable) to your laptop
3. Set connection on the **tools** menu
4. Check that the **board** sub menu is "Arduino Uno"
5. Adjust **port** sub menu to the Arduino COM port.

**WARNING**

__:warning: THE ARDUINO SHOULD NEVER RECEIVE VOLTAGE HIGHER THAN 5V. THIS WILL IRREPARABLLY DAMAGE THE BOARD.__

## Part I Goals

## Goal 1 - Blinking Led
1. Run the blinking code (**Blink**) on the IDE.
2. Learn the following functions:
```
> pinMode
> digitalWrite
```
Hint: Check out the Arduino [Blink](https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink) tutorial. 

## Goal 2 - Measuring
1. Read a value function from an analog entry: **ReadAnalogVoltage**.
2. Validate the reading using the multimeter.
3. Learn the following functions:

```
> analogRead
> Serial.begin
> Serial.println
```

Hint: Check out the Arduino [ReadAnalogVoltage](https://www.arduino.cc/en/Tutorial/BuiltInExamples/ReadAnalogVoltage) tutorial.

## Goal 3 - Deciding on threshold.

1. Combine the previous two goals on a threshold detector
2. Read an analog input and, if higher than 3V, turn on the LED.
 **Attention** the amplitude should be lower than 5V.

## Goal 4 - Dimming a light.
1. Activate the PWM with a 1kHz function to dim the LED light.
2. Use the code example
3. Verify on the oscilloscope the PWM frequency and the width of the square wave.
4. Learn the following functions:

```
> analogWrite
```

Hint: Check out the Arduino [Fade](https://www.arduino.cc/en/Tutorial/BuiltInExamples/Fade) tutorial.

## Going deeper
* Get to know the ATmega architecture: http://www.atmel.com/devices/atmega328p.aspx
* Check project done with arduino:
  * http://www.makeuseof.com/tag/10-great-arduino-projects-for-beginners
  * https://startingelectronics.org/beginners/start-electronics-now/tut10-ten-arduino-projects-for-absolute-beginners/
  * http://www.instructables.com/id/Beginner-Arduino/
* You can used 123D circuits to simulate, program and test Arduino code: https://123d.circuits.io





# Part II -  Python PyFirmata


## Initial Setup

### Setting up your Arduino for Firmata

1. On **File** menu: Select **Examples** -> **Firmata** -> **StandardFirmata**
2. **Verify** and **Upload** Standard Firmata code to the Arduino board

### Installing pyfirmata

1. Connect via SSH to the RPi
2. Set up your RPi with the pyFirmata library. Run the following commands:
```
> pi@raspberrypi~$ sudo apt-get install python-serial
> pi@raspberrypi~$ sudo pip install pyfirmata
```

### Find the Arduino port

1. Find out the port name for the USB interface used. Run this command in the terminal without Arduino plugged in:

```
> ls /dev/tty*
```

2. Plug in the Arduino to the Raspberry Pi with a USB cable 
3. Rerun the command. If a new name appears, then this is the name of your port.  Register it to be further used.

## Goal 1 - Connecting to an Arduino

1. Create a file `ex1.py` in `/home/pi/lab5` directory (or open an IPython console)
2. Import the Arduino and util classes from the pyfirmata module and create an object using the USB address you found in the previous step:

```python
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyUSB0') # example
```

## Goal 2 -  Blink a LED

1. Use digital pin 13, which is connected to an internal LED.
2. LED on pin 13 should blink 10 times (time ON = 1s and time OFF = 1s)
3. Close pyFirmata after it is done

Learn the following functions:
```
    >>> board.digital[pin_nr].write(pin_value) # set the pin values high or low (1 and 0, respectively)
    >>> board.pass_time(t) # Non-blocking time-out for t seconds
    >>> board.exit()
```

## Goal 3 - Controlling analog ports

1. To use analog ports, it is handy to start an iterator thread:

```python
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
```

2. Read an analog input on pin A0 and print the result repeatedly, for 2 minutes (sampling_rate = 10 Hz).

Learn the following functions:
```
    >>> time.time()
    >>> board.analog[0].read()
```

3. Save the data received from pin A0 in a file `data_analog.txt`.
4. The file should have 2 columns:
 - Column 1 - current time (s)
 - Column 2 - pin A0 data (V)

Learn the following functions:
```
    >>> file = open('data_analog.txt', 'w')
    >>> file.write()
    >>> file.close()
 ```

* Question: What is the maximum sampling rate you can use to acquire the signal?

## Goal 4 - Dimming a LED

1. Adapt the code from link 4 about dimming a LED
2. Define a digital pin as PWM
3. The time to reach the max/min of brightness should be 5 s
4. Number of steps to get to the max/min -> use STEPS = 10
5. The LED should be brightening and dimming repeatedly for 2 minutes

Learn the following functions:
```
    >>> digital_a0 = board.get_pin()
    >>> digital_a0.write()
```


## Links
* http://raspberrypi-aa.github.io/session3/firmata.html
* https://github.com/tino/pyFirmata/
* https://media.readthedocs.org/pdf/pyfirmata/latest/pyfirmata.pdf
* Dimming a LED: http://fabian-affolter.ch/blog/dimming-a-led-with-pyfirmata/

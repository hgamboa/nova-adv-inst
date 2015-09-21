# Lab 3/4 - Setting up Raspberry Pi

## PLUGGING IN YOUR RASPBERRY PI

* Before you plug anything into your Raspberry Pi, make sure that you have all the equipment listed bellow:
  - SD card
  - Display and connectivity cables
  - Keyboard and mouse
  - Power supply
  - Internet connection (via an ethernet cable or a wifi adapter)

  1. Begin by slotting your SD card into the SD card slot on the Raspberry Pi, which will only fit one way.
  2. Next, plug in your USB keyboard and Mouse into the USB slots on the Raspberry Pi.
  3. Make sure that your monitor or TV is turned on, and that you have selected the right input (e.g. HDMI 1, DVI, etc).
  4. Then connect your HDMI cable from your Raspberry Pi to your monitor or TV.
  5. To connect your Raspberry Pi to the internet, plug in an ethernet cable into the ethernet port next to the USB ports or
  plug in your Wireless nano USB Adapter into the USB slot. 
  6. Finally plug in the micro usb power supply. This action will turn on and boot your Raspberry Pi.

## LOGGING INTO YOUR RASPBERRY PI

* Your raspberry pi will start loading the Operating System (Raspbian).
* As this is the first time you have booted Raspbian, the Raspberry Pi Config Menu will apppear:
  - Using your keyboard to navigate through this menu, select "Internationalization options" -> "Change Timezone" and select
  your geographic location. 
* Then, select "Finish" and press Enter.
* You will return to the command line.



* Login prompt:
  username: pi
  password: raspberry
* After the command line prompt:

  > pi@raspberrypi~$ startx

  and press Enter.

## HELP

* If you have problems with keyboard configuration:
http://raspberrypi.stackexchange.com/questions/236/simple-keyboard-configuration

Use the command:

  > $ sudo dpkg-reconfigure keyboard-configuration

to reconfigure your keyboard. Choose "Portugues" for keyboard layout. Then , reboot.



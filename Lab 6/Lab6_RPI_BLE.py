#Lab6_RPI_BLE.py
#Sample program, to run in the RPI, to test BLE comunication with the M5Stick
#v100 - PV - AAI(23/24)

#!/usr/bin/env python3
import asyncio
import logging
import uuid
from aioconsole import ainput

from bleak import BleakScanner, BleakClient

# Enable debug output
# logging.basicConfig(level=logging.DEBUG)

#this is what identifies your M5Stick. Must be personalized
DEVICE_NAME = "m5-stack"
SERVICE_UUID = uuid.UUID("94039c15-338f-4297-9014-aaba7d760713")
CHAR_UUID = uuid.UUID("94039c15-338f-4297-9014-aaba7d760713")

#BLE Comunication loop
async def run(loop):
    print("Searching devices...")
    devices = await BleakScanner.discover()

    device = list(filter(lambda d: d.name == DEVICE_NAME, devices))
    if len(device) == 0:
        raise RuntimeError(f"Failed to find a device name '{DEVICE_NAME}'")

    address = device[0].address
    print(f"Connecting to the device... (address: {address})")
    flag = False
    while flag == False: 
     try:
      async with BleakClient(address, loop=loop) as client:
        flag = True
        print("Done")
        print("Message from the device...")
        value = await client.read_gatt_char(CHAR_UUID)
        print(value.decode())

        print("Sending message to the device...")
        message = bytearray(b"RPI ready")
        await client.write_gatt_char(CHAR_UUID, message, True)
        
        #receives the BLE data from the m5-stick
        def callback(sender, data):
            print(f"Received: {data}")

        print("Subscribing to characteristic changes...")
        await client.start_notify(CHAR_UUID, callback)

        #print("Waiting 60 seconds to receive data from the device...")
        #await asyncio.sleep(60)

        #waits for an input from user to end process
        result = await ainput('Press any key to exit')
        print("Disconnecting from device")
     except:
      print("Retrying ...")


#start BLE comunications loop
loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))

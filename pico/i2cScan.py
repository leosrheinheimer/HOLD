from machine import Pin, I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

scan = i2c.scan()


if len(scan) == 0: 
    print("nothing found")
else: 
    for address in scan:
        print(hex(address))
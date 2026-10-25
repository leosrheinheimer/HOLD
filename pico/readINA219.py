from machine import Pin, I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

bus = i2c.readfrom_mem(0x40,0x02,2,addrsize=8)

bus_list = list(bus)
reading_in_millivolts = ((bus_list[0]*256 + bus_list[1])//8)*4
reading_volts = reading_in_millivolts/1000

print(f'voltage: {reading_volts:.3f}')

shunt = i2c.readfrom_mem(0x40,0x01,2,addrsize=8)
shunt_list = list(shunt)
shunt_reading = (shunt_list[0]*256 + shunt_list[1])
if shunt_reading > 32767 : 
    shunt_reading -= 65536
shunt_volts = shunt_reading * (10**-5)
shunt_amps = shunt_volts/0.1 ##0.1 is the ohms
shunt_milliamps = shunt_amps*1000
print(f'shunt mA: {shunt_milliamps:.1f}')
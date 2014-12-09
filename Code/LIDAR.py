import time, serial

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)

packetposition = 0
while data:
	data = ord((ser.read()))
	if data == 250:
		print("start of packet")
		packetposition = 1
	if packetposition == 1
		multiplier = data
		packetposition = 2
	if packetposition = 3
	

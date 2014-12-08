import time, serial

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)

while True:
	data = (ser.read())
	print ord(data)

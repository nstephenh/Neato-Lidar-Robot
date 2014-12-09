import time, serial

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)
while t>10000:
	data = (ser.read())
	print ord(data)
	t= t+1 

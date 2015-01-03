import time, serial, math

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)


class LIDAR:
	def scan(self):
		packetposition = 90
		byteposition = 23
		done = 0
		start = 0
		lastdata = 0
		scandata = []
		while done == 0:
			rawdata = ser.read()
			data = ord(rawdata)
			if data == 250:
				byteposition = 0 # Shows the start of the packet
			if byteposition == 1:
				packetposition = data - 160 # sets the index for the particular packet
				if packetposition == 0:
					start = 1
			if start == 1:
				coordinate = None
				if byteposition == 4:
					lastdata = data
				elif byteposition == 5:
					coordinate = (self.readdegree(packetposition, 1, lastdata, data))
				elif byteposition == 8:
					lastdata = data
				elif byteposition == 9:
					coordinate = (self.readdegree(packetposition, 2, lastdata, data))
				elif byteposition == 10:
					lastdata = data
				elif byteposition == 11:
					coordinate = (self.readdegree(packetposition, 3, lastdata, data))
				elif byteposition == 16:
					lastdata = data
				elif byteposition == 17:
					coordinate = (self.readdegree(packetposition, 4, lastdata, data))
				elif  packetposition == 89 and byteposition == 21:
					done =	1
				if coordinate:
					scandata.append(coordinate)
			byteposition += 1
		return scandata
		
	def readdegree(self, scannumber, datanumber, data1, data2):
		angle = (scannumber * 4) + datanumber
		distance = data1 | (( data2 & 0x3f) << 8)
		if distance > 53:
			coordinate = [distance, angle]
			return coordinate
		elif angle < 0 or angle > 360:
			return [0,0]
		else:
			return [0, angle]
		


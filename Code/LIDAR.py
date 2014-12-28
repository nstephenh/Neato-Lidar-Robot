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
		while done == 0:
			rawdata = ser.read()
			data = ord(rawdata)
			lastdata = 0
			if data == 250:
				byteposition = 0 # Shows the start of the packet
			if byteposition == 1:
				packetposition = data - 160 # sets the index for the particular packet
				if packetposition == 0:
					start = 1
			if start == 1:
				if byteposition == 2 or byteposition == 3:
					# implement speed info here if necessary, for now were ignoring it
					speed = "fast"
				if byteposition == 4:
					lastdata = data
				if byteposition == 5:
					self.readdegree(packetposition, 1, lastdata, data)
				if byteposition == 8:
					lastdata = data
				if byteposition == 9:
					self.readdegree(packetposition, 2, lastdata, data)
				if byteposition == 10:
					lastdata = data
				if byteposition == 11:
					self.readdegree(packetposition, 3, lastdata, data)
				if byteposition == 16:
					lastdata = data
				if byteposition == 17:
					self.readdegree(packetposition, 4, lastdata, data)
				if  packetposition == 89 and byteposition == 21:
					done =	1
			byteposition += 1
		return True
		
	def readdegree(self, scannumber, datanumber, data1, data2):
		angle = scannumber * 4 + datanumber
		angle_rad = angle * math.pi / 180.0
		c = math.cos(angle_rad)
		s = -math.sin(angle_rad)
		distance = data1 | (( data2 & 0x3f) << 8)
		dist_x = distance*c
		dist_y = distance*s
		print (dist_x, dist_y)
		
lidar = LIDAR()
lidar.scan()

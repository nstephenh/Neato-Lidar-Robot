import time, serial, math

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)


class LIDAR:
	def scan(self):
		packetposition = 90
		byteposition = 0
		done = 0
		started = True
		scandata = []
		ser.flushInput()
		rawdata = 0
		while done == 0:
			rawdata = ser.read()
			if ord(rawdata) == 250:
				rawdata = ser.read()
				if ord(rawdata) >=160 and ord(rawdata) <= 249 :
					index = ord(rawdata)
					scandata = [ord(data) for data in (ser.read(20))]
					done = 1
		return [250] + [index] + scandata
			
	
	def checkscan(self, scandata):
		checksumdata = int(scandata[20]) + (int(scandata[21]) << 8)
		data = scandata[:21]
		if self.checksum(data) == checksumdata:
			print "valid data"
			return 0
		else:
			return 1
	def readdata(self, scan):
		for 
			
			
		
		
	def readdegree(self, scannumber, datanumber, data1, data2):
		angle = (scannumber * 4) + datanumber
		distance = data1 | (( data2 & 0x3f) << 8)
		if ((angle < 0) or (angle > 360)):
			return [0,0]
		elif distance > 53:
			coordinate = [distance, angle]
			return coordinate
		else:
			return [0, angle]
		
	def checksum(self, data):
		"""Compute and return the checksum as an int.
		data -- list of 20 bytes (as ints), in the order they arrived in.
		"""
		# group the data by word, little-endian
		data_list = []
		for t in range(10):
			data_list.append( data[2*t] + (data[2*t+1]<<8) )

		# compute the checksum on 32 bits
		chk32 = 0
		for d in data_list:
			chk32 = (chk32 << 1) + d

		# return a value wrapped around on 15bits, and truncated to still fit into 15 bits
		checksum = (chk32 & 0x7FFF) + ( chk32 >> 15 ) # wrap around to fit into 15 bits
		checksum = checksum & 0x7FFF # truncate to 15 bits
		return int(checksum)

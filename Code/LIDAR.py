import time, serial, math

print "Lidar Sensor Program by Noah Haskell"

port = "/dev/ttyACM0"
baud = 115200
ser = serial.Serial(port, baud)


class LIDAR:
	def readpacket(self):
		done = False
		packetdata = []
		rawdata = 0
		while done == False:
			rawdata = ser.read()
			if ord(rawdata) == 250:
				rawdata = ser.read()
				if ord(rawdata) >=160 and ord(rawdata) <= 249 :
					index = ord(rawdata)
					packetdata = [ord(data) for data in (ser.read(20))]
					done = True
					return [250] + [index] + packetdata
			
	
	def checkpacket(self, scandata):
		checksumdata = int(scandata[20]) + (int(scandata[21]) << 8)
		data = scandata[:21]
		if self.checksum(data) == checksumdata:
			return True
		else:
			return False
			
	def readscan(self):
		done = False
		started = False
		scandata = []
		ser.flushInput()
		while done == False:
			packet = self.readpacket()
			if self.checkpacket(packet):
				if packet[1] == 160:
					started = True
				if started == True:
					scannumber = packet[1] - 160
					scandata.append(self.readdegree(scannumber, 1, packet[4], packet[5]))
					scandata.append(self.readdegree(scannumber, 2, packet[8], packet[9]))
					scandata.append(self.readdegree(scannumber, 3, packet[12], packet[13]))
					scandata.append(self.readdegree(scannumber, 4, packet[16], packet[17]))
				if packet[1] == 249 and started == True:
					done == True
					return scandata
		
	def readdegree(self, scannumber, datanumber, data1, data2):
		angle = (scannumber * 4) + datanumber
		distance = data1 | (( data2 & 0x3f) << 8)
		if distance > 100:
			return [distance, angle]
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

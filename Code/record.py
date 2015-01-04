from LIDAR import LIDAR

lidar = LIDAR()
data = lidar.scan()
print data
print lidar.checkscan(data)
	

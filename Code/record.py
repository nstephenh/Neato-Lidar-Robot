from LIDAR import LIDAR

lidar = LIDAR()
data = lidar.readscan()
for coordinate in data:
	print coordinate[0], ",", coordinate[1]



from LIDAR import LIDAR
LIDAR = LIDAR()
from networktables import NetworkTable

#NetworkTable.setIPAddress("localhost")
NetworkTable.setTeam(900)
NetworkTable.setClientMode()
NetworkTable.initialize()

dashboard = NetworkTable.getTable('SmartDashboard')

while True:
	for data in LIDAR.readscan():
		degree = "deg" + str(data[1])
		dashboard.putNumber(degree, data[0])

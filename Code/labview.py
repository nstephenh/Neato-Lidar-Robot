from LIDAR import LIDAR
LIDAR = LIDAR()
from networktables import NetworkTable

ip = ""
NetworkTable.setIPAddress(ip)
NetworkTable.setClientMode()
NetworkTable.initialize()

dashboard = NetworkTable.getTable('SmartDashboard')

while True:
	dashboard.putArray(LIDAR.readscan())

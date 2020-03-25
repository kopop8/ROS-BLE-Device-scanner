# ROS-BLE-Device-scanner
Node that that scans for and publishes BLE devices
Tested with ROS Kinetic with Ubuntu 16.04 and Raspbian

## Install
Install pyblue with pip (Must be python 2.7)
```pip install pyblue```
Than download this package and put it in your catkin_ws/src
go to catkin_ws and build
``` catkin_make```

<b>!IMPORTANT You need to run this as root (with sudo) or you have to change your bluetooth permissions so your user can access bluetooth </b> 

## How to use
```roslaunch ble_device_scanner ble_scanner.launch```



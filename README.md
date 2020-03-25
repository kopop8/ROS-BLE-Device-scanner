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
After that you can listen to it using:
```rostopic echo ble_devices```

###Example output
```
devices: 
  - 
    rssi: "-68"
    addr: "4d:dd:35:af:a2:e8"
    data: 
      - 
        adtype: "3"
        description: "Complete 16b Services"
        value: "0000fe9f-0000-1000-8000-00805f9b34fb"
      - 
        adtype: "22"
        description: "16b Service Data"
        value: "9ffe025a535579743475695f75670000017110fdcc85"
      - 
        adtype: "255"
        description: "Manufacturer"
        value: "e0000202ca94ee8a"
  - 
    rssi: "-64"
    addr: "51:cd:2f:8f:64:4c"
    data: 
      - 
        adtype: "1"
        description: "Flags"
        value: "1a"
      - 
        adtype: "10"
        description: "Tx Power"
        value: "0c"
      - 
        adtype: "255"
        description: "Manufacturer"
        value: "4c0010064b1eaff9a9bb"
  - 
    rssi: "-69"
    addr: "59:73:a7:5d:12:68"
    data: 
      - 
        adtype: "1"
        description: "Flags"
        value: "1a"
      - 
        adtype: "10"
        description: "Tx Power"
        value: "0c"
      - 
        adtype: "255"
        description: "Manufacturer"
        value: "4c001005471cfe5900"
  - 
    rssi: "-56"
    addr: "0c:c8:d2:34:1b:c1"
    data: 
      - 
        adtype: "255"
        description: "Manufacturer"
        value: "060001092002614cbc4fb7b91fe9ae8c0141965120c6df27f94408e411"
---

```


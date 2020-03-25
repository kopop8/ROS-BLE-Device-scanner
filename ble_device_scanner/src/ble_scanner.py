#!/usr/bin/env python
import rospy
from bluepy.btle import Scanner, DefaultDelegate
from std_msgs.msg import String
from ble_device_scanner.msg import Device, Devices, DeviceTuple


def talker():
    pub = rospy.Publisher('ble_devices', Devices ,queue_size=10)
    rospy.init_node('ble_scanner', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        devices = scanner()
        pub.publish(devices)
        rate.sleep()
        
def scanner():
    scanner = Scanner()
    devices = scanner.scan(2.0)
    ble_devices = []
    for dev in devices:
        temp = Device()
        temp.addr = str(dev.addr)
        temp.rssi = str(dev.rssi)
        for (adtype, desc, value) in dev.getScanData():
            tempTuple = DeviceTuple()
            tempTuple.adtype = str(adtype)
            tempTuple.description = str(desc)
            tempTuple.value = str(value)
            temp.data.append(tempTuple)
        ble_devices.append(temp)
    return ble_devices

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
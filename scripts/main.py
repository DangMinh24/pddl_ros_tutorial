#!/usr/bin/python
import rospy
from std_msgs.msg import String
if __name__ == "__main__":
    rospy.init_node("node_0", anonymous=True)
    rospy.spin()

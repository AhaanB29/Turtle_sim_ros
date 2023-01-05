# !/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        cont="hello world %d" %i
        rospy.loginfo(cont)
        pub.publish(cont)
        rate.sleep()
        i+=1
if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


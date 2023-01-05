# !/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("21BAI1747_chat",String,queue_size=5)
    rospy.init_node("21BAI1747_talker",anonymous=True)
    rate=rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        cont = "This is from talker %s" %i
        rospy.loginfo(cont)
        pub.publish(cont)
        rate.sleep()
        i+=1
if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


    
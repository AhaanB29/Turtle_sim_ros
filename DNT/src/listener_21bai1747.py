# !/usr/bin/env python3
import rospy
from std_msgs.msg import String
def chat(msg):
    rospy.loginfo("I heard from "+rospy.get_caller_id()+" %s"%msg.data)
def listener():
    rospy.Subscriber("chatter",String,chat)
    rospy.init_node("21BAI1747_listener",anonymous=True)
    rospy.spin()
if __name__ == "__main__":
    listener()
# !/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
def chatter_callback(msg):
    print("My position is:",'(',msg.x,",",msg.y,")")
    print("Angular speed:",msg.angular_velocity)
    print("Theta",msg.theta)
def give_posn():
    rospy.init_node('posn',anonymous=True)
    rospy.Subscriber('/turtle1/pose',Pose,chatter_callback)
    rospy.spin()
if __name__=='__main__':
    give_posn()
# !/usr/bin/env python3
import rospy,math,time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move_turtle():
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=5)
    rospy.init_node("Turtle1_move",anonymous=True)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x= 0.1
        twist.linear.y= 0.2
        #twist.angular.z= 0.0
        pub.publish(twist)
        rate.sleep()

def move(obj,speed,dist,forward):
    message_obj = Twist()
    global x,y
    x0,y0 =x,y
    if forward:
        speed = abs(speed)
    else :
        speed = -abs(speed)
    
    loop_rate = rospy.Rate(1)
    while(True):
        distance_covered = math.sqrt(((x0-x)**2)+((y-y0)**2))
        klinear=0.5
        message_obj.linear.x= (dist-distance_covered)*klinear
        rospy.loginfo("Moving")
        obj.publish(message_obj)
        
        if(distance_covered >= dist):
            rospy.loginfo("Reached")
            break
    message_obj.linear.x=0.0
    obj.publish(message_obj)

def pose_callback(pose_msg):
    global x,y,yaw
    x= pose_msg.x
    y = pose_msg.y
    yaw = pose_msg.theta

def go_to_goal(obj,x_goal,y_goal):
    global x,y,yaw
    message = Twist()
    loop_rate = rospy.Rate(10)
    while 1:
        klinear = 0.4
        distance  = math.sqrt(((x_goal-x)**2)+((y-y_goal)**2))
        speedl = abs(distance)*klinear
        kangular = 4.0
        desired_ang=  math.atan2(y_goal-y,x_goal-x)
        speeda = (desired_ang-yaw)*kangular
        message.angular.z=speeda
        message.linear.x= speedl
        obj.publish(message)
        if(distance < 0.01):
            rospy.loginfo("Reached the goal")
            break
def turtle_twist(obj,angl_speed_deg,relative_angle,clock):
    message = Twist()
    speed = abs(math.radians(angl_speed_deg))
    if(clock):
        message.angular.z = speed
    else:
        message.angular.z = (-1)*speed
    loop_rate =rospy.Rate(100)
    t0 = rospy.Time.now().to_sec()
    while(True):
        obj.publish(message)
        t1 = rospy.Time.now().to_sec()
        curr_angle = (t1-t0)*angl_speed_deg
        if(curr_angle >= relative_angle):
            print("Posn reached")
            break
    message.angular.z = 0
    obj.publish(message)

def orientation(obj,speed_deg, rotate):
    relative = math.radians(rotate) - yaw
    if relative <0:
        clock = 0
    else:
        clock =1
    turtle_twist(obj,speed_deg,math.degrees(abs(relative)),clock)

def spiral(obj ,r,t):
    mesg = Twist()
    loop_rate = rospy.Rate(1)
    while (x<10.5 and y<10.5):
        mesg.linear.x = r
        mesg.linear.y=0
        mesg.linear.z=0
        mesg.angular.x=0
        mesg.angular.y =0
        mesg.angular.z = t
        r+=1
        obj.publish(mesg)
        loop_rate.sleep()
    mesg.linear.x =0
    mesg.angular.z=0
    obj.publish(mesg)

def turtle_clean(obj):
    msg = Pose()
    msg.x = 1
    msg.y = 1
    msg.theta = 0
    go_to_goal(obj,1,1)
    orientation(obj,30,math.radians(msg.theta))
    for i  in range(2):
        move(obj,5,1,1)
        turtle_twist(obj,30,90,1)
        move(obj,5,5,1)
        turtle_twist(obj,30,90,0)
        move(obj,5,1,1)
        turtle_twist(obj,30,90,0)
        move(obj,5,5,1)
        turtle_twist(obj,30,90,1)
        move(obj,5,1,1)


def turtle_square(obj):
    msg = Pose()

    go_to_goal(obj,5,4)
    orientation(obj,30,math.radians(msg.theta))
    for i  in range(4):
        move(obj,10,3,1)
        turtle_twist(obj,30,90,1)

def turtle_arc(obj):
    msg = Twist()
    turtle_twist(obj,20,120,1)
    move(obj,5,2,1)
    msg.linear.x =1.2
    msg.linear.y = 0.1
    msg.angular.z = -1.2
    x0,y0 = x,y
    while not rospy.is_shutdown():
        obj.publish(msg)
        distance_covered = math.sqrt(((x0-x)**2)+((y-y0)**2))
        if(distance_covered >= 0.5):
            break
    move(obj,5,1,1)
    obj.publish(msg)
if __name__=="__main__":
    try:
        rospy.init_node("Motion_pose",anonymous=True)
        pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        sub = rospy.Subscriber("/turtle1/pose",Pose,pose_callback)
        time.sleep(2)
       
        #move(pub,10,4,1)
        #turtle_twist(pub,35,270,1)
        #go_to_goal(pub,1.50,1.80)
        #orientation(pub,3000,36000)
        #spiral(pub,10,10)
        #turtle_square(pub)
        turtle_arc(pub)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")


        


    
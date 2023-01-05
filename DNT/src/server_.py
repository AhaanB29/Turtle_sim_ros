# ! usr/bin/env python3
from DNT.srv import AddTwoInt
from DNT.srv import AddTwoIntRequest
from DNT.srv import AddTwoIntResponse
import rospy,time

def handle_add(req):
    print("Requested : %d + %d "%(req.a,req.b))
    time.sleep(4)
    print("Returning: %d " %(req.a + req.b))
    sum_ints = AddTwoIntResponse(req.a + req.b)
    return sum_ints
def Server():
    rospy.init_node("Server_add",anonymous=True)
    rospy.Service("Add",AddTwoInt,handle_add)
    rospy.spin()

if __name__=="__main__":
    Server()
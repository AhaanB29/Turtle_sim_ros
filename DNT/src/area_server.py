# ! usr/bin/env python3
from DNT.srv import areacal
from DNT.srv import areacalRequest
from DNT.srv import areacalResponse
import rospy,time

def handle_area(req):
    print("Request (l,b): (%f,%f)"%(req.l,req.b))
    ar = areacalResponse(req.l*req.b)
    return ar
def server_area():
    rospy.init_node("server_area",anonymous=True)
    rospy.Service("Area",areacal,handle_area)
    rospy.spin()

if __name__ == "__main__":
    server_area()
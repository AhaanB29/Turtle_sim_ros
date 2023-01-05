# ! usr/bin/env python3
from DNT.srv import areacal
from DNT.srv import areacalRequest
from DNT.srv import areacalResponse
import rospy,time
import sys

def request_send(x,y):
    rospy.wait_for_service("Area")
    try:
        m= rospy.ServiceProxy("Area",areacal)
        resp = m(x,y)
        return resp.area
    except rospy.ServiceException:
        print("Connection Failed")
def usage():
    return
if __name__=="__main__":
    if(len(sys.argv)==3):
        l = float(sys.argv[1])
        b= float(sys.argv[2])
    else:
        print("%f [x,y]"%sys.argv[2])
        sys.exit(1)
    print("Requested: length =%f , breadth = %f "%(l,b))
    print("Area : %f" %(request_send(l,b)))

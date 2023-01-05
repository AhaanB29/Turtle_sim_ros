# ! usr/bin/env python3
from DNT.srv import AddTwoInt
from DNT.srv import AddTwoIntRequest
from DNT.srv import AddTwoIntResponse
import rospy,time
import sys

def client_mode(x,y):
    rospy.wait_for_service("Add")
    try:
        m = rospy.ServiceProxy("Add",AddTwoInt)
        resp = m(x,y)
        return resp.sum
    except rospy.ServiceException :
        print("Server connection failed: %s")
def usage():
    return
if __name__=="__main__":
    if  len(sys.argv)==3:
        x=int(sys.argv[1])
        y = int(sys.argv[2])

    else:
        print("%s [x,y]"%sys.argv[0])
        sys.exit(1)
    print("Requested %d + %d " %(x,y))
    s = client_mode(x,y)
    print("Response : %s + %s = %s "%(x,y,s))




import cv2
import rospy

class CameraNode():
    def __init__(self) -> None:
        rospy.init_node('camera')

        self.camera_pub = rospy.Publisher('')
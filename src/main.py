#!/home/python_envs/ros-melodic/bin/python3

import rospy
import cv2
from geometry_msgs.msg import Twist

class MainNode():
    def __init__(self):
        rospy.init_node('main')

        # Publisher for velocity
        self.vel_pub = rospy.Publisher('/estop/cmd_vel', Twist, queue_size=10)

        # State of the robot
        self.state = "default"

        # Latest camera frame
        self.ret = None
        self.frame = None

    def update_sensors(self):
        # Load camera frame into self.ret and self.frame
        pass

    def update_state(self):
        # Update self.state of the robot given the current state
        pass

    def update_control(self):
        # Use self.state and where the TRACKER marker is detected to determine
        # the twist message to send to the robot
        pass

    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            # Update sensor info from camera
            self.update_sensors()
            # Turn camera info into usable information
            #   which aruco markers were found and where the TRACKER marker
            #   is if it was found
            # Update state of the robot based on latest sensor info
            self.update_state()
            # Use the current state and current camera info to determine control
            self.update_control()

if __name__ == '__main__':
    main_node = MainNode()
    main_node.run()
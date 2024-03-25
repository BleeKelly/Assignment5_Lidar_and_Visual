#!/usr/bin/env python3

import rospy
import numpy as np
import math 
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
class TurtleBot:
    tuning_parameter = 0.3
    steering_speed = 0.3
    errorSignal_2 = 0
    errorSignal_1 = 0
    errorSignal = 0
    def __init__(self):#Initialization script
        rospy.init_node('wall_follower',anonymous=True)#Starts node called 'wall_follower'
        print("Created Node")
        self.lidar_data = rospy.Subscriber("/scan", LaserScan,callback=self.drive)#Subscriber object that listens for LaserScan type messages from "/scan". It will then use the percieve method to process the message
        print("Created Subscriber")
        self.turtle_bot_move = rospy.Publisher("/cmd_vel",Twist,queue_size=10)#Publisher object that publishes a Twist type message to "/cmd_vel" and has a queue buffer with size of 10
        print("Created Publisher")
        self.move_msg=Twist()
        self.time_one=rospy.Time.now().to_sec()
    def drive(self,lidar_data):
    def divsion(self):
        #Divide the front 180 degrees into 6 segments, with 3 semi circles
        self.far_left=Region(0,30)
        self.left=Region(30,60)
        self.front_left=Region(60,90)
        self.front_right=Region(90,120)
        self.right=Region(120,150)

    def evaluation(self,lidar_data):
    def decision(self):
    def motion_generation(self):
    def execute(self):

class Region:
    def __init__(self,min_angle,max_angle):
        
if __name__== '__main__':
    try:
        tb=TurtleBot()
        print("trying")
        rospy.spin()
    except rospy.ROSInterruptException:
        tb_stop=TurtleBot()
        tb_stop.stop()
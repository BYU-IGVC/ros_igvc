#!/usr/bin/env python

'''
This is the core ros module that external users will use to call ROS functions
Last Updated: 24 Jan 2019
Author: Isaac
'''

import rospy

class ROS_Handler(object):
    def __init__(self):
        rospy.init_node('test_server')
        s = rospy.Service('test_server', run_test, self.test)

    def test(self):
        print ('this is a test function')


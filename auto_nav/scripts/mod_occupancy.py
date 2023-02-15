#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid


def talker():
    pub = rospy.Publisher('maprewriter', OccupancyGrid, queue_size=1)
    rospy.init_node("map_rewrite")
    rate = rospy.Rate(2)
    print("Waiting for map")
    while not rospy.is_shutdown():
        data = rospy.wait_for_message('map', OccupancyGrid)
        rospy.loginfo("Map received")
        grid = list(data.data)
        rospy.loginfo("Map size: "+str(len(grid)))
        height = data.info.height
        width = data.info.width
        for i in range(height//2, 2 * (height//3)):
            for j in range(width//2, 2*(width//3)):
                index = 384 * i + j
                grid[index] = 100
        init_msg = OccupancyGrid()
        init_msg = data
        init_msg.data = tuple(grid)
        pub.publish(init_msg)
        rate.sleep()




if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
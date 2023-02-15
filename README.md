# TurtleBot3 Simulation Setup

# Steps

## Download TurtleBot3 packages

Use turtlebot3 [setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) website to install turtlebot3 package

## Download Turtlebot3 Simulation package
[Click here](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)


## Install dependencies
Install [AMCL](http://wiki.ros.org/amcl) package and [move_base](http://wiki.ros.org/move_base) package

## Clone Source code
Clone the above package into ~/catkin_ws/src and run ``` catkin_make ```

## Launch simulation

Run the following commands in different terminals

``` 
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

```
export TURTLEBOT3_MODEL=waffle
roslaunch auto_nav turtlebot3_auto_nav.launch

```

A Rviz window will open which can be used to set goal positions which the bot will try to navigate to.

For navigation using Stereo Camera only, install [RTabMap](http://wiki.ros.org/rtabmap_ros) and use the [tutorial](http://wiki.ros.org/rtabmap_ros/Tutorials/MappingAndNavigationOnTurtlebot) to perform navigation.


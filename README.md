# Distance-Monitor-Package
A distance monitor developed for Robot movement checking nodes, via ROS2 

# File Setup Guide : 
Create your ros2 workspace and put this src folder inside it

# Working and Useage : 

## distance_publisher.py 
distance_publisher.py is a Publisher Node, which randomly generates a fake distance value ranging from 0-150 cm, and publishes it in the topic name "distance".

## distance_subscriber.py 
distance_subscriber.py is a Subscriber Node, subscribed to the topic "distance". The recieved data is compared with the set parameters inside this file and accordingly output is logged, if it is safe for the robot to continue moving, or if it should move slowly or if it should stop.

## Launching
1) Open terminal inside your ros2 workspace
2) Build the workspace via 'colcon build --packages-select distance_monitor'
3) ource your terminal via 'source install/setup.bash'
4) Launch the launch file via 'ros2 launch distance_monitor distance_monitor_launch.launch.py'

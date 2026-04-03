from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='distance_monitor',
            executable='distance_publisher',
            name='distance_publisher',
            output='screen'
        ),
        Node(
            package='distance_monitor',
            executable='distance_subscriber',
            name='distance_subscriber',
            output='screen',
            parameters=[{
                'warning_distance': 80,
                'stop_distance': 40
            }]
        ),
    ])

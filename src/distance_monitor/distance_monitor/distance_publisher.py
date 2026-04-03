import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Distance_Publisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')       
        self.publisher_ = self.create_publisher(String, 'distance', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        dist = random.randint(0,150)
        msg = String()
        msg.data = str(dist)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data} cm' )


def main(args=None):
    rclpy.init(args=args)

    distance_publisher = Distance_Publisher()

    rclpy.spin(distance_publisher)

    distance_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


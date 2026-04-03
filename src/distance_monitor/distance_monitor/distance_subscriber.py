import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Distance_Subscriber(Node):

    def __init__(self):
        super().__init__('distance_subscriber')
        
        self.declare_parameter("warning_distance",80)
        self.declare_parameter("stop_distance",40)

        self.subscription = self.create_subscription(
            String,
            'distance',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
    	stop_dist = self.get_parameter("stop_distance").value
    	warn_dist = self.get_parameter("warning_distance").value
    	if(float(msg.data) < stop_dist):
    		self.get_logger().info(f'STOP : {msg.data} cm')
    	elif (float(msg.data) < warn_dist and float(msg.data) > stop_dist): 
    		self.get_logger().info(f'WARN : {msg.data} cm')
    	else:
    		self.get_logger().info(f'GOOD : {msg.data} cm')
        


def main(args=None):
    rclpy.init(args=args)

    distance_subscriber = Distance_Subscriber()

    rclpy.spin(distance_subscriber)

    distance_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

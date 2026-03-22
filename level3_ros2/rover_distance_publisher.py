import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class RoverDistancePublisher(Node):
    def __init__(self):
        super().__init__('rover_distance_publisher')
        self.publisher_ = self.create_publisher(Float64, 'rover_distance', 10)
        self.timer = self.create_timer(1.0, self.publish_distance)

    def publish_distance(self):
        distance = random.uniform(0.0, 100.0)
        msg = Float64()
        msg.data = distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing rover distance: {distance:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

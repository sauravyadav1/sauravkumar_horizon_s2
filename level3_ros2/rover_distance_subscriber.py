import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class RoverDistanceSubscriber(Node):
    def __init__(self):
        super().__init__('rover_distance_subscriber')
        self.subscription = self.create_subscription(
            Float64,
            'rover_distance',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received rover distance: {msg.data:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class RoverDistanceSubscriber(Node):
    def __init__(self):
        super().__init__('rover_distance_subscriber')
        self.subscription = self.create_subscription(
            Float64,
            'rover_distance',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received rover distance: {msg.data:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class RoverDistanceSubscriber(Node):
    def __init__(self):
        super().__init__('rover_distance_subscriber')
        self.subscription = self.create_subscription(
            Float64,
            'rover_distance',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received rover distance: {msg.data:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

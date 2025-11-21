import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


class PointSubscriber(Node):
    def __init__(self):
        super().__init__('point_subscriber')
        self.counter = 0
        self.subscription = self.create_subscription(
            Point,              
            'point_topic',      
            self.listener_callback, 
            10                  
        )

    def listener_callback(self, msg: Point):
        self.get_logger().info(
            f'Receiving Point #{self.counter}: x={msg.x:.2f}, y={msg.y:.2f}, z={msg.z:.2f}'
        )
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = PointSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

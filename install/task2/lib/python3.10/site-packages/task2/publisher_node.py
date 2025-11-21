import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


class PointPublisher(Node):
    def __init__(self):
        super().__init__('point_publisher')
        self.publisher_ = self.create_publisher(Point, 'point_topic', 10)
        self.counter = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        point = Point()
        point.x = random.uniform(-10.0, 10.0)
        point.y = random.uniform(-10.0, 10.0)
        point.z = random.uniform(-10.0, 10.0)

        self.get_logger().info(
            f'Publishing Point #{self.counter}: x={point.x:.2f}, y={point.y:.2f}, z={point.z:.2f}'
        )

        self.publisher_.publish(point)
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = PointPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

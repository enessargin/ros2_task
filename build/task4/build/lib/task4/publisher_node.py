
import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

SHAPES = ['circle', 'square', 'triangle', 'star', 'hexagon']
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']


class ColorShapePublisher(Node):
    def __init__(self):
        super().__init__('color_shape_publisher')
        self.publisher_ = self.create_publisher(String, 'shapes', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)

        payload = f'{shape}:{color}'
        msg = String()
        msg.data = payload

        self.get_logger().info(
            f'PUBLISH -> #{self.counter} shape={shape}, color={color}'
        )

        self.publisher_.publish(msg)
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = ColorShapePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

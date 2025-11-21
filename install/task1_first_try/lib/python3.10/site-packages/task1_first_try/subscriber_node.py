import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FirstTrySubscriber(Node):
    def __init__(self):
        super().__init__('first_try_subscriber')
        self.counter = 0
        self.subscription = self.create_subscription(
            String,
            'first_try',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg: String):
        self.get_logger().info(
            f'Receiving message #{self.counter} {msg.data}'
        )
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = FirstTrySubscriber()
    try:
        rclpy.spin(node)  
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

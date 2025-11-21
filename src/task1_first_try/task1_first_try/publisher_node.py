import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FirstTryPublisher(Node):
    def __init__(self):
        super().__init__('first_try_publisher')
        self.publisher_ = self.create_publisher(String, 'first_try', 10)
        self.counter = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello from publisher"
        self.get_logger().info(
            f'Publishing message #{self.counter} {msg.data}'
        )
        self.publisher_.publish(msg)
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = FirstTryPublisher()
    try:
        rclpy.spin(node)  
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

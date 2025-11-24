import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from example_interfaces.srv import Trigger  

class ColorShapeSubscriber(Node):
    def __init__(self):
        super().__init__('color_shape_subscriber')

        self.colors = ['red', 'green', 'blue', 'yellow', 'purple']
        self.color_index = 0
        self.target_color = self.colors[self.color_index]

        self.subscription = self.create_subscription(
            String,
            'shapes',
            self.listener_callback,
            10
        )

        self.srv = self.create_service(
            Trigger,              
            'next_color',         
            self.next_color_callback  
        )

        self.get_logger().info(
            f'Initial target color = "{self.target_color}". '
            f'Call /next_color service to change it.'
        )

    def listener_callback(self, msg: String):
      
        try:
            shape, color = msg.data.split(':')
        except ValueError:
            self.get_logger().warn(f'Bad message format: "{msg.data}"')
            return

        self.get_logger().info(
            f'RECV -> shape={shape}, color={color}'
        )

        if color == self.target_color:
            self.get_logger().info(
                f'*** DETECTED target color "{self.target_color}" -> shape={shape}'
            )

    def next_color_callback(self, request, response):

        self.color_index = (self.color_index + 1) % len(self.colors)
        self.target_color = self.colors[self.color_index]

        msg = f'Target color changed to "{self.target_color}"'
        self.get_logger().info(msg)

        response.success = True
        response.message = msg
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ColorShapeSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")

        self.sub_ = self.create_subscription(String, "chatter", self.msgCallback, 10)

    def msgCallback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")


def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

# add into setup.py into entry_points={'console_scripts': ... , 'simple_subscriber = percheron_py_examples.simple_subscriber:main'} 
# run ros2 run percheron_py_examples simple_subscriber
# run into another terminal: ros2 topic pub /chatter std_msgs/msg/String "data: 'Hello ROS 2'"

if __name__ == '__main__':
    main()
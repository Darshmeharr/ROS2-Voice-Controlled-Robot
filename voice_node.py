import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import speech_recognition as sr

class VoiceNode(Node):

    def __init__(self):
        super().__init__('voice_node')

        self.publisher_ = self.create_publisher(
            String,
            'voice_command',
            10
        )

        self.recognizer = sr.Recognizer()

        self.listen_loop()

    def listen_loop(self):

        while rclpy.ok():

            with sr.Microphone() as source:

                self.get_logger().info("Listening...")

                audio = self.recognizer.listen(source)

                try:
                    command = self.recognizer.recognize_google(audio)

                    msg = String()
                    msg.data = command.lower()

                    self.publisher_.publish(msg)

                    self.get_logger().info(
                        f"Published: {command}"
                    )

                except Exception:
                    self.get_logger().info(
                        "Could not understand audio"
                    )

def main(args=None):

    rclpy.init(args=args)

    node = VoiceNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()

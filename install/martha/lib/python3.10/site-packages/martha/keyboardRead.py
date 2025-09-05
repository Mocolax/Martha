import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import keyboard

class keyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_pub')
        self.publisher = self.create_publisher(String, 'teclas', 10)
        self.get_logger().info("Nodo Teclado Listo")
        
        # Temporizador para teclas
        self.timer = self.create_timer(0.1, self.check_keys)
        
        
    def check_keys(self):
        if keyboard.is_pressed('w'):
            self.publisher_.publish(String(data='w'))
        elif keyboard.is_pressed('s'):
            self.publisher_.publish(String(data='s'))
        elif keyboard.is_pressed('a'):
            self.publisher_.publish(String(data='a'))
        elif keyboard.is_pressed('d'):
            self.publisher_.publish(String(data='d'))

def main(args = None):
    rclpy.init(args = args)
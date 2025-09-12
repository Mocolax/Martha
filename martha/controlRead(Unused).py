import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from inputs import get_gamepad
from geometry_msgs.msg import Twist

class controlPublisher(Node):
    def __init__(self):
        super().__init__('control_pub')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.01, self.send)
        
        
        self.get_logger().info("Nodo control Listo")

    def send(self):
        velocidad_lineal = 0.0
        velocidad_angular = 0.0
        events = get_gamepad()
        
        for event in events:
            if event.code == 'ABS_Y': 
                velocidad_lineal = -event.state / 1.0
            elif event.code == 'ABS_X':
                velocidad_angular = event.state / 1.0
                
            msg = Twist()
            msg.linear.x = velocidad_lineal
            msg.angular.z = velocidad_angular
            
            self.publisher.publish(msg)
            self.get_logger().info(f"Mensaje: x={msg.linear.x:.2f},     z={msg.angular.z:.2f}")
            
    
def main(args = None):
    rclpy.init(args = args)
    nodo = controlPublisher()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
import time
import serial
import struct
import rclpy
from rclpy.node import Node

#julian puto

class movimiento(Node):
	def __init__(self):
		super().__init__('Movimiento')
		self.get_logger().info("Nodo Movimiento iniciado")

def main(args=None):
	with serial.Serial('/dev/ttyACM1', 115200, timeout=0.0025) as ser:
		while True:
			time.sleep(0.5)
			print('HOLA')
			message = struct.pack(
				'dddddd',
				0.0,      # x
				0.0,     # y
				0.0,    # z
				False,      # start_button
				False,       # back_button
				9912399
			)	
			ser.write(message)
   
if __name__ == '__main__':
    main()
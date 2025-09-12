import serial
import time
import rclpy
from rclpy import Node
import struct

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

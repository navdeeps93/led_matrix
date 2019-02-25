import asyncio
import ast
from websocket import create_connection

from led_display import *
UBUNTU_PATH = "/home/nav/Documents/led_matrix/led_socket_client/id.conf"
PI_PATH = "/home/pi/Documents/led_matrix/led_socket_client/id.conf"

#Websocket client
def ws_client():
	#initalize led matrix, need to move this to __main__
	screen_init()

	print("Begin websocket Client")
	socket = create_connection("ws://173.255.221.187:8080")
	print("Connected to Server..Sending Device ID")
	recv_data = socket.recv()
	print("This is what i recieved: ", recv_data)
	
	#Send device id
	id_hash_string = open(PI_PATH).read()
	id_hash = ast.literal_eval(id_hash_string)
	print("id hash", id_hash.items())
	id_hash_value = id_hash["id"]
	device_id_string = 'Device:' + str(id_hash_value)
	print("Deivce id string: ", device_id_string)
	socket.send(device_id_string)
	
	
	r = 0
	g = 0
	b = 0

	#loop and display points
	while True:
		print("Waiting for recv data")
		recv_data = socket.recv()


		rgb_array = recv_data.split(",")
		print("Rgb array: ", rgb_array)

		count = len(rgb_array)
		if (count == 3):
			x = int(rgb_array[0])
			y = int(rgb_array[1])
			hex_color = rgb_array[2]
			print("X coord: ", x)
			print("Y Coord: ", y)

			if (r >= 255 - 6):
				r = 0
			if (g >= 255 - 4):
				g = 0
			if (b >= 255 - 3):
				b = 0
				
			r = r + 6
			g = g + 3
			b = b + 4
			
			set_pixel(x,y,r,g,b)
			rgb_array = []
		else:
			print("Bad Data")



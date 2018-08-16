import asyncio
import websockets

#Websocket client
def ws_client():
	#initalize led matrix, need to move this to __main__
	screen_init()

	print("Begin websocket Client")
	socket = create_connection("ws://localhost:8080/websocket")
	socket.send("hi r u there")
	recv_data = websocket.recv()

	print("Connected to Server..Sending Device ID")

	#Send device id
	id_hash_string = open(PI_PATH).read()
	id_hash = ast.literal_eval(id_hash_string)
	device_id_string = 'device_id:' + str(id_hash["id"])
	socket.send(device_id_string.encode())



	#loop and display points
	while True:
		try:
			print("Waiting for recv data")
			recv_data = client_socket.recv(1024)

			format_recv_data = recv_data.decode("utf-8").rstrip()
			print("Recv Data is RGB Data: ", format_recv_data)

			rgb_array = format_recv_data.split(",")
			print("Rgb array: ", rgb_array)

			count = len(rgb_array)
			if (count == 3):
				x = int(rgb_array[0])
				y = int(rgb_array[1])
				hex_color = rgb_array[2]
				print("X coord: ", x)
				print("Y Coord: ", y)
				set_pixel(x,y,0,0,255)
				rgb_array = []
			else:
				print("Bad Data")
		except (TypeError, ValueError, OverflowError):
			print("Failed to recv shit?")





def socket_thread():
	global shared_rgb
	screen_init()
	SERVER_PORT = ('173.255.221.187', 3333)

	#Create ipv4 TCP socket 
	print ("Creating Socket")
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	global socket_connected
	socket_connected = 1

	#connect to a server
	while True:
		try:
			client_socket.connect(SERVER_PORT)
			print("Does this line run")
			break
		except (TypeError, ValueError, OverflowError):
			print("Failed to connect trying again...")
			time.sleep(1)

	print("Connected to Server...")
	#Send device id
	#read id file into hash
	id_hash_string = open("/home/pi/Documents/led_matrix/led_socket_client/id.conf").read()
	id_hash = ast.literal_eval(id_hash_string)
	print("Here is the Hash: ", id_hash.items())
	just_id = id_hash["id"]
	device_id_string = 'device_id:' + str(just_id)
	print("Here is device_id_string: ", device_id_string)
	client_socket.sendall(device_id_string.encode())
	#Time for the infinite loop
	while True:
		try:
			print("Waiting for recv data")
			recv_data = client_socket.recv(1024)
			print("Received RGB data: ", recv_data)

			if (recv_data == "change_mode"):
				print("Change Modes!!!!!")
			else:
				print("Raw what i get: ", recv_data)
				format_recv_data = recv_data.decode("utf-8").rstrip()
				print("Recv Data is RGB Data: ", format_recv_data)
				rgb_array = format_recv_data.split(",")
				print("Rgb array: ", rgb_array)
				count = len(rgb_array)
				if (count < 3):
					print("not enough commas")
				else:
					x = int(rgb_array[0])
					y = int(rgb_array[1])
					hex_color = rgb_array[2]
					print("X coord: ", x)
					print("Y Coord: ", y)
					set_pixel(x,y,0,0,255)
					rgb_array = []
		except (TypeError, ValueError, OverflowError):
			print("Failed to recv shit?")



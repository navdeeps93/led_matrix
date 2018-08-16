#Simple client socket to connect to Skylar's server
import socket
import sys
import time
import requests
import ast
from multiprocessing import Process, Value, Array
import random
from colors import rgb, hex

#custom imports
#need to add __init__.py to all sub directories
from rgb_examples.image_viewer import *

shared_rgb = []
socket_connected = 0

def provision(mac,  width, height):
	URL = "https://grid-draw.herokuapp.com/grids"

	data_hash = {"mac" : get_mac().rstrip(), "width" : width, "height" : height}
	print("Data: ", data_hash)

	#Post the data
	post_data = requests.post(URL, data_hash)
	print ("HTTP CODE: ", post_data)
	print ("What he say back: ", post_data.content)
	
	#Write content to file
	write_to_file("/home/pi/Documents/led_matrix/led_socket_client/id.conf", post_data.content.decode("utf-8"))


	#read id file into hash
	#id_hash_string = open("/home/pi/Documents/led_matrix/led_socket_client/id.conf").read()
	#id_hash = ast.literal_eval(id_hash_string)

	#print("Here is the Hash: ", id_hash.items())


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







def post_thread():
	print("In Post_Thread")










def RGB_thread():
	global shared_rgb
	print("In RGB_Thread")
	screen_init()

	while True:
		print("Shared RGB Array: ", shared_rgb)
		count = len(shared_rgb)
		if (count < 3):
			print("not enough commas")
		else:
			x = shared_rgb[0]
			y = shared_rgb[1]
			hex_color = shared_rgb[2]
			print("X coord: ", x)
			print("Y Coord: ", y)
			print("Hex Color: ", hex_color)
			time.sleep(7)
			rgb_tuple = tuple(hex(hex_color).rgb)
			if (rgb_tuple.count() == 1):
				set_pixel(x,y,rgb_tuple[0],rgb_tuple[1],brgb_tuple[2])
				#clear array, need to watch out if other thread can be fucked by this
				shared_rgb = []
			else:
				print("Tuple count is not righ!")







def get_mac(interface = 'eth0'):
	#Returns mac address of 'interface'
	try:
		mac = open("/sys/class/net/%s/address" %interface).read()
	except:
		mac = "00:00:00:00:00:00"
	return "mac=" + mac









def write_to_file(file_name, data):
	file = open(file_name, "w")
	file.write(data)
	file.close()


def socket_client():

	SERVER_PORT = ('173.255.221.187', 3003)

	#Create ipv4 TCP socket 
	print ("Creating Socket")
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	#connect to a server
	while True:	
		try:
			client_socket.connect(SERVER_PORT)
			break
		except (TypeError, ValueError, OverflowError):
			print("Failed to connect trying again...")
			time.sleep(1)


	print("Connected to Server...")
	print("Grabbing MAC Address...")

	mac_address = get_mac()
	print("Mac Address: ", mac_address)


	#Look for our first response
	while True:
		try:
			print("Sending MAC: ", mac_address)
			client_socket.sendall(mac_address.encode())
			device_id = client_socket.recv(1024)
			print("Received Device ID: ", device_id)
			return device_id
		except (TypeError, ValueError, OverflowError):
			print("Failed to send MAC Address, trying again...")



if __name__ == '__main__':
	global socket_connected
	socket_connected = 0
	provision(get_mac().rstrip(), "64", "32") #first boot
	print("Begin process")
	#screen_init() #TODO: remove this
	Process(target=socket_thread).start()
	
	time.sleep(5)
	#Process(target=post_thread).start()
	print("Wait for a bit, thens tart RGB Thread")
	time.sleep(5)
	#Process(target=RGB_thread).start()




	#display_image("emoji.png")
	
	#Process(target=socket_thread).start()
	#Process(target=post_thread).start()
	#Process(target=RGB_thread).start()

	#This function will wait for internet to begin
	#Check if this is first boot ever, or reboot
	#call provision or refresh depending on if reboot or restart
	#begin thread


#64 is col (x axis)
#32 is row (y axis)





#provision(get_mac().rstrip(), "64", "32") #first boot






#refresh for latest image from server

#refresh every few minutes



#data recieves will be x,y,hex value for color



#device_id = socket_client()
#write_to_file("id.conf", device_id)

#save this device_id to a file somewhere
#display it to a screen


#save the ID
#reporivison with MAC
#servers sends me back passcode
#pass code displayed on screen

#you send me a confirmation
#bada bing, appear a smiley face or something
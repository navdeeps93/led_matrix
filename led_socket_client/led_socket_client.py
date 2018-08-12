#Simple client socket to connect to Skylar's server
import socket
import sys
import time
import requests
import ast
from multiprocessing import Process, Value, Array






def provision(mac,  width, height):
	URL = "https://grid-draw.herokuapp.com/grids"

	data_hash = {"mac" : get_mac().rstrip(), "width" : width, "height" : height}
	print("Data: ", data_hash)

	#Post the data
	post_data = requests.post(URL, data_hash)
	print ("HTTP CODE: ", post_data)
	print ("What he say back: ", post_data.content)
	
	#Write content to file
	write_to_file("/Users/navdeep/Desktop/led_socket_client/id.conf", post_data.content.decode("utf-8"))


	#read id file into hash
	id_hash_string = open("/Users/navdeep/Desktop/led_socket_client/id.conf").read()
	id_hash = ast.literal_eval(id_hash_string)

	print("Here is the Hash: ", id_hash.items())


def socket_thread():
	SERVER_PORT = ('0.0.0.0', 21)

	#Create ipv4 TCP socket 
	print ("Creating Socket")
	client_socket = socket.socket(socket.AF_INET, .socketSOCK_STREAM)


	#connect to a server
	while True:	
		try:
			client_socket.connect(SERVER_PORT)
			break
		except (TypeError, ValueError, OverflowError):
			print("Failed to connect trying again...")
			time.sleep(1)

	print("Connected to Server...")

	#Time for the infinite loop
	while True:
		try:
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
				shared_rgb = Array(format_recv_data.split(","))
				print("Shared_RGB array: ", shared_rgb)
				time.sleep(1)

			#Write rgb data to buffer
		except (TypeError, ValueError, OverflowError):
			print("Failed to recv shit?")
			time.sleep(1)







def post_thread():
	print("In Post_Thread")










def RGB_thread():
	print("In RGB_Thread")
	While
	#not yet :^(





def get_mac(interface = 'enp0s3'):
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
	Process(target=socket_thread).start()
	#Process(target=post_thread).start()
	#Process(target=RGB_thread).start()

	#This function will wait for internet to begin
	#Check if this is first boot ever, or reboot
	#call provision or refresh depending on if reboot or restart
	#begin thread


#64 is col (x axis)
#32 is row (y axis)
provision(get_mac().rstrip(), "64", "32") #first boot

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
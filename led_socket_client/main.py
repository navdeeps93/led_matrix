import socket
import sys
import time
import requests
import ast
import random
from colors import rgb, hex
from multiprocessing import Process, Value, Array

#Imports from files
from led_display import *
from file_io import *

UBUNTU_PATH = "/home/nav/Documents/led_matrix/led_socket_client/id.conf"
PI_PATH = "/home/pi/Documents/led_matrix/led_socket_client/id.conf"


def checkKeyValuePairExistence(dic, key):
	try:
		return dic[key]
	except KeyError:
		return False


def provision(mac,  width, height):
	URL = "https://grid-draw.herokuapp.com/grids"

	data_hash = {"mac" : get_mac().rstrip(), "width" : width, "height" : height}
	print("Provision Data: ", data_hash)

	#Post the data
	post_data = requests.post(URL, data_hash)
	print ("HTTP CODE: ", post_data)
	print ("What he say back: ", post_data.content)

	#store post_data into hash
	id_hash = ast.literal_eval(post_data.content.decode("utf-8"))
	print("key_id hash: ", id_hash.items())

	#is this even necessary?
	#for i in id_hash:
	#	if ((checkKeyValuePairExistence(id_hash, i)) == False):
	#		print("There was a missing Value, need to try again"


	#Write content to file
	write_to_file(PI_PATH, id_hash)


	#display key on screen
	print("Displaying key on screen")
	screen_init()
	
	#loop here until we recieve ok from server, or make a thread that i can kill whenever
	display_text(str(id_hash["key"]))



if __name__ == '__main__':

	print("Begin Main")
	#Startup Routine
	provision(get_mac().rstrip(), "1", "1") #first boot



	#Start Websocket

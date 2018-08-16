def write_to_file(file_name, data):
	file = open(file_name, "w")
	file.write(str(data))
	file.close()


def get_mac(interface = 'eth0'):
	#Returns mac address of 'interface'
	try:
		mac = open("/sys/class/net/%s/address" %interface).read()
	except:
		mac = "00:00:00:00:00:00"
	return "mac=" + mac

#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image



global options

def screen_init():
        # Configuration for the matrix
	options = RGBMatrixOptions()
	options.rows = 32
	options.cols = 64
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
	options.brightness = 30
	options.show_refresh_rate=1
	global matrix
	matrix = RGBMatrix(options = options)

def set_pixel(x, y, r, g, b):
	print("In set_piexel")
	print("X coord: ", x)
	print("Y Coord: ", y)
	matrix.SetPixel(x, y, 100, 144, 255)



def display_image(image_file):
	print("hi")
	image = Image.open(image_file)

	# Configuration for the matrix
	options = RGBMatrixOptions()
	options.rows = 32
	options.cols = 64
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
	options.brightness = 30
	options.show_refresh_rate=1
	matrix = RGBMatrix(options = options)

	# Make image fit our screen.
	image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

	matrix.SetImage(image.convert('RGB'))

	try:
		print("Press CTRL-C to stop.")
		while True:
			time.sleep(100)
	except KeyboardInterrupt:
		sys.exit(0)

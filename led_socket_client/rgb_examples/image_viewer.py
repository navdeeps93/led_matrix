#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image


def display_image(image_file):
	print("hi")
	image = Image.open(image_file)

	# Configuration for the matrix
	options = RGBMatrixOptions()
	options.rows = 32
	options.cols = 64
	options.chain_length = 1
	options.parallel = 1
	options.hardware_mapping = 'adafuit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

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

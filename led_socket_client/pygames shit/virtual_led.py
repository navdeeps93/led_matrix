import pygame
import time
from random import randint
# Define the colors we will use in RGB format

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
color_array = [BLACK, WHITE, BLUE, GREEN, RED]




def init(cols, rows):
	global screen
	pygame.init()
	size = [cols, rows]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Virtual LED Matrix")
	pygame.display.toggle_fullscreen()


def draw_grid(square_size, cols, rows):

	for x in range(0, cols, square_size):
		for y in range(0, rows, square_size):
			print("X: ", x, "Y: ", y)
			squares = (x, y, square_size, square_size)
			pygame.draw.rect(screen, WHITE, squares, 1)
			pygame.display.flip()
	time.sleep(3)










def draw_line(x, y):
	i = 0
	row = 0
	col = 0
	switch = y
	color = GREEN
	while (i < x):
		pygame.draw.line(screen, color, [0, 0], [col,row], 2)
		pygame.display.flip()
		if (i % 32):
			color = color_array[randint(0, 3)]

		#continue downward
		col+=2

		#if reach half of line, continue upward
		if (i > (y/2)):
			row-=2
		else:
			row+=2
		i+=1

		time.sleep(0.00001)

init(600,300)
#draw_grid(square_size, num_of_sqaures_col, num_of_squares_rows)
draw_grid(20,64*10,32*10)









#draw_line(1000,1000)

#time.sleep(10)


#draw_line(700,700)
#draw_line(500, 500)
#draw_line(300,300)



#Draws a bunch of triangles big to small
'''
x = 0
r = 1000
c = 1000
while (x < 20):
	draw_line(r,c)
	r-=30
	c-=30
	x+=1
'''

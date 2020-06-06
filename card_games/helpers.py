import pygame

def track_mouse(x, y, width, height):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	x_end, y_end = (x + width, y + height)
	hovering = ( x <= mouse_x <= x_end and y <= mouse_y <= y_end )
	click_occured = pygame.mouse.get_pressed()[0] == 1
	clicked = (hovering and click_occured)

	return (hovering, clicked)

def get_location(x, y, w, h, border_x, border_y):
	x_start = x - border_x
	y_start = y - border_y
	width = w + ( 2 * border_x )
	height = h + ( 2 * border_y )

	return (x_start, y_start, width, height)



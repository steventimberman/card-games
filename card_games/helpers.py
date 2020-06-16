import pygame

def is_hovering(mouse_x, mouse_y, x, y, width, height):
	x_end, y_end = (x + width, y + height)
	hovering = ( x <= mouse_x <= x_end and y <= mouse_y <= y_end )
	return hovering


def get_location(x, y, w, h, border_x, border_y):
	x_start = x - border_x
	y_start = y - border_y
	width = w + ( 2 * border_x )
	height = h + ( 2 * border_y )

	return (x_start, y_start, width, height)

def check_type(var, expected_type, var_is_type=False):
	if type(var) != expected_type:
		raise Exception(f'Expected type {expected_type}, received {type(var)}')

def check_type_many(var, expected_type_list, var_is_type=False):
	var_type = var if var_is_type else type(var)
	if var_type not in expected_type_list:
		raise Exception(f'Expected one of these types: {expected_type_list}, received {type(var)}')


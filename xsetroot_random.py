#!/usr/bin/env python
# xsetroot_random.py
# Chooses a random X root-window bg color, either by name or hexcode. Requires xsetroot.

# Imports
import random
import argparse
import os
import io

# Functions
def readList(clist):
	if not os.access(clist, os.F_OK):
		print("ERROR: File does not exist!")
		exit()
	elif not os.access(clist, os.R_OK):
		print("ERROR: File is not readable!")
		exit()
	else:
		path=clist

	collist=io.open(clist, 'r')
	colors=[line.strip() for line in collist]
	collist.close()
	return colors


def pickCol(clist):
	if not args.hex:
		color=str(clist[random.randint(0, len(clist)-1)])
		return color
	else:
		color="#"
		for i in range(6):
			color+=str(random.randint(0,9))
		return color

# Arguments
parser = argparse.ArgumentParser(description="Chooses a random X root-window bg color, either by name or hexcode. Requires 'xsetroot'.")

parser.add_argument('-f', '--file', \
		default='included', \
		metavar='FILE', \
		help='read color names and/or hexcodes from FILE (format: one string per line)')
parser.add_argument('-x', '--hex', \
		action='store_true', \
		help='generate a random hexcode')

args=parser.parse_args()

# Execution
if __name__ == "__main__":
	if not args.hex:
		if args.file == "included":
			colors=['Alice Blue', 'Antique White', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanched Almond', 'Blue', 'Blue Violet', 'Brown', 'Burlywood', 'Cadet Blue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornsilk', 'Cyan', 'Dark Blue', 'Dark Cyan', 'Dark Goldenrod', 'Dark Gray', 'Dark Green', 'Dark Khaki', 'Dark Magenta', 'Dark Olive Green', 'Dark Orange', 'Dark Orchid', 'Dark Red', 'Dark Salmon', 'Dark Sea Green', 'Dark Slate Blue', 'Dark Slate Gray', 'Dark Turquoise', 'Dark Violet', 'Deep Pink', 'Deep Sky Blue', 'Dim Gray', 'Dodger Blue', 'Firebrick', 'Floral White', 'Forest Green', 'Gainsboro', 'Ghost White', 'Gold', 'Goldenrod', 'Gray', 'Green', 'Green Yellow', 'Honeydew', 'Hot Pink', 'Indian Red', 'Ivory', 'Khaki', 'Lavender', 'Lavender Blush', 'Lawn Green', 'Lemon Chiffon', 'Light Blue', 'Light Coral', 'Light Cyan', 'Light Goldenrod', 'Light Gray', 'Light Green', 'Light Pink', 'Light Salmon', 'Light Sea Green', 'Light Sky Blue', 'Light Slate Gray', 'Light Steel Blue', 'Light Yellow', 'Lime Green', 'Linen', 'Magenta', 'Maroon', 'Medium Aquamarine', 'Medium Blue', 'Medium Orchid', 'Medium Purple', 'Medium Sea Green', 'Medium Slate Blue', 'Medium Spring Green', 'Medium Turquoise', 'Medium Violet Red', 'Midnight Blue', 'Mint Cream', 'Misty Rose', 'Moccasin', 'Navajo White', 'Navy', 'Old Lace', 'Olive Drab', 'Orange', 'Orange Red', 'Orchid', 'Pale Goldenrod', 'Pale Green', 'Pale Turquoise', 'Pale Violet Red', 'Papaya Whip', 'Peach Puff', 'Peru', 'Pink', 'Plum', 'Powder Blue', 'Purple', 'Red', 'Rosy Brown', 'Royal Blue', 'Saddle Brown', 'Salmon', 'Sandy Brown', 'Sea Green', 'Seashell', 'Sienna', 'Sky Blue', 'Slate Blue', 'Slate Gray', 'Snow', 'Spring Green', 'Steel Blue', 'Tan', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'White Smoke', 'Yellow', 'Yellow Green']
		else:
			colors=readList(args.file)
	else:
		colors=[]

	color=str(pickCol(colors))
	print(color)
	os.system("xsetroot -solid '%s'" % color)

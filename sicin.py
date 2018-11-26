#!/usr/bin/python
#
# usage: sicin.py [-h] <FILE>
#
# Input handler for sic. (http://tools.suckless.org/sic)
# It provides line editing and a history buffer.
# The prompt shows the default channel/user.
# An empty prompt means it's the host.
# Usage example:
#   $ tail -f FILE | sic
#   $ sicin.py FILE
# Quit with ':q'
# 
# positional arguments:
#   <FILE>      File that is piped into sic.
# 
# optional arguments:
#   -h, --help  show this help message and exit
 
# Imports
import argparse
import readline

# Parse Arguments
parser = argparse.ArgumentParser(prog='sicin.py',\
formatter_class=argparse.RawDescriptionHelpFormatter,\
description='Input handler for sic. (http://tools.suckless.org/sic)\n\
It provides line editing and a history buffer.\n\
The prompt shows the default channel/user.\n\
An empty prompt means it\'s the host.\n\
Usage example:\n  \
$ tail -f FILE | sic\n  \
$ sicin.py FILE\n\
Quit with \':q\'')

parser.add_argument('afile', nargs=1, help='File that is piped into sic.', metavar='<FILE>', type=str)

args = parser.parse_args()

# Default Prompt is empty
prompt=''

# Try to read the file to find current default channel/user
try:
	with open("%s" % args.afile[0], "r") as rf:
		lines = rf.readlines()
	for l in lines:
		if ':s' in l:
			prompt = l.split()[1].rstrip('\n')
except IOError:
	pass

# Main Loop
while True:
	line = raw_input(prompt + '> ')
	if line.startswith(':s'):
		prompt=line.split()[1].rstrip('\n')
	if line == ':q':
		exit()
	with open("%s" % args.afile[0], "a") as af:
		af.write(line + '\n')

#!/usr/bin/env python

import argparse
import os
import os.path
import shutil
import re

def ParseArgs() :
	parser = argparse.ArgumentParser(description='Delete folders based on a regular expression.')

	parser.add_argument('-q', '--quiet', action="store_true", help="Delete folders without confirmation.")
	parser.add_argument('regex', type=str, help="Regular expression for the folders to delete.")

	args = parser.parse_args()

	return args

def Run() :
	args = ParseArgs()

	regex = args.regex
	if not str.startswith(regex, '^') :
		regex = '^' + regex
	if not str.endswith(regex, '$') :
		regex = regex + '$'

	current_directory = os.getcwd()
	dir_list = [dir for dir in os.listdir(current_directory) if os.path.isdir(dir)]

	dirs_to_remove = [dir for dir in dir_list if re.match(regex, dir, re.IGNORECASE)]

	execute_action = True

	if not args.quiet :
		print "You are going to delete these folders :"
		for dir in dirs_to_remove :
			print dir
		accepted = raw_input('Do you accept (y/N): ')
		if accepted != 'y' :
			execute_action = False

	if execute_action :
		for dir in dirs_to_remove :
			shutil.rmtree(dir)

if __name__ == "__main__" :
	Run()
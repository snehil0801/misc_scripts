from os import walk
from os import path
import sys
all_arg=len(sys.argv)
if all_arg != 2:
	print('ERROR: Currently script can search only one kind of files at once')
	sys.exit(255)
file_to_find=sys.argv[1]
if file_to_find in (['h','help']):
	print('find_any_file.py <type of file[keyword/extention etc.]>')
	sys.exit(0)

for root,dirs,files in walk(".", topdown=True):
	for names in files:
		if file_to_find in names: 
			print(path.join(root,names))

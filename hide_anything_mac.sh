#!/bin/bash

#Script take name of file or Directory that you want to hide,
#Provided path of Directory should be absolute
#Otherwise script will throw an error while execution

DIR_OR_FILE=$1

if [ -d "$DIR_OR_FILE" ]
then
	echo "Passed is Directory"
elif [ -f "$DIR_OR_FILE" ]
then
	echo "Passed is a file"
else
	echo "ERROR: Not able to find file or directory"
	exit 255
fi
IFS=''
#Hiding the passed file or directory
echo "Going to Hide $DIR_OR_FILE"
mv $DIR_OR_FILE .$DIR_OR_FILE

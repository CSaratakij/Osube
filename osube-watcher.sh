#!/bin/bash

IFS=$'\n'

if [ "$1" == "-h" ]
then
	echo "------------------------------"
	echo "   Osube file watcher   "
	echo "------------------------------"
	echo "Usage: osube-watcher [-h] A B"
	echo ""
	echo "A 	watching directory"
	echo "B 	extract osu! beatmap directory"
	echo ""
	echo "------------------------------"
	echo "OPTIONAL"
	echo "-h	Print help"
	echo ""
	echo "------------------------------"
	echo "Example"
	echo "osube-watcher ~/Download ~/BeatmapDir"
	echo ""
	echo "** If not passing a watching dir, current working directory will be use."
	echo "** If not passing an extract dir, environment var 'OSU_BEATMAP_SONGDIR' will be use"

	echo "------------------------------"
	exit
fi

WATCH_DIR="$1"
EXTRACT_DIR="$2"

# Check the watching directory
if [ -z $WATCH_DIR ]
then
	WATCH_DIR=$PWD
elif [ ! -d $WATCH_DIR ]
then
	echo "Error : Directory $WATCH_DIR does not exists."
	exit -1
fi

# Check the extract directory
if [ -z $EXTRACT_DIR ]
then
	if [ -z $OSU_BEATMAP_SONGDIR ]
	then
		echo "You need to specify extract directory\nUse -h for help"
		echo "You can use environment var 'OSU_BEATMAP_SONGDIR' to specify extract directory instead of passing the argument"
		exit -1
	fi

	EXTRACT_DIR=$OSU_BEATMAP_SONGDIR

elif [ ! -d $EXTRACT_DIR ]
then
	echo "Error : Directory $EXTRACT_DIR does not exists."
	exit -1
fi

echo "Watching dir : $WATCH_DIR"
echo "Extract dir : $EXTRACT_DIR"

# Run Watcher
inotifywait -m -q -e moved_to --format '%f' "$WATCH_DIR" | grep --line-buffered -o "^[0-9].*.osz" | while read -r MAP; do osube "$WATCH_DIR/$MAP" $EXTRACT_DIR; done


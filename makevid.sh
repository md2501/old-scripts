#!/bin/bash
# Creates a video from a picture and an audio file
# Usage ./makevid.sh picture audio [output.mp4]

if [ ! $# == 2 ] && [ ! $# == 3 ]; then
	echo -e "Creates a video from a picture and an audio file (Requires avconv) \n \
 Usage: ./$(basename $0) picture audio [output.mp4]"
	exit 1
fi

pic=$1
aud=$2
out=${3-output.mp4}
dur=$(avconv -i $aud 2>&1 | grep Duration | cut -f1 -d, | cut -f2,3,4,5 -d: | tr -d [:blank:])

	ffmpeg -loop 1 -i $pic -i $aud -t $dur -vcodec mpeg4 -acodec copy -f avi $out

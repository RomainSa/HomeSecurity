#!/bin/bash

PHOTO_NB=1

while true
  do
  DATE=$(date +"%u")
  if [ $PHOTO_NB = 1 ]
  then
    rm snap_"$DATE"*.jpg
  fi
  raspistill --width 1280 --height 960 --quality 100 -o /home/pi/camera/snap_"$DATE"_"$PHOTO_NB".jpg
  /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/camera/snap_"$DATE"_"$PHOTO_NB".jpg /
  ((PHOTO_NB++))
done


#!/bin/bash

MP3PATH="/media/FreeAgent_Drive/mp3s"

docker rm pythonjukebox
docker run --name pythonjukebox -d -v $MP3PATH:/media/FreeAgent_Drive/mp3s -p 5555:5555 --restart=on-failure pythonjukebox

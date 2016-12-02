#!/bin/bash

ip=$1
echo "The Raspberry Pi ip address is: $ip";

mkdir tempDirForPicTransfer

args=$#
for (( i=2; i<=$args; i+=1))
do
    if [ -d "${!i}" ]; then
        cp -r ${!i} tempDirForPicTransfer
    elif [ -f ${!i} ]; then
        cp ${!i} tempDirForPicTransfer
    else
        echo "${!i} is not a valid path!!! oops"
    fi
done

scp -r tempDirForPicTransfer/. pi@$ip:~/picturesForAlbum
rm -rf tempDirForPicTransfer

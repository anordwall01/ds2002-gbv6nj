#!/usr/bin/bash

#this is a script which retrives a url, puts in into a bucket and has 
#the bucket expire at a given time

#this takes three arguments, a url, a bucket and a time

set -e

URL=$1

BUCKET=$2

TIME=$3

echo "fetching image!"

curl "$URL" > image.jpg || exit 1

echo "image fetched!"


echo "uploading to bucket!"

aws s3 cp image.jpg s3://"$BUCKET"/ || exit 1

echo "uploaded to bucket"


echo "creating temporary link..."

IMAGE_URL=$(aws s3 presign --expires-in "$TIME" s3://"$BUCKET"/image.jpg)

echo "the link is: $IMAGE_URL"

echo "this link will expire in $TIME seconds"



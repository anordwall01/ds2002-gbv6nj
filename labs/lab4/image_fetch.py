#!/usr/bin/python3

import boto3
import requests
import os

s3 = boto3.client('s3')

#fetch file from internet
def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")


image_url = "https://darlingjadore.com/wp-content/uploads/2020/04/IMG_0985-1-scaled.jpg"
file = "downloaded_image.jpg"
path = os.path.join(os.getcwd(), file) # Saves to current directory

download_file(image_url, path)


#upload file to bucket
def upload_file(file_name, bucket, object_name):
        response = s3.upload_file(file_name, bucket, object_name)
        print(response)
        return True

upload_file("downloaded_image.jpg","ds2002-gbv6nj","image-UPLOADED.jpg")

#create link
bucket_name = "ds2002-gbv6nj"
object_name = "image-UPLOADED.jpg"
expires_in = 6870

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

 print(f"URL: {response}")

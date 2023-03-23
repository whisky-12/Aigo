# math_utils.py

from minio import Minio
from minio.error import InvalidResponseError
import os


class MathUtils:

    @staticmethod
    def upload_image(object_name, image_path):
        minio_server_url = 'oss-dev.flydiysz.cn'
        # Set up client object
        minioClient = Minio(minio_server_url,
                            access_key='admin',
                            secret_key='WlwCy9Gp4FGbjqbq',
                            secure=True)

        # Set up bucket name and image path
        bucket_name = 'ai-image'

        if not minioClient.bucket_exists(bucket_name):
            minioClient.make_bucket(bucket_name)

        try:
            with open(image_path, 'rb') as file_data:
                file_stat = os.stat(image_path)
                # upload image
                minioClient.put_object(bucket_name, object_name, file_data, file_stat.st_size)
                print("Image uploaded successfully.")
                return "https://"+minio_server_url+"/"+bucket_name+"/"+object_name+"";

        except InvalidResponseError as err:
            print(err)

def main():
    # object_name需要更改
    image_path = 'C:\\Users\\sang\\Desktop\\image.jpg'
    object_name = 'image.jpg'
    imageurl = MathUtils.upload_image(object_name,image_path);
    print(imageurl)

if __name__ == '__main__':
    main()

import os
import urllib.request
import time


class DownloadUtils:
    def download_image(imageUrl,intPut):
        # currentPath = os.getcwd().replace('\\', '/')
        # filePath = ''
        fileName = intPut + str(time.time()).split(".")[0] + ".png"

        try:
            urllib.request.urlretrieve(imageUrl, filename=fileName)
        except IOError as e:
            print("IOE ERROR"+e)
        except Exception as e:
            print("Exception")
        return fileName

# url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2Fdb28650f-c776-4ba8-9891" \
#       "-81d9396ebc99%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size" \
#       "=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1681553421&t=ecd90633c017d10a6aaafc180b7d79ec"
# # filepath =MathUtils.upload_image(url)
# path = DownloadUtils.download_image(url)
# print(path)

import os
import argparse
import platform
import logging
import cv2
import paddlehub as hub
import time

from fuc.algorithm.util.downloadimage import DownloadUtils
from fuc.algorithm.util.uploadimage import MathUtils

# 配置日志参数
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] ==> %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

# 查看系统类型
platform_ = platform.system()
is_win = is_linux = is_mac = False

if platform_ == "Windows":
    is_win = True
elif platform_ == "Linux":
    is_linux = True
elif platform_ == "Darwin":
    is_mac = True


# 判断系统是否更换下编码输出
def encode_str_by_sys(content):
    if is_linux or is_mac:
        return content
    elif is_win:
        return content.decode('utf-8').encode('gbk')
    else:
        return content


arg = argparse.ArgumentParser("This is an algorithm script!")


def U2Net_Portrait(content_imagePath):
    # 检测路径是否为空
    if not content_imagePath:
        logging.error(encode_str_by_sys("Image path may be empty"))
        return -1
    else:
        intput_path = "fuc/algorithm/feature/Image2Image/Quick_Sketch/intput/"
        content_imagePath = DownloadUtils.download_image(content_imagePath,intput_path)

    module = hub.Module(name='U2Net_Portrait')
    # 检测模型是否为空
    if not module:
        logging.error(encode_str_by_sys("Model loading failed"))
        return -1

    try:
        images = [cv2.imread(content_imagePath)]
    except:
        logging.error(encode_str_by_sys("Can not read this image !"))
        return -1
    print("开始处理")
    results = module.Portrait_GEN(
        images=images,
        face_detection=False
    )
    print("处理结束")
    if not results:
        logging.error(encode_str_by_sys("No target information detected"))
        return -1
    output_dir = "fuc/algorithm/feature/Image2Image/Quick_Sketch/output/"
    timeMask = str(time.time()).split(".")[0]
    output_file = output_dir + timeMask + ".png"
    cv2.imwrite(output_file, results[0])
    uploadUrl = MathUtils.upload_image(timeMask + ".png", output_file)

    path = "fuc/algorithm/feature/Image2Image/Quick_Sketch/intput/"
    # 删除缓存intput图片
    files = os.listdir(path)
    for pic in files:  # 遍历文件夹
        if pic.endswith(".png"):
            os.remove(path + '/' + pic)
        elif pic.endswith(".jpg"):
            os.remove(path + '/' + pic)
    # 删除缓存output图片
    path = "fuc/algorithm/feature/Image2Image/Quick_Sketch/output/"
    files = os.listdir(path)
    for pic in files:  # 遍历文件夹
        if pic.endswith(".png"):
            os.remove(path + '/' + pic)
        elif pic.endswith(".jpg"):
            os.remove(path + '/' + pic)

    return uploadUrl


# 主函数
def main(args):
    # 当前脚本的路径
    script_path = os.getcwd()
    # 判断系统执行相应的脚本
    if is_linux or is_mac:
        # 打印参数
        print(args.imagePath)

        # TODO 写你的算法函数
        res = U2Net_Portrait(args.imagePath)
        # 下载
        # 处理
        # 返回结果
        print(res)
        return res
    elif is_win:
        # TODO 写你的算法函数
        res = U2Net_Portrait(args.imagePath)
        # 下载
        # 处理
        # 返回结果
        print("########打印预测结果###########")
        print(res)
        print("########打印结束###########")
        return res
        pass
    else:
        logging.error(encode_str_by_sys("Unable to execute this script because of unknown system type！！！！！！！"))
    # 回到原来的路径下
    os.chdir(script_path)


if __name__ == '__main__':
    arg.add_argument("--imagePath", type=str, default='NONE',
                     help="Here is a network path, and the incoming "
                          "value is an content_image address.")

    args = arg.parse_args()
    main(args)

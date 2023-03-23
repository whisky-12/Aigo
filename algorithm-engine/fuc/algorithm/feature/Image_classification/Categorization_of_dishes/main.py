import os
import argparse
import platform
import logging
import sys
import cv2
import paddlehub as hub

sys.path.append("D:\\AI-3\\new\\algorithm-engine")

from fuc.algorithm.util.downloadimage import DownloadUtils

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


def mobilenet_v2_dishes(ImagePath, top_k):
    # 检测路径是否为空
    if not ImagePath:
        logging.error(encode_str_by_sys("Image path may be empty"))
        return -1
    else:
        intput_path = "fuc/algorithm/feature/Image_classification/Categorization_of_dishes/intput/"
        InPutImagePath = DownloadUtils.download_image(ImagePath,intput_path)

    module = hub.Module(name='mobilenet_v2_dishes')
    # 检测模型是否为空
    if not module:
        logging.error(encode_str_by_sys("Model loading failed"))
        return -1

    try:
        print(InPutImagePath)
        images = [cv2.imread(InPutImagePath)]
    except:
        logging.error(encode_str_by_sys("Can not read this image !"))
        return -1

    # 返回预测结果
    top_k = int(top_k)
    results = module.classification(images=images,top_k=top_k)
    if not results:
        logging.error(encode_str_by_sys("No target information detected"))
        return -1
    # 删除缓存input图片
    path = "fuc/algorithm/feature/Image_classification/Categorization_of_dishes/intput/"
    files = os.listdir(path)
    for pic in files:  # 遍历文件夹
        if pic.endswith(".png"):
            os.remove(path + '/' + pic)
        elif pic.endswith(".jpg"):
            os.remove(path + '/' + pic)
    return results


# 主函数
def main(args):
    # 当前脚本的路径
    script_path = os.getcwd()
    # 判断系统执行相应的脚本
    if is_linux or is_mac:
        # 打印参数
        print(args.imagePath)

        # TODO 写你的算法函数
        res = mobilenet_v2_dishes(args.imagePath, args.top_k)
        # 下载
        # 处理
        # 返回结果
        print(res)
        return res
    elif is_win:
        # TODO 写你的算法函数
        res = mobilenet_v2_dishes(args.imagePath, args.top_k)
        # 下载
        # 处理
        # 返回结果
        print("########打印预测结果###########")
        print(res)
        print("########打印结束###########")
        return res
    else:
        logging.error(encode_str_by_sys("Unable to execute this script because of unknown system type！！！！！！！"))
    # 回到原来的路径下
    os.chdir(script_path)
    print(script_path)
    # path = 'intput'  # 添加自己的相对路径
    # files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # print(files[0:10])  # 看一看文件都有啥


if __name__ == '__main__':
    arg.add_argument("--imagePath", "-e", type=str, default='NONE', help="Here is a network path, and the incoming "
                                                                         "value is an image address.")
    arg.add_argument("--top_k", type=int, default=1, help="Fill in the maximum number of objects in the "
                                                          "prediction screen here")
    args = arg.parse_args()
    main(args)

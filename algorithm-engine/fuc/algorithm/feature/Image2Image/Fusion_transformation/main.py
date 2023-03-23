import os
import argparse
import platform
import logging
import cv2
import paddlehub as hub

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


def stylepro_artistic(content_imagePath, styles_imagePath, alpha, output_dir):
    # 检测路径是否为空
    if not content_imagePath:
        logging.error(encode_str_by_sys("Image path may be empty"))
        return -1
    if not styles_imagePath:
        logging.error(encode_str_by_sys("Image path may be empty"))
        return -1
    module = hub.Module(name='stylepro_artistic')
    # 检测模型是否为空
    if not module:
        logging.error(encode_str_by_sys("Model loading failed"))
        return -1

    try:
        images = [{
            'content': cv2.imread(content_imagePath),
            'styles': [cv2.imread(styles_imagePath)],
        }]
    except:
        logging.error(encode_str_by_sys("Can not read this image !"))
        return -1

    results = module.style_transfer(
        images=images,
        alpha=alpha,
        visualization=True,
        output_dir=output_dir
    )

    if not results:
        logging.error(encode_str_by_sys("No target information detected"))

    return results[0].get('save_path')


# 主函数
def main(args):
    # 当前脚本的路径
    script_path = os.getcwd()
    # 判断系统执行相应的脚本
    if is_linux or is_mac:
        # 打印参数
        print(args.imagePath)

        # TODO 写你的算法函数
        res = stylepro_artistic(args.content_imagePath, args.styles_imagePath, args.alpha, args.output_dir)
        # 下载
        # 处理
        # 返回结果
        print(res)
        return res
    elif is_win:
        # TODO 写你的算法函数
        res = stylepro_artistic(args.content_imagePath, args.styles_imagePath, args.alpha, args.output_dir)
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
    arg.add_argument("--content_imagePath", type=str, default='NONE',
                     help="Here is a network path, and the incoming "
                          "value is an content_image address.")
    arg.add_argument("--styles_imagePath", type=str, default='NONE',
                     help="Here is a network path, and the incoming "
                          "value is an styles_image address.")
    arg.add_argument("--alpha", type=float, default=1.0, help="The conversion strength is between [0, 1], "
                                                               "and the default value is 1;")
    arg.add_argument("--output_dir", type=str, default='Output', help="Here is the folder path of output results")
    args = arg.parse_args()
    main(args)

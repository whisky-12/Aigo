import os
import sys
import argparse
import platform
import logging

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


# 主函数
def main(args):
    # 当前脚本的路径
    script_path = os.getcwd()
    # 判断系统执行相应的脚本
    if is_linux or is_mac:
        # 打印参数
        print(args.param1)
        print(sys.version)

        # TODO 写你的算法函数

    elif is_win:
        print(args.param1)
        print(sys.version)
        pass
    else:
        logging.error(encode_str_by_sys("Unable to execute this script because of unknown system type！！！！！！！"))
    # 回到原来的路径下
    os.chdir(script_path)


if __name__ == '__main__':
    arg.add_argument("--param1", "-e", type=str, default='1', help="The name of your param1. eg: 1 or 2")
    args = arg.parse_args()
    main(args)

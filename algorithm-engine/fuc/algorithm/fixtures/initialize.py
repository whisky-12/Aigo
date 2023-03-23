# 初始化
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.settings")
django.setup()

from common.utils.core_initialize import CoreInitialize
# from fuc.algorithm.views.xxx import XXXInitSerializer


class Initialize(CoreInitialize):

    # def init_xxx(self):
    #     """
    #     初始化部门信息
    #     """
    #     self.init_base(XXXInitSerializer, unique_fields=['p1', 'p2', 'p3'])

    def run(self):
        # self.init_xxx()
        pass


if __name__ == "__main__":
    Initialize(app='fuc.algorithm').run()

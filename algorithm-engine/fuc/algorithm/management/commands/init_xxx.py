# 城市联动
"""
到乡级 使用方法
1. https://www.npmjs.com/package/china-division 下载数据，把对应的json放入对应目录
2. 修改此文件中对应json名
3. 右击执行此py文件进行初始化
"""
import json
import os

import django
import pypinyin
from django.core.management import BaseCommand
from django.db import connection

from application import dispatch

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()


def main():
    # TODO do something
    pass


class Command(BaseCommand):
    """
    项目初始化命令: python manage.py init
    """

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        print(f"正在准备初始化省份数据...")

        if dispatch.is_tenants_mode():
            from django_tenants.utils import get_tenant_model
            from django_tenants.utils import tenant_context
            for tenant in get_tenant_model().objects.exclude(schema_name='public'):
                with tenant_context(tenant):
                    print(f"租户[{connection.tenant.schema_name}]初始化数据开始...")
                    main()
                    print(f"租户[{connection.tenant.schema_name}]初始化数据完成！")
        else:
            main()
        print("xxx数据初始化数据完成！")

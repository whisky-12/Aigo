import json
import logging
import os

import django
from django.db.models import QuerySet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()
from django.core.management.base import BaseCommand

from application.settings import BASE_DIR
from fuc.algorithm.models import Users
# from fuc.algorithm.views.xxx import XxxInitSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    生产初始化菜单: python3 manage.py generate_init_json 生成初始化的model名
    例如：
    全部生成：python3 manage.py generate_init_json
    只生成某个model的： python3 manage.py generate_init_json users
    """

    def serializer_data(self, serializer, query_set: QuerySet):
        serializer = serializer(query_set, many=True)
        data = json.loads(json.dumps(serializer.data, ensure_ascii=False))
        with open(os.path.join(BASE_DIR, f'init_{query_set.model._meta.model_name}.json'), 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return

    def add_arguments(self, parser):
        parser.add_argument("generate_name", nargs="*", type=str, help="初始化生成的表名")

    # def generate_xxx(self):
    #     self.serializer_data(XxxInitSerializer, Xxx.objects.filter(parent_id__isnull=True))

    def handle(self, *args, **options):
        generate_name = options.get('generate_name')
        generate_name_dict = {
            # "xxx": self.generate_xxx,
        }
        if not generate_name:
            for ele in generate_name_dict.keys():
                generate_name_dict[ele]()
            return

        for generate_name in generate_name:
            if generate_name not in generate_name_dict:
                print(f"该初始化方法尚未配置\n{generate_name_dict}")
                raise Exception(f"该初始化方法尚未配置,已配置项:{list(generate_name_dict.keys())}")
            generate_name_dict[generate_name]()
            return


if __name__ == '__main__':
    # with open(os.path.join(BASE_DIR, 'temp_init_xxx.json')) as f:
    #     for xxx_data in json.load(f):
    #         xxx_data['creator'] = 1
    #         xxx_data['modifier'] = 1
    #         request.user = Users.objects.order_by('create_datetime').first()
    #         serializer = MenuInitSerializer(data=menu_data, request=request)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    a = Users.objects.filter()
    print(type(Users.objects.filter()))

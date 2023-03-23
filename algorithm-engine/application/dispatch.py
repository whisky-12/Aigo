#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import connection


def is_tenants_mode():
    """
    判断是否为租户模式
    :return:
    """
    return hasattr(connection, "tenant") and connection.tenant.schema_name


# ================================================= #
# ******************** 初始化 ******************** #
# ================================================= #

def init():
    # 初始化
    return

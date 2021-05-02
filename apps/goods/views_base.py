#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: views_base.py
@time: 2021/5/2 22:07
@desc: 
"""
import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {
        #         'name': good.name,
        #         'category': good.category.name,
        #         'market_price': good.market_price
        #     }
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        # # 使用model_to_dict方法
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        # 使用serializer序列化器
        # data = serializers.serialize('json', goods)
        # return HttpResponse(data, content_type='application/json')

        # 使用JsonResponse返回
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)

# goods/view_base.py

from django.views.generic import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        #通过django的view实现商品列表页
        json_list = []
        #获取所有商品
        goods = Goods.objects.all()
        import json
        from django.core import serializers
        from django.http import JsonResponse

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        #In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(json_data,safe=False)
import xadmin
from .models import Order
from .models import OrderDetail


#订单模型管理类
class OrderModelAdmin(object):
    pass

xadmin.site.register(Order,OrderModelAdmin)

#订单详情模型管理类
class OederDetailModelAdmin(object):
    pass

xadmin.site.register(OrderDetail,OederDetailModelAdmin)
from my_task.main import app


# 完成过期取消订单
@app.task(name="check_order")
def check_order():
    print("判断订单是否超时")

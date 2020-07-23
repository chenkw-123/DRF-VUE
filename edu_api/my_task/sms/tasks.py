# 任务就是一个一个的函数
from edu_api.settings import constants
from my_task.main import app  # 任务必须写在tasks中，不能识别别的文件名称
# 导包要注意main中加载的是什么配置
from edu_api.util.send_msg import Message
import logging

logger = logging.getLogger("django")


@app.task(name="send_msg")  # 指定任务的名称,不指定，则使用默认的函数名
def send_msg(mobile, code):
    # print("发送短信调用此方法")
    message = Message(constants.API_KEY)
    status = message.send_message(mobile, code)
    # print(message)
    if not status:
        logger.error("用户发送短信失败，手机号为：%s" % mobile)

    return ("成功啦！")


@app.task(name="send_email")
def send_email():
    print("发送邮件调用此方法")

    return "send_email"

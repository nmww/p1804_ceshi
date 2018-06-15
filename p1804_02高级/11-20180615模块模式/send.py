# __all__ 指定的模块方法，表示用from导入后需要应用的方法
__all__ = ['send','sendmsg']

# 该模块用于消息发送
def send():
    print("send message to your friends.")
def sendmsg():
    print('send msgs ......')

if __name__ == '__main__':
    #这里是内部的模块功能测试
    print('==这里是内部测试专用代码==')
    send()
    sendmsg()

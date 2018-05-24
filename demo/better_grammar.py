# 文件相关
def file():
    import demo.FileUtils
    fileUtils = demo.FileUtils

    try:
        fileUtils.read_file()
        # fileUtils.appendFile()
        fileUtils.create_file()
    except FileNotFoundError:
        print("没有找到该文件")
    except FileExistsError:
        print("文字执行发生异常")
    except AttributeError:
        print("没有找到这个方法")
    finally:
        print("执行完毕")


# 线程


import time


def thread():
    import math
    import _thread

    def logThread(name, maxCount):
        num = 0
        while num < 2:
            num += 1
            # 沉睡1秒
            # time.sleep(1)
            print("%s执行——现在时间：%s\n" % (name, time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))

    # threading 模块
    import threading
    class MyThreading(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            time.sleep(0.5)
            print("%s 时间：%s" %
                  (self.name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))

    # 线程同步
    class LockThraeding(threading.Thread):
        def __init__(self, name):
            threading.Thread.__init__(self)
            self.name = name

        def run(self):
            # 加锁
            thread_lock.acquire()
            time.sleep(1)
            print("%s 时间：%s" %
                  (self.name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
            # 解锁
            thread_lock.release()

    # 声明线程同步锁
    thread_lock = threading.Lock()

    try:
        _thread.start_new_thread(logThread, ("线程2", 3))
        _thread.start_new_thread(logThread, ("线程1", 5))

        td1 = MyThreading("threading1")
        td2 = MyThreading("threading2")
        td1.start()
        td2.start()

        ltd1 = LockThraeding("同步锁1")
        ltd2 = LockThraeding("同步锁2")
        ltd1.start()
        ltd2.start()

        td1.join()
        td2.join()
        ltd1.join()
        ltd2.join()
    except:
        print("线程启动失败")
    # 保持主线程3s后退出
    time.sleep(3)


# 时间模块
def time_log():
    print(time.time())
    # 输出：1523584077.842348
    print(time.localtime(time.time()))
    # 输出：time.struct_time(tm_year=2018, tm_mon=4, tm_mday=13, tm_hour=9, tm_min=50, tm_sec=12, tm_wday=4, tm_yday=103, tm_isdst=0)
    # 时间格式化
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    # 输出：2018-04-13 09:52:10


# http模块
def http():
    from urllib import request

    def getHtml(url):
        with request.urlopen(url) as r:
            data = r.read()
            return data.decode("utf-8")

    print(getHtml("http://vipstone.cnblogs.com"))

    # def post(url):
    #     from urllib import request, parse
    #
    #     params = parse.urlencode([("name", "老王"), ("pwd", "123456")])
    #     req = request.Request("http://127.0.0.1:8360/video/login")
    #     req.add_header("User-Agent",
    #                    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
    #
    #     with request.urlopen(req, data=params.encode("utf-8")) as r:
    #         data = r.read()
    #         print(data.decode("utf-8"))


def json():
    import json

    data = {"a": "b", "c": 2}

    str_data = '{"a": "b", "c": 2}'
    print(str(data))
    print(str_data)
    d = json.loads(str_data)
    print("d" + str(d))
    a = json.dumps((data)) # 装成string json
    b = json.loads(a)      # 转成字典
    c = json.dumps(b)

    print((a))
    print((b))
    print((c))


# time.sleep(10)
# file()
# thread()
# time_log()
# http()
json()

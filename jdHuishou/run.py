import config.cookie as cookieConfig
import requests
import threading
import time
 
exitFlag = 0
 
class jdThread(threading.Thread):
    def __init__(self, threadID, name, headers):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.headers = headers
    def run(self):
        print ("生成机体 " + self.name)
        getCoupon(self.name, self.headers)
        print ("销毁机体 " + self.name)
 
def getCoupon(name, headers):
    while 1:
        # 判断当前时间
        time.sleep(0.05)
        t = (int)(time.time())
        if t < 1547467190:
            # 19:59:50
            print("%s: %s [%s]" % (name, time.ctime(time.time()), 'waiting'))
            continue
        if t > 1547467210:
            # 20:00:10
            print("%s: %s [%s]" % (name, time.ctime(time.time()), 'end'))
            return
        resp = requests.post('https://hsc.jd.com/couponObtain/obtain',
            data = {
                'couponCode' : 'a581584484b9420fa16aa9477cda86f3',
                'p' : '2',
            },
            headers = headers
        )
        print ("%s: %s [%s]" % (name, time.ctime(time.time()), resp.json()))
 
threads = []
# 创建新线程
i = 1
for name, headers in cookieConfig.config.items():
    thread = jdThread(i, "B-" + str(i) + ' ' + name, headers)
    thread.start()
    threads.append(thread)
    i += 1
    
    pass

# 等待所有线程完成
for t in threads:
    t.join()
print ("销毁原型机")
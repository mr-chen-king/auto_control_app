from multiprocessing import Process, Pool
import time
import uiautomator2 as u2
import random
import subprocess

#由于进程启动的开销比较大，使用多进程的时候会导致大量内存空间被消耗。为了防止这种情况发生可以使用进程池，（由于启动线程的开销比较小，所以不需要线程池这种概念，多线程只会频繁得切换cpu导致系统变慢，并不会占用过多的内存空间）

#进程池中常用方法：
#apply()
#同步执行（串行）
#apply_async()
#异步执行（并行）
#terminate()
#立刻关闭进程池
#join()
#主进程等待所有子进程执行完毕。必须在close或terminate()
#之后。
#close()
#等待所有进程结束后，才关闭进程池。

#滑动浏览
# x_bt x坐标波动区间 sy_bt 起始点波动区间 ey_bt 终点波动区间
def down(x_bt,sy_bt,ey_bt,speed,d):
    sx = ex = random.choice(x_bt)
    sy = random.choice(sy_bt)
    ey = random.choice(ey_bt)

    d.swipe(sx,sy,ex,ey,speed)



def Foo(i):
    d = u2.connect(i)
    while True:
        while True:
            try:
                print("刷新列表")
                down([0.5, 0.6, 0.7, 0.8], [0.2, 0.3, 0.4], [0.6, 0.7, 0.8], 0.3,d)
                time.sleep(3)
                if d(resourceId="c.l.b:id/title").count > 0:
                    d(resourceId="c.l.b:id/title")[1].click()
                    time.sleep(2)
                if d(resourceId="com.cashtoutiao:id/tv_title").count > 0:
                    d(text=u"奇趣").click()
                    time.sleep(2)
                    d(resourceId="com.cashtoutiao:id/tv_title")[2].click()
                    time.sleep(2)
                if d(resourceId="com.ldzs.zhangxin:id/tv_article_title").count > 0:
                    d(resourceId="com.ldzs.zhangxin:id/tv_article_title")[1].click()
                    time.sleep(2)

                if d.exists(text=u"{0}".format(random.choice(['不喜欢', '喜欢']))):
                    d(text=u"{0}".format(random.choice(['不喜欢', '喜欢']))).click()
                    time.sleep(1)
                if d.exists(resourceId="c.l.b:id/main_btn"):
                    if d(resourceId="c.l.b:id/main_btn").info.get('text',None)==None:
                        d(resourceId="c.l.b:id/main_btn").click()
                        time.sleep(2)

                break
            except:
                d = u2.connect(i)
                print("异常")
                continue

        time1 = round(time.time())
        while True:
            try:
                time2 = round(time.time())
                print(time2)
                if time2 - time1 > 20:  # 页面停留大于 15秒
                    print("返回列表……………………………………")
                    #看商品
                    if d.exists(resourceId="c.l.b:id/back_btn"):
                        d(resourceId="c.l.b:id/back_btn").click()
                        #time.sleep(2)
                        # 回列表页
                        break
                    #看新闻
                    if d.exists(resourceId="c.l.b:id/back"):
                        d(resourceId="c.l.b:id/back").click()
                        #time.sleep(2)
                        break
                    #惠头条
                    if d.exists(resourceId="com.cashtoutiao:id/iv_back"):
                        d(resourceId="com.cashtoutiao:id/iv_back").click()
                        #time.sleep(2)
                        break

                    if d.exists(resourceId="com.ldzs.zhangxin:id/iv_back_533"):
                        d(resourceId="com.ldzs.zhangxin:id/iv_back_533").click()
                        #time.sleep(2)
                        break
                    d.press("back")
                    time.sleep(2)
                    break

                else:
                    down([0.5, 0.6, 0.7, 0.8], [0.5, 0.6, 0.7], [0.2, 0.3], 0.1, d)
                    #time.sleep(1)
                    if d.exists(text=u"展开全文"):
                        d(text=u"展开全文").click()
                        #time.sleep(1)
                    if d.exists(text=u"open"):
                        d(text=u"open").click()
                        #time.sleep(1)
            except:
                d = u2.connect(i)
                print("异常")




def getdevlist():
    '''
    利用adb devices先输出所有已连接上的android devices,然后去掉输出中无用的字符,只保留devices SN
    '''
    #devlist = []
    connectfile = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    list = connectfile.stdout.readlines()
    # print(list)
    for i in range(len(list)):
        if str(list[i],'utf-8').find('\tdevice') != -1:
            temp = str(list[i],'utf-8').split('\t')
            #yield devlist.append(temp[0])
            yield temp[0]


def Bar(arg):
    print('-->exec done:', arg)



if __name__ == '__main__':
    # 允许进程池同时放入5个进程
    #pool = Pool(5)
    # 允许进程池同时放入5个进程
    pool = Pool(4)

    #for i in ['T8DDU15C25006210','f8c0906a','de2b902a']:
    for i in getdevlist():
        print(i)
        pool.apply_async(func=Foo, args=(i,),
                         callback=Bar)  # func子进程执行完后，才会执行callback，否则callback不执行（而且callback是由父进程来执行了）
        # pool.apply(func=Foo, args=(i,))

    print('end')
    pool.close()
    # 主进程等待所有子进程执行完毕。必须在close()或terminate()之后。
    pool.join()

    #Foo('f8c0906a')
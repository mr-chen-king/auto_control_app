import requests
import subprocess

def getdevlist():
    #利用adb devices先输出所有已连接上的android devices,然后
    '''去掉输出中无用的字符,只保留devices SN
    '''
    devlist = []
    connectfile = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    list = connectfile.stdout.readlines()
    # print(list)
    for i in range(len(list)):
        if str(list[i],'utf-8').find('\tdevice') != -1:
            temp = str(list[i],'utf-8').split('\t')
            devlist.append(temp[0])
            #yield temp[0]
    return "#".join(devlist)

def task_list():
    data = getdevlist()
    #print(data)
    datas = {"devices":data}

    r = requests.post(url="http://api.aikeling.com/Kernel/create_task",data=datas)
    #print(r.status_code)
    print(r.text)

if __name__== '__main__':
    task_list()
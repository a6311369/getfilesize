import os
import os.path
import math
list1 = []

def get_size(path):
    fileList = os.listdir(path)  # 获取path目录下所有文件
    for filename in fileList:
        # print(filename)         #印出檔案名稱
        pathTmp = os.path.join(path,filename)  # 获取path与filename组合后的路径
        if os.path.isdir(pathTmp):   # 判断是否为目录
            get_size(pathTmp)        # 是目錄就繼續遞迴尋找
        elif os.path.isfile(pathTmp):  # 判断是否为文件
            filesize = os.path.getsize(pathTmp)  # 如果是文件，则获取相应文件的大小
            filesize2 = int(filesize3(filesize))
            print('檔案名稱：%s' % filename ,'檔案大小：%d byte' % filesize2 )
            list1.append(filesize)      # 将文件的大小添加到列表
    # print(sum(list1))
    # print(fileList)
# path= input("输入路径：").strip()  #由用户指定文件路径

#位元組轉換
def roundstr(size):
    return str(round(size, 1))
def filesize3(bytesize):
    if bytesize < 1024:
        return str(bytesize) + ' Bytes'
    elif bytesize < 1024 ** 2:    #**為返回x的y次方
        return roundstr(bytesize / 1024.0) + ' KBytes'
    elif bytesize < 1024 ** 3:
        return roundstr(bytesize / (1024.0 ** 2)) + ' MBytes'
    elif bytesize < 1024 ** 4:
        return roundstr(bytesize / (1024.0 ** 3)) + ' GBytes'
    elif bytesize < 1024 ** 5:
        return roundstr(bytesize / (1024.0 ** 4)) + ' TBytes'
    else:
        return str(bytesize) + ' Bytes'

path = 'C:\\影片\\無聊詹'    #指定路徑
get_size(path)
# print('目錄中的文件總大小：%d Byte' % sum(list1))


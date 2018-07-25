#coding=utf-8
import os
import os.path
import math


list1 = []
b = []
def get_size(path):
    fileList = os.listdir(path)  # 獲取path目錄下所有文件
    for filename in fileList:
        # print(filename)         #印出檔案名稱
        pathTmp = os.path.join(path,filename)  # 獲取path與filename組合後的路徑
        if os.path.isdir(pathTmp):   # 判斷是否為目錄
            get_size(pathTmp)        # 是目錄就繼續遞迴尋找
        elif os.path.isfile(pathTmp):  # 判斷是否為檔案
            filesize9 = os.path.getsize(pathTmp)  # 如果是檔案，則獲取相應檔案的大小
            filesize = filesize3(os.path.getsize(pathTmp))  # 如果是檔案，則獲取相應檔案的大小
            # filesize2 = filesize3(filesize)
            if filesize9 > 1073741824: #檔案大小比對，超過1G就抓出來
                a = '該檔案超過1G','檔案名稱：%s' % filename ,'檔案大小：%s ' % filesize
                b.append(a) #將檔案名稱增加到list內
                # print (a)
                # print('該檔案超過1G','檔案名稱：%s' % filename ,'檔案大小：%s ' % filesize)
            # print('檔案名稱：%s' % filename ,'檔案大小：%s ' % filesize )  # %s是接字串  %d是接數值
            # list1.append(filesize)      # 將檔案的大小添加到列表
    # print(sum(list1))
    # print(fileList)
# path= input("输入路径：").strip()  #由用戶指定檔案路徑

#位元組轉換
def roundstr(size):
    return str(round(size, 1))   #round(size, 1) 取小數第一位後開始四捨五入
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

path = 'E:\\ISO'    #指定路徑
get_size(path)
# print('目錄中的文件總大小：%d Byte' % sum(list1))
for i in b:   #跑回圈輸出list內的資料
    print(i)


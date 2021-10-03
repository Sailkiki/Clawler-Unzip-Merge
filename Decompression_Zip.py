#coding=utf-8
import zipfile
import os
import shutil

def unzip_file(path):
    filenames = os.listdir(path)#获取目录下所有文件名
    for filename in filenames:
        filepath = os.path.join(path,filename)
        zip_file = zipfile.ZipFile(filepath)

        newfilepath = filename.split(".", 1)[0] #获取压缩文件的文件名
        # print(newfilepath)
        newfilepath = os.path.join(path, newfilepath)
        # print(newfilepath)

        if os.path.isdir(newfilepath): # 根据获取的压缩文件的文件名建立相应的文件夹
            pass
        else:
            os.mkdir(newfilepath)

        for name in zip_file.namelist():# 解压文件
            zip_file.extract(name, newfilepath)
        zip_file.close()
        Conf = os.path.join(newfilepath, 'conf')
        if os.path.exists(Conf):
            shutil.rmtree(Conf)
        if os.path.exists(filepath):
            os.remove(filepath)
        print("解压{0}成功".format(filename))
if __name__ == '__main__':
    unzip_file('D:\\crawler\zips')


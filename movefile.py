# -*- encoding: utf-8 -*-
'''
@File    :   for_lhluo.py
@Time    :   2021/11/05 17:42:25
@Author  :   lhluo4
@Version :   1.0
@Contact :   lhluo4@iflytek.com
@License :   (C)Copyright 2021, lhluo4
@Desc    :   None
'''

# here put the import lib
import os
import shutil
import zipfile


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


if __name__ == "__main__":
    path = r'E:\test'
    dst_dir = r'E:\test2'
    zipLst = []

    for file in os.listdir(path):
        if file.endswith('zip'):
            zipLst.append(file)
    print(zipLst)

    if os.path.exists(dst_dir):
        pass
    else:
        os.mkdir(dst_dir)
    for file in zipLst:
        zip_src = os.path.join(path, file)
        unzip_file(zip_src, dst_dir)

'''
Created on 2015-01-27
Updated on 2024-01-15 : Change coding style in Python 3 runtime
@author: BALLAD
'''

import os

################################################################
#
# Rename files of my auto model images collection, make it tidy.
# Use GBK or UTF-8 depends on OS (Windows_ZHCN using GBK)
#
################################################################

# Commented Info
# -*- coding: GBK -*- Python 2 style
# coding=gbk 

# WORK_DIR
# WORK_DIR = "E:\\pytemp\\"
# WORK_DIR = "E:\\个人资料\\Collection\\"
WORK_DIR = "E:\\Devspace\\github\\motorwantlist\\motorwantlist-e\\src\\renderer\\assets\\motor_images\\"

# Rename files (images) of all auto images collection        
# @param prootpath - the root path
def walk_root_dir(rootpath):
    for filename in os.listdir(rootpath):
        if os.path.isfile(os.path.join(rootpath, filename)) == False:
            dirname = rootpath + "\\" + filename
            walk_maker_dir(dirname, filename)

# Rename files (logo, and model image) of a spec auto maker        
# @param path - auto maker dir name
# @param maker_name - auto maker name
def walk_maker_dir(path, maker_name):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) == True:
            # maker logo image
            # 所有 logo 临时改为 jpg
            # filetype = ''
            # dot_pos = filename.rfind('.')
            # if dot_pos != -1:
            #     filetype = filename[dot_pos + 1:len(filename)]
            # else :
            #     filetype = "jpg"
            filetype = "jpg"
            new_name = maker_name + ' - logo.' + filetype
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
        else:
            dirname = path + "\\" + filename
            model_name = filename
            rename_files_of_dir(dirname, model_name)

# Rename files (images) of a spec auto model        
# @param path - auto model dir name
# @param model_name - model name of auto model
def rename_files_of_dir(path, model_name):
    # 临时改名为 Tempfilename
    i = 1
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) == True:
            filetype = ''
            dot_pos = filename.rfind('.')
            if dot_pos != -1:
                filetype = filename[dot_pos + 1:len(filename)]
            else :
                filetype = "jpg"
            new_name = 'Tempfilename' + str(i) + "." + filetype
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            i = i + 1
    # 再按照 model_name 命名
    i = 1
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) == True:
            filetype = ''
            dot_pos = filename.rfind('.')
            if dot_pos != -1:
                filetype = filename[dot_pos + 1:len(filename)]
            else :
                filetype = "jpg"
            new_name = model_name + ' - ' + str(i) + "." + filetype
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            i = i + 1
     
if __name__ == '__main__':
    # rename_files_of_dir('E:\\pytemp\\Lamborghini\\Lamborghini Diablo 1991\\', 'Lamborghini Diablo 1991')
    walk_root_dir(WORK_DIR)

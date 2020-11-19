# -*- coding: utf-8 -*-
# Author: kelvinBen
# Github: https://github.com/kelvinBen/AppInfoScanner
import os
import time
import shutil
import platform


# smali 所在路径
smali_path = ""

# backsmli 所在路径
backsmali_path = ""

# apktool 所在路径
apktool_path = ""

# 系统类型
os_type = ""

# 输出路径
output_path = ""

# 下载完成标记
download_flag = False

class Bootstrapper(object):

    def __init__(self, path):
        global smali_path
        global backsmali_path
        global apktool_path
        global os_type
        global output_path
        global script_root_dir
        global txt_result_path
        global xls_result_path
        global strings_path
        global history_path
        global app_history_path
        global domain_history_path
        global excel_row 
        global download_path
        global download_flag

        create_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

        script_root_dir =  os.path.dirname(os.path.abspath(path))
        tools_dir = os.path.join(script_root_dir,"tools")
        
        if platform.system() == "Windows":
            machine2bits = {'AMD64':64, 'x86_64': 64, 'i386': 32, 'x86': 32}
            machine2bits.get(platform.machine())

            if platform.machine() == 'i386' or platform.machine() == 'x86':
                strings_path = os.path.join(tools_dir,"strings.exe")
            else:
                strings_path = os.path.join(tools_dir,"strings64.exe")
        else:
            strings_path ="strings"
        
        excel_row = 0
        backsmali_path = os.path.join(tools_dir,"baksmali.jar")
        apktool_path = os.path.join(tools_dir, "apktool.jar")
        output_path = os.path.join(script_root_dir,"out")
        history_path = os.path.join(script_root_dir,"history")
        download_path = os.path.join(script_root_dir,"download")
        txt_result_path = os.path.join(script_root_dir,"result_"+str(create_time)+".txt")
        xls_result_path = os.path.join(script_root_dir,"result_"+str(create_time)+".xls")
        app_history_path = os.path.join(history_path,"app_history.txt")
        domain_history_path = os.path.join(history_path,"domain_history.txt")


    def init(self):
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.makedirs(output_path)

        if os.path.exists(download_path):
            shutil.rmtree(download_path)
        os.makedirs(download_path)

        if not os.path.exists(history_path):
            os.makedirs(history_path)
        
        if os.path.exists(txt_result_path):
            os.remove(txt_result_path)

        if os.path.exists(xls_result_path):
            os.remove(xls_result_path)

        
            


        
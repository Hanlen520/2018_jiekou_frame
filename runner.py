# -*- coding: utf-8 -*-
__author__ = 'Administrator'
#from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
from public.path import get_super_path
import time,unittest
from public.se_email import Send_email

# a=get_super_path()+r'\TestCase'
# print(a)
class RunTestCase():
    def __init__(self):
        self.super_path=get_super_path()
        self.case_path=get_super_path()+r'\TestCase'

    #获取测试文件下的测试用例
    @property
    def suite(self):
        dir_case=unittest.defaultTestLoader.discover(
            self.case_path,
            #pattern='test_*.py',
            pattern='*_test.py',
            top_level_dir=None
                )
        return dir_case

    #获取当前时间
    @property
    def getNowTime(self):
        return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

    def runAutomation(self):
        filename=self.super_path+r"\report\test_"+RunTestCase().getNowTime+'.html'
        fp=open(filename,'wb')
        runner=BSTestRunner(
            stream=fp,
            title=u'API_test',
            description=u'接口测试报告详情',
        )
        runner.run(RunTestCase().suite)


if __name__ == '__main__':
    R=RunTestCase()
    R.runAutomation()
    #调用自动发送邮件
    Send_email("E:\F\zhangwk02\\2018_jiekou_frame0504\\report").send_email()
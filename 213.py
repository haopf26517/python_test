#coding=utf-8
import unittest
#导入两个执行用例
import ffpp213.py
import ffppyjzscx213.py
#导入报告模块
import HTMLTestRunner
import time
#定义一个单元测试test容器
testunit=unittest.TestSuite()
#将测试用例加入到测试容器，即测试套件中。
testunit.addTest(unittest.makeSuite(ffpp213.Ffppunits))
testunit.addTest(unittest.makeSuite(ffppyjzscx213.FfppUntis1))
#取前面的时间'
now = time.strftime("%Y-%m-%M-%H-%M-%S",time.localtime(time.time()))
#定义报告存放的路径
filename= 'f:\\pyse\\report\\'+now+'restule.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'应急指挥火情测试报告',
    description=u'用例执行情况：')
#执行测试套件
runner.run(testunit)

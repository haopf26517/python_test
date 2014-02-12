# -*- coding: cp936 -*-

#从sys包里解出argv 功能模块
from sys import argv
#从os.path包里解出exists功能模块
from os.path import exists
#定交两个argv参数
script, from_file, to_file = argv
#打印出拷贝的源文件名和目标文件名。
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#以%r方式打开文件，并把返回值赋予变量 in_file
in_file = open(from_file)
#读取文件内容，并把内容赋予变量 indata
indata = in_file.read()

#打印出读取文件内容的长度字节。
print "The input file is %d bytes long" % len(indata)
#查询目标文件是否存在。
print "Does the output file exist? %r" % exists(to_file)

#打印出提示语：Ready, hit RETURN to continue, CTRL-C to abort.
print "Ready, hit RETURN to continue, CTRL-C to abort."
#输入任意键继续。
raw_input()

#以'w'方式打开目标文件
out_file = open(to_file, 'w')
#把源文件写入目标文件。
out_file.write(indata)
#打印出结束语。
print "Alright, all done."
#关闭两个文件
out_file.close()
in_file.close()

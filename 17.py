# -*- coding: cp936 -*-

#��sys������argv ����ģ��
from sys import argv
#��os.path������exists����ģ��
from os.path import exists
#��������argv����
script, from_file, to_file = argv
#��ӡ��������Դ�ļ�����Ŀ���ļ�����
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
#��%r��ʽ���ļ������ѷ���ֵ������� in_file
in_file = open(from_file)
#��ȡ�ļ����ݣ��������ݸ������ indata
indata = in_file.read()

#��ӡ����ȡ�ļ����ݵĳ����ֽڡ�
print "The input file is %d bytes long" % len(indata)
#��ѯĿ���ļ��Ƿ���ڡ�
print "Does the output file exist? %r" % exists(to_file)

#��ӡ����ʾ�Ready, hit RETURN to continue, CTRL-C to abort.
print "Ready, hit RETURN to continue, CTRL-C to abort."
#���������������
raw_input()

#��'w'��ʽ��Ŀ���ļ�
out_file = open(to_file, 'w')
#��Դ�ļ�д��Ŀ���ļ���
out_file.write(indata)
#��ӡ�������
print "Alright, all done."
#�ر������ļ�
out_file.close()
in_file.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fileIO import *
from formula import *

def screen_in():
    form_list = Formula()
    print('请输入变量列表 如: x y z t')
    form_list.vars = list_in()
    print('请输入函数公式 如 x**y+3*x')
    form_list.formula = input()
    for i in range(len(form_list.vars)):
        element=var_in(form_list.vars[i])
        form_list.varlist_in(element)
    output(form_list.output())
    print('是否保存 y/n')
    if (input() == 'y'):
        print ('输入文件名：')
        file_out(input(),form_list)
def var_in(var):
    newtest = Data()
    print('输入%s的单位 c m k ...' % var)
    newtest.unit = input()
    print('输入%s的列表 如: 1 1 1 1 1' % var)
    lists = list_in()
    lists = [float(lists[i]) for i in range(len(lists))]
    newtest.rxl = lists
    print('输入系统误差：')
    try:
        newtest.ub = float(input())
    except ValueError as e:
        print(e,'数据未输入，默认为0')
        newtest.ub=0
    return newtest
def main():
    print('请输入需要读取的文件,不需要就乱输入')
    file_name=input()
    try:
        open('./'+file_name+'.json','r')
    except FileNotFoundError:
        screen_in()
    else:
        file_in(file_name)

# start main at last ################################################
if __name__ == '__main__':
    main()

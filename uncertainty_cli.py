#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fileIO import *
from formula import *

def file_in():
    pass
def file_out():
    pass
def screen_in():
    form_list = Formula()
    print('请输入变量列表 如: x y z t')
    form_list.vars = list_in()
    print('请输入函数公式 如 x**y+3*x')
    form_list.formula = input()
    form_list.varlist_in(var_in)
    output(form_list)
    print('是否保存 y/n')
    if (input() == 'y')
        file.out():
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
def output(form_list):
    for i in range(len(form_list.vars)):
        print('%s = %f~%f' % (form_list.vars[i],form_list.varlist[i].avg, form_list.varlist[i].sigma_x))
    avg_list = [ form_list.varlist[i].avg for i in range(len(form_list.varlist))]

    diff = form_list.diff(avg_list)
    xig = [ diff[i]*form_list.varlist[i].sigma_x for i in range(len(avg_list))]
    sigma = sqrt(reduce(lambda x,y: x+y , map(lambda x: x**2, xig)))
    value = form_list.value(avg_list)
    Ex = sigma/value
    print('   @ = %f~%f   %e' % (value, sigma, Ex))
def main():
    screen_in()

# start main at last ################################################
if __name__ == '__main__':
    main()

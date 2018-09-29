#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from functools import reduce
from sympy import Symbol, diff, evalf, symbols
from sympy.parsing.sympy_parser import parse_expr
# classes ###########################################################
class Data(object):

    def __str__(self):
        return 'Data named (name: %s)' % self.name
    __repr__=__str__

    @property
    def rxl(self):
        return self._rxl
    @rxl.setter
    def rxl(self, value):
        self._rxl = value
    @property
    def ub(self):
        return self._ub
    @ub.setter
    def ub(self,value=0):
        if len(self._rxl) > 1:
            value = value / sqrt(3)
        self._ub = value
    @property
    def avg(self):
        add = lambda x,y: x+y
        n = len(self._rxl)
        return reduce(add, self._rxl)/n
# ---------get sigma_x------------
    @property
    def sigma_x(self):
        x_ = self.avg
        rxl = self._rxl
        ub = self._ub
        n = len(rxl)
        if n>1:
            add = lambda x,y: x+y
            ss = reduce(add, map(lambda x: (x-x_)**2, rxl))
            ua =  sqrt(ss/(n*(n-1)))
        else:
            ua = 0
        return sqrt(ua**2+ub**2)
#----------object formula------------
class Formula(object):
    @property
    def vars(self):
        return self._vars
    @vars.setter
    def vars(self,vlist):
        self._vars = vlist
    @property
    def varsy(self):
        return symbols(self._vars)
    @property
    def formula(self):
        return self._formula
    @formula.setter
    def formula(self,func):
        self._formula = parse_expr(func)

    def value(self, avg):
        dicts = {}
        for i in  range(len(self.varsy)):
            dicts[self.varsy[i]] = avg[i]
        return self._formula.evalf(subs=dicts)
    def diff (self, avg):
        df =[ self._formula.diff(self.varsy[i]) for i in range(len(self.varsy)) ]
        dicts = {}
        for i in  range(len(self.varsy)):
            dicts[self.varsy[i]] = avg[i]
        df_vars =[ df[i].evalf(subs=dicts) for i in range(len(self.varsy))]
        return df_vars
# ------------function--------
def list_in():
    strs = input()
    strs.strip(" ")
    return strs.split(" ")
def var_in(var):
    newtest = Data()
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
def formula_in():
    newtest = Formula()
    print('请输入变量列表 如: x y z t')
    newtest.vars = list_in()
    print('请输入函数公式 如: x**y+3*x')
    newtest.formula = input()
    return newtest
def add(x,y):
    return x+y
def main():
    form_list = formula_in()
    var_list =[]
    for i in range(len(form_list.vars)):
        var_list.append(var_in(form_list.vars[i]))
    for i in range(len(form_list.vars)):
        print('%s = %f~%f' % (form_list.vars[i], var_list[i].avg, var_list[i].sigma_x))
    avg_list = [ var_list[i].avg for i in range(len(var_list))]

    diff = form_list.diff(avg_list)
    xig = [ diff[i]*var_list[i].sigma_x for i in range(len(avg_list))]
    sigma = sqrt(reduce(add, map(lambda x: x**2, xig)))
    value = form_list.value(avg_list)
    Ex = sigma/value
    print('   @ = %f~%f   %e' % (value, sigma, Ex))

# start main at last ################################################
if __name__ == '__main__':
    main()

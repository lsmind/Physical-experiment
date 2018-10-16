#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from functools import reduce
from sympy import Symbol, diff, evalf, symbols
from sympy.parsing.sympy_parser import parse_expr
# Units dictionary #################################################
units={'c':0.01,'d':0.1, 'm':0.001, 'k':1000, 'u':0.000001, 'n':0.000000001}

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
        self.rxl_t=value
        self._rxl = list(map(lambda x: x*self.unit, value))
    @property
    def ub(self):
        return self._ub
    @ub.setter
    def ub(self,value=0):
        self.ub_t=value
        if len(self._rxl) > 1:
            value = value / sqrt(3)
        self._ub = value*self._unit
    @property
    def avg(self):
        add = lambda x,y: x+y
        n = len(self._rxl)
        return reduce(add, self._rxl)/n
    @property
    def unit(self):
        return self._unit
    @unit.setter
    def unit(self,value=1):
        try:
            self.unit_t=value
            unit = units[value]
        except KeyError:
            print("输入错误,默认未1");
            self._unit = 1
        else:
            self._unit = unit
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
    def varlist_in(self,vars_in):
        var_list =[]
        for i in range(len(self._vars)):
            var_list.append(vars_in(self.vars[i]))
        self.varlist = var_list

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
    listin = list(filter(lambda s: s and s.strip(), strs.split()))
    return listin

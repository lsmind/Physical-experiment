#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
from functools import reduce
from sympy import Symbol, evalf, symbols
from sympy.parsing.sympy_parser import parse_expr
# Units dictionary #################################################
units={'1':1, 'c':0.01, 'd':0.1, 'm':0.001, 'k':1000, 'u':0.000001, 'n':0.000000001}

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
    def unit(self):
        return self._unit
    @unit.setter
    def unit(self,value=1):
        try:
            unit = units[value]
        except KeyError:
            print("输入错误,默认未1");
            self._unit = 1
            self.unit_t=value
        else:
            self._unit = unit
            self.unit_t=value
class Formula(object):
    def __init__ (self):
        self.varlist=[]
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
        self.formula_t = func
        self._formula = parse_expr(func)
    def varlist_in(self,element):
        self.varlist.append(element)

    def value(self, avg):
        dicts = {}
        for i in  range(len(self.varsy)):
            dicts[self.varsy[i]] = avg[i]
        return self._formula.evalf(subs=dicts)
    def output(self):
        result = ["result:"]
        for j in range(len(self.varlist[-1].rxl)):
            avg_list = [];
            for i in range(len(self.varlist)):
                max = len(self.varlist[i].rxl) - 1
                if max < j:
                    item = self.varlist[i].rxl[max]
                else:
                    item = self.varlist[i].rxl[j]
                avg_list.append(item)
            value = self.value(avg_list)
            result.append('%e' % (value))
        return result

# ------------function--------
def list_in():
    strs = input()
    listin = list(filter(lambda s: s and s.strip(), strs.split()))
    return listin

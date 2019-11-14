#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from formula import *

def load_form(file_name):
    lst = [] 
    with open(file_name,'r') as f:
        for each_form in f.readlines():
            lst.append(each_form.replace("\n", "").replace("^","**"))
    return lst

def save_form(file_name, lst):
    with open(file_name,'w') as f:
        for each_form in lst:
            f.write(each_form)

def load(file_name):
    with open(file_name,'r') as f:
        content = f.read()
        try:
            content_js = json.loads(content)
        except KeyError:
            print("输入格式有误")
        else:
            return content_js

def save(file_name,content):
    with open(file_name,'w') as f:
        try:
            content_js = json.dumps(content)
        except KeyError:
            print("输入格式有误")
        else:
            content_js_r = content_js.replace(", ", ",\n")
            f.write(content_js_r)
def file_out(filename,form_list):
    file_dict = {}
    file_dict["vars"] = form_list.vars
    file_dict["formula"] = form_list.formula_t
    for var in range(len(form_list.vars)):
        list_i = []
        list_i.append(form_list.varlist[var].rxl_t)
        list_i.append(form_list.varlist[var].unit_t)
        list_i.append(form_list.varlist[var].ub_t)
        file_dict[form_list.vars[var]] = list_i
    save(filename,file_dict)
def file_in(filename):
    contain = load(filename)
    form_list = Formula()
    form_list.vars = contain['vars']
    form_list.formula = contain['formula']
    for i in range(len(form_list.vars)):
        element = contain[form_list.vars[i]]
        form_list.varlist_in(fvar_in(element))
    return form_list
def fvar_in(element):
    newtest = Data()
    newtest.unit = element[1]
    newtest.rxl = element[0]
    newtest.ub = element[2]
    return newtest
def output(form_list):
    str_list = form_list.output()
    for result in str_list:
        print(result)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
import fileIO as IO

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.varlist=[]
        self.pack()
        self.operat()
    def operat(self):
        add_var=Button(self, text="添加", command=self.createVar)
        add_var.pack()
        self.fform_in()
        compute=Button(self, text="计算")
        compute.pack()
    def fform_in(self):
            formula_lable=Label(self, text="公式")
            formula_lable.pack()
            formula = Entry(self)
            formula.pack()
    def createVar(self):
        name_lable=Label(self, text="名字")
        name_lable.pack()
        name = Entry(self)
        name.pack()
        ub_lable=Label(self, text="误差")
        ub_lable.pack()
        ub = Entry(self)
        ub.pack()
        rxl_lable=Label(self, text="数据")
        rxl_lable.pack()
        rxl = Entry(self)
        rxl.pack()
    def createCan(self):
        #self.alertButton = Button(self, text='Hello', command=self.*****)
        self.alertButton.pack()

    def Error(Error_code):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Error, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('物理不确定度计算')
# 主消息循环:
app.mainloop()

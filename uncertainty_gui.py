#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtWidgets
import GUIwidget
import formula

class MainApp(QtWidgets.QMainWindow, GUIwidget.Ui_MainWindow):
    """ MainApp for create a class to use GUI """

    def __init__(self,parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # 数据结构
        self.dataSet={} # {'x':Data()}
        # 按键操作
        self.btnAddVar.clicked.connect(self.add_variable)
        self.btnDelVar.clicked.connect(self.del_variable)
        self.btnCompute.clicked.connect(self.compute)
        self.btnAddData.clicked.connect(self.add_data)
        self.btnDelData.clicked.connect(self.del_data)
        self.lstVar.itemClicked.connect(self.on_lstVar_lstData)
        self.cbbUnit.currentTextChanged.connect(self.unit_change)
        self.lndError.editingFinished.connect(self.error_input)

    def add_variable(self):
        # 获取输入框的值
        varName=self.lndVar.text()
        # 不为空且不为数字
        if varName == '' or not varName.isalpha():
            # 清空输入
            self.lndVar.clear()
            return None
        # 检测是否重复
        for itemName in self.dataSet.keys():
            if varName == itemName:
            # 清空输入
                self.lndVar.clear()
                return None
        # 添加进数据集
        self.dataSet[varName] = currentData = formula.Data()
        # 数据初始化
        ## 单位
        currentData.unit='1'
        ## 数据表
        currentData.rxl=[]
        ## 误差
        currentData.ub=.0
        # 添加列表
        self.lstVar.addItem(varName)
        # 清空输入框
        self.lndVar.clear()

    def del_variable(self):
        # 获取选中值
        varName=self.lstVar.currentItem()
        # 从数据集中删除
        try:
            del self.dataSet[varName.text()]
        except AttributeError:
            self.lstData.clear()
            return 1
        # 从表格中删除
        self.lstVar.takeItem(self.lstVar.row(varName))
        # 刷新列表
        self.on_lstVar_lstData()

    def add_data(self):
        # 获取输入框的值
        varName=self.lndData.text()
        # 输入框的值不能为空
        if varName == '' or not varName.isdigit():
            # 清空输入框
            self.lndData.clear()
            return None
        try:
            newData = self.currentData.rxl_t.copy()
        except AttributeError:
            return 1
        # 添加进数据集
        newData.append(float(varName))
        self.currentData.rxl = newData
        # 添加列表
        self.lstData.addItem(varName)
        # 清空输入框
        self.lndData.clear()

    def del_data(self):
        # 获取选中值
        DataName=self.lstData.currentItem()
        # 从数据集中删除
        try:
            # 从表格中删除
            self.lstData.takeItem(self.lstData.row(DataName))
            # 删除数据
            temprxl = self.currentData.rxl_t.copy()
            temprxl.remove(float(DataName.text()))
            self.currentData.rxl = temprxl

        except AttributeError:
            return 1

    def on_lstVar_lstData(self):
        # 获取当前Data
        try:
            self.currentData = self.dataSet[self.lstVar.currentItem().text()]
        except AttributeError:
            self.lstData.clear()
            return 1
        # 更新数据列表
        self.lstData.clear()
        for Number in self.currentData.rxl_t:
            self.lstData.addItem(str(Number))
        # 更新单位
        self.cbbUnit.setCurrentText(self.currentData.unit_t)
        # 更新误差
        self.lndError.setText(str(self.currentData.ub_t))

    def unit_change(self):
        try:
            self.currentData.unit_t = self.cbbUnit.currentText()
            self.currentData.rxl = self.currentData.rxl_t
        except AttributeError:
            return 1

    def error_input(self):
        try:
            self.currentData.ub = float(self.lndError.text())
        except AttributeError:
            return 1

    def compute(self):
        form_list = formula.Formula()
        form_list.vars = list(self.dataSet.keys())
        form_list.formula = self.lndFormula.text()
        form_list.varlist = list(self.dataSet.values())
        results = ''
        for result in  form_list.output():
            results = results + '\n' + result
        choose = QtWidgets.QMessageBox.information(self, '结果',
            results+'\n   是否需要保存',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if choose == QtWidgets.QMessageBox.Yes:
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

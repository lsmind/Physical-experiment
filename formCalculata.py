#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtWidgets
import GUIwidget
import formula
import fileIO

class extroApp(QtWidgets.QWidget, GUIwidget.Ui_frmIntro):
    def __init__(self, content, parent=None):
        super(extroApp, self).__init__(parent)
        self.setupUi(self, content)

class MainApp(QtWidgets.QMainWindow, GUIwidget.Ui_MainWindow):
    """ MainApp for create a class to use GUI """

    def __init__(self,parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.wndLicence = extroApp('licence')
        self.wndAnthor = extroApp('anthor')
        self.wndUsage = extroApp('usage')
        # 数据结构
        self.dataSet={} # {'x':Data()}
        self.fileName=None
        self.fileFormName=None
        # 信息槽
        self.lstForm.currentRowChanged.connect(self.updateFormRow)
        self.lstVar.currentRowChanged.connect(self.updateVarRow)
        self.lstData.currentRowChanged.connect(self.updateDataRow)
        self.lndData.returnPressed.connect(self.add_data)
        self.lndVar.returnPressed.connect(self.add_variable)
        self.lndForm.returnPressed.connect(self.add_formula)
        self.btnAddVar.clicked.connect(self.add_variable)
        self.btnDelVar.clicked.connect(self.del_variable)
        self.btnAddForm.clicked.connect(self.add_formula)
        self.btnDelForm.clicked.connect(self.del_formula)
        self.btnCompute.clicked.connect(self.compute)
        self.btnAddData.clicked.connect(self.add_data)
        self.btnDelData.clicked.connect(self.del_data)
        self.lstForm.itemDoubleClicked.connect(self.editForm)
        self.lstVar.itemClicked.connect(self.on_lstVar_lstData)
        self.actLicence.triggered.connect(self.wndLicence.show)
        self.actAnthor.triggered.connect(self.wndAnthor.show)
        self.actUsage.triggered.connect(self.wndUsage.show)
        self.actOpen.triggered.connect(self.openFile)
        self.actSave.triggered.connect(self.saveFile)
        self.actOpenForm.triggered.connect(self.openFormFile)
        self.actSaveForm.triggered.connect(self.saveFormFile)
        self.actSaveAs.triggered.connect(self.saveAsFile)
    def updateFormRow(self):
        self.lblForm.setText(str(1 + self.lstForm.currentRow()))
    def updateDataRow(self):
        self.lblData.setText(str(1 + self.lstData.currentRow()))
    def updateVarRow(self):
        self.lblVar.setText(str(1 + self.lstVar.currentRow()))
    def add_formula(self):
        # 获取输入框的值
        varName=self.lndForm.text()
        # 输入框的值不能为空
        if varName == '':
            # 清空输入框
            self.lndForm.clear()
            return None
        # 添加列表
        self.lstForm.addItem(varName)
        # 清空输入框
        self.lndForm.clear()
    def del_formula(self):
        # 获取选中值
        DataName=self.lstForm.currentItem()
        # 从数据集中删除
        try:
            # 从表格中删除
            self.lstForm.takeItem(self.lstForm.row(DataName))
            # 删除数据
        except AttributeError:
            return 1
    def saveAsFile(self):
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "选取文件", "./", "Json Files (*.json)")
        self.saveFile()
    def saveFormFile(self):
        try:
            items = []
            for index in range(self.lstForm.count()):
                 items.append(self.lstForm.item(index))
            formulas = [i.text() for i in items]
        except SyntaxError as e:
            QtWidgets.QMessageBox.critical(self, '<error>',
                    '错误原因: '+str(e),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.Yes)
            return -1
        if self.fileFormName is None:
            self.fileFormName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "选取文件", "./", "Text Files (*.txt)")
        try:
            fileIO.save_form(self.fileFormName+'.txt', formulas)
        except FileNotFoundError as e:
            QtWidgets.QMessageBox.critical(self, '错误',
                    '无法保存数据 \n错误原因: '+str(e),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.Yes)
            return -1
    def saveFile(self):
        try:
            form_list = formula.Formula()
            form_list.vars = list(self.dataSet.keys())
            #form_list.formula = self.lndFormula.text()
            form_list.varlist = list(self.dataSet.values())
        except SyntaxError as e:
            QtWidgets.QMessageBox.critical(self, '错误',
                    '数据不完善 \n错误原因: '+str(e),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.Yes)
            return -1
        if self.fileName is None:
            self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "选取文件", "./", "Json Files (*.json)")
        try:
            fileIO.file_out(self.fileName+'.json', form_list)
        except FileNotFoundError as e:
            QtWidgets.QMessageBox.critical(self, '错误',
                    '无法保存数据 \n错误原因: '+str(e),
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.Yes)
            return -1
    def openFormFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "Text Files (*.txt)")
        self.addFormLst(fileName)
    def addFormLst(self, fileName):
        form_list = fileIO.load_form(fileName)
        for forms in form_list:
            self.lstForm.addItem(forms)
    def openFile(self):
        # 打开文件
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "Json Files (*.json)\n Text Files (*.txt)")
        extend = fileName.split('.')[-1]
        if extend == "json":
            try:
                form_list = fileIO.file_in(fileName)
            except FileNotFoundError as e:
                QtWidgets.QMessageBox.critical(self, '错误',
                        '文件无法读取 \n错误原因: '+str(e),
                        QtWidgets.QMessageBox.Yes,
                        QtWidgets.QMessageBox.Yes)
                return -1
            # 添加进当下文件
            self.fileName = fileName
            # 显示文件内容
            self.dataSet = dict(zip(form_list.vars, form_list.varlist))
            self.lstVar.clear()
            for varName in self.dataSet.keys():
                self.lstVar.addItem(varName)
                self.on_lstVar_lstData()
        elif extend == "txt":
            self.addFormLst(fileName)
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
        if varName == '' or not varName.replace('.','').isdigit():
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
    def editForm(self):
        self.lndForm.setText(self.lstForm.currentItem().text())
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
        # 更新误差
    def unit_change(self):
        try:
            self.currentData.rxl = self.currentData.rxl_t
        except AttributeError:
            return 1
    def compute(self):
        try:
            form_list = formula.Formula()
            form_list.vars = list(self.dataSet.keys())
            formText =self.lstForm.currentItem().text()
            form_list.formula = formText
            form_list.varlist = list(self.dataSet.values())
            results = ''
            for result in  form_list.output():
                results = results + '\n' + result
            self.txtInfo.append('<info> 公式' + str(self.lstForm.currentRow()) + '计算结果为: ' + results)
        except BaseException as e:
            self.txtInfo.append('<error> 程序无法完成计算, 错误原因: '+str(e))
            return -1

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

# Physical-experiment
>一些计算物理实验的小工具
- 物理不确定度计算程序


## 概述
本程序由私人在课余时间开发 欢迎和我交流

## 环境搭建
python安装: <https://www.python.org/downloads/source/>  
pip安装：<https://pip.pypa.io/en/latest/installing/#id7>  
python依赖：  
```shell
pip install sympy
```

## 使用
### 启动
```shell
python uncertainty_cli.py
```
### 操作
$为提示符 表示需要输入的内容
```shell
请输入需要读取的文件,不需要就乱输入
$
请输入变量列表 如: x y z t
$ x y
请输入函数公式 如 x**y+3*x
$ sin(x)+cos(y)
输入x的单位 c m k ...
$ m
输入x的列表 如: 1 1 1 1 1
$ 1 2 3 1 2
输入系统误差：
$ 0.1
输入y的单位 c m k ...
$ m
输入y的列表 如: 1 1 1 1 1
$ 2 2 1 2 2
输入系统误差：
$ 0.1
x = 1.800000e-03~3.785939e-04
y = 1.800000e-03~2.081666e-04
   @ = 1.001798e+00~3.785935e-04   3.779138e-04
是否保存 y/n
$ n
```

## 源文件查看
- [python命令行启动](./uncertainty_cli.py)

[回到首页](#readme)

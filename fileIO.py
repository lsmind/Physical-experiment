#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def load(file_name):
    with open('./file_name','r') as f:
        content = f.read()
        try:
            content_js = json.loads(content)
        except KeyError:
            print("输入格式有误")
        else:
            return content_js

def save(file_name,content):
    with open('./file_name','w') as f:
        try:
            content_js = json.dumps(content)
        except KeyError:
            print("输入格式有误")
        else:
            f.write(content_js)
